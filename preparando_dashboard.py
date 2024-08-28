import pandas as pd

# Passo 2: Carregar o Arquivo Excel
file_path = '01-2024.xlsx'  # Substitua pelo caminho correto
df = pd.read_excel(file_path)

# Exibir as primeiras linhas para inspeção
#print(df.head())

# Passo 3: Calcular as Métricas Requeridas

# 1. Quantidade de horas extras por filial - Acumulado
horas_extras_filial_acumulado = df.groupby('Unidade')['Crédito'].sum().reset_index()

# 2. Quantidade de horas extras por filial - Mês a mês
df['Data'] = pd.to_datetime(df['Data'], format="%d.%m.%Y")  # Ajuste o formato da data conforme necessário
df['Mês'] = df['Data'].dt.to_period('M')
horas_extras_filial_mes = df.groupby(['Unidade', 'Mês'])['Crédito'].sum().reset_index()

# 3. Quantidade de horas extras por colaborador - Mês a mês
horas_extras_colaborador_mes = df.groupby(['Funcionário Nome', 'Mês'])['Crédito'].sum().reset_index()

# 4. Top 10 colaboradores com saldo positivo
saldo_positivo_top10 = df.groupby('Funcionário Nome')['Crédito'].sum().nlargest(10).reset_index()

# 5. Top 10 colaboradores com saldo negativo
# Converta a coluna 'Débito' para numérico e trate valores não numéricos
df['Débito'] = pd.to_numeric(df['Débito'], errors='coerce')
saldo_negativo_top10 = df.groupby('Funcionário Nome')['Débito'].sum().nlargest(10).reset_index()

# 6. Quantidade de faltas/atrasos por colaborador - Mês
faltas_atrasos_colaborador_mes = df.groupby(['Funcionário Nome', 'Mês'])['Faltas e Atrasos'].sum().reset_index()

# 7. Quantidade de faltas/atrasos por colaborador - Acumulado
faltas_atrasos_colaborador_acumulado = df.groupby('Funcionário Nome')['Faltas e Atrasos'].sum().reset_index()

# 8. Quantidade de faltas/atrasos por filial - Mês a mês
faltas_atrasos_filial_mes = df.groupby(['Unidade', 'Mês'])['Faltas e Atrasos'].sum().reset_index()

# 9. Quantidade de faltas/atrasos por filial - Acumulado
faltas_atrasos_filial_acumulado = df.groupby('Unidade')['Faltas e Atrasos'].sum().reset_index()

#Exportar os DataFrames para uso no dashboard (opcional, apenas para depuração)
horas_extras_filial_acumulado.to_csv('horas_extras_filial_acumulado.csv', index=False)
horas_extras_filial_mes.to_csv('horas_extras_filial_mes.csv', index=False)
horas_extras_colaborador_mes.to_csv('horas_extras_colaborador_mes.csv', index=False)
saldo_positivo_top10.to_csv('saldo_positivo_top10.csv', index=False)
saldo_negativo_top10.to_csv('saldo_negativo_top10.csv', index=False)
faltas_atrasos_colaborador_mes.to_csv('faltas_atrasos_colaborador_mes.csv', index=False)
faltas_atrasos_colaborador_acumulado.to_csv('faltas_atrasos_colaborador_acumulado.csv', index=False)
faltas_atrasos_filial_mes.to_csv('faltas_atrasos_filial_mes.csv', index=False)
faltas_atrasos_filial_acumulado.to_csv('faltas_atrasos_filial_acumulado.csv', index=False)
