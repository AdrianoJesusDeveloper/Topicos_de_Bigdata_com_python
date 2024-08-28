import streamlit as st
import pandas as pd

# Carregar os dados
@st.cache_data
def load_data():
    file_path = 'c:/Users/adria/Desktop/tabela de Ponto/01-2024.xlsx'
    df = pd.read_excel(file_path, sheet_name='Data')
    return df

df = load_data()

st.title('Dashboard de Ponto')

# Métrica 1: Quantidade de colaboradores
num_colaboradores = df['Funcionário Nome'].nunique()
st.metric("Quantidade de Colaboradores", num_colaboradores)

# Métrica 2: Batida de pontos (atrasos e pontualidade)
df['Faltas e Atrasos'] = df['Faltas e Atrasos'].astype(str).fillna('')
atraso = df[df['Faltas e Atrasos'].str.contains('Atraso', na=False)].shape[0]
pontualidade = df.shape[0] - atraso
st.write(f"Total de Atrasos: {atraso}")
st.write(f"Total de Pontualidade: {pontualidade}")

# Métrica 3: Quantidade de horas trabalhadas por cargo
# Certifique-se de que 'Saída Expediente' está em formato de hora
df['Horas Trabalhadas'] = pd.to_datetime(df['Saída Expediente'], format='%H:%M', errors='coerce').dt.hour
horas_por_cargo = df.groupby('Cargo')['Horas Trabalhadas'].sum()
st.bar_chart(horas_por_cargo)

# Adicionar gráficos e tabelas adicionais conforme necessário
st.write("Dados Detalhados:")
st.dataframe(df)