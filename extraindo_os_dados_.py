import re
import pandas as pd

# Lendo o conteúdo do arquivo de texto
with open('dados.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Função para extrair informações com base em padrões regex
def extract_info(section, pattern):
    match = re.search(pattern, section)
    return match.group(1).strip() if match else None

# Dividindo o conteúdo em seções com base no 'Empregador: '
sections = content.split('Empregador: ')[1:]

# Processando cada seção em um DataFrame
dataframes = []

for section in sections:
    lines = section.split('\n')

    # Extraindo informações comuns da seção
    empregador_info = 'Empregador: ' + extract_info(section, r'(.+?) Cartão de ponto')
    cnpj = extract_info(section, r'CNPJ: (.+?)\s')
    endereco = extract_info(section, r'End: (.+?) Competência')

    competencia = extract_info(section, r'Competência: (.+?)\n')
    unidade = extract_info(section, r'Unidade: (.+?) Data de admissão')
    admissao = extract_info(section, r'Data de admissão (.+)')
    funcionario_id_nome = extract_info(section, r'Funcionário: (\d+ - .+) Cargo:')
    cargo = extract_info(section, r'Cargo: (.+)')

    if funcionario_id_nome:
        funcionario_id, funcionario_nome = funcionario_id_nome.split(' - ')
    else:
        funcionario_id, funcionario_nome = None, None

    # Extraindo registros
    records_start = section.find('Registros Crédito Débitos Faltas e Atrasos') + len('Registros Crédito Débitos Faltas e Atrasos') + 1
    records_end = section.find('Crédito', records_start)
    records = section[records_start:records_end].strip().split('\n')

    # Analisando registros em uma lista de dicionários
    data = []
    for record in records:
        parts = record.split()
        if len(parts) < 14:  # Ignorar registros com elementos ausentes
            continue
        date = parts[0]

        # Extraindo horários
        entrada = parts[1] if len(parts) > 1 else None
        almoco = parts[2] if len(parts) > 2 else None
        retorno_almoco = parts[3] if len(parts) > 3 else None
        saida_expediente = parts[4] if len(parts) > 4 else None

        # Extraindo crédito, débito e faltas e atrasos
        credit = parts[-6] if len(parts) > 10 else None
        debit = parts[-5] if len(parts) > 10 else None
        faltas_atrasos = parts[-4] if len(parts) > 10 else None

        # Corrigindo formatação dos horários
        try:
            entrada = pd.to_datetime(entrada, format='%H:%M').strftime('%H:%M') if entrada else None
        except ValueError:
            entrada = None

        try:
            almoco = pd.to_datetime(almoco, format='%H:%M').strftime('%H:%M') if almoco else None
        except ValueError:
            almoco = None

        try:
            retorno_almoco = pd.to_datetime(retorno_almoco, format='%H:%M').strftime('%H:%M') if retorno_almoco else None
        except ValueError:
            retorno_almoco = None

        try:
            saida_expediente = pd.to_datetime(saida_expediente, format='%H:%M').strftime('%H:%M') if saida_expediente else None
        except ValueError:
            saida_expediente = None

        # Verificando e preenchendo os valores de débito e almoço se estiverem vazios
        if not almoco and entrada and saida_expediente:
            almoco = '12:00'  # Supondo horário padrão de almoço
        if not debit:
            debit = '00:00'  # Preenchendo com um valor padrão

        data.append({
            'Empregador': empregador_info,
            'CNPJ': cnpj,
            'Endereço': endereco,
            'Competência': competencia,
            'Unidade': unidade,
            'Data de admissão': admissao,
            'Funcionário ID': funcionario_id,
            'Funcionário Nome': funcionario_nome,
            'Cargo': cargo,
            'Data': date,
            'Entrada': entrada,
            'Almoço': almoco,
            'Retorno Almoço': retorno_almoco,
            'Saída Expediente': saida_expediente,
            'Crédito': credit,
            'Débito': debit,
            'Faltas e Atrasos': faltas_atrasos
        })

    # Convertendo a lista de dicionários em um DataFrame
    df = pd.DataFrame(data)
    dataframes.append(df)

# Combinando todos os DataFrames em um
combined_df = pd.concat(dataframes, ignore_index=True)

# Definindo o caminho de saída no desktop ou na pasta atual
output_file_path = '01-2024.xlsx'

# Salvando em um arquivo Excel com filtros
with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
    combined_df.to_excel(writer, index=False, sheet_name='Data')
    worksheet = writer.sheets['Data']
    for col_num, value in enumerate(combined_df.columns.values):
        worksheet.write(0, col_num, value)
        worksheet.set_column(col_num, col_num, 20)
    worksheet.autofilter(0, 0, len(combined_df), len(combined_df.columns) - 1)

print(f"Arquivo Excel salvo em: {output_file_path}")
