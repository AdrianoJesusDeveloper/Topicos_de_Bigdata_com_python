import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Função para ler os dados de um arquivo CSV
def read_from_csv(file_path):
    return pd.read_csv(file_path)

# Carregar dados processados com Spark
horas_extras_filial_acumulado = read_from_csv('c:/Users/adria/Desktop/tabela de ponto/horas_extras_filial_acumulado.csv')
horas_extras_filial_mes = read_from_csv('c:/Users/adria/Desktop/tabela de ponto/horas_extras_filial_mes.csv')
horas_extras_colaborador_mes = read_from_csv('c:/Users/adria/Desktop/tabela de ponto/horas_extras_colaborador_mes.csv')
saldo_positivo_top10 = read_from_csv('c:/Users/adria/Desktop/tabela de ponto/saldo_positivo_top10.csv')
saldo_negativo_top10 = read_from_csv('c:/Users/adria/Desktop/tabela de ponto/saldo_negativo_top10.csv')
faltas_atrasos_colaborador_mes = read_from_csv('c:/Users/adria/Desktop/tabela de ponto/faltas_atrasos_colaborador_mes.csv')
faltas_atrasos_colaborador_acumulado = read_from_csv('c:/Users/adria/Desktop/tabela de ponto/faltas_atrasos_colaborador_acumulado.csv')
faltas_atrasos_filial_mes = read_from_csv('c:/Users/adria/Desktop/tabela de ponto/faltas_atrasos_filial_mes.csv')
faltas_atrasos_filial_acumulado = read_from_csv('c:/Users/adria/Desktop/tabela de ponto/faltas_atrasos_filial_acumulado.csv')

# Inicializar a aplicação Dash
app = dash.Dash(__name__)

# Layout da aplicação
app.layout = html.Div([
    html.H1("Dashboard de Análise de Ponto de Funcionários"),
    dcc.Tabs([
        dcc.Tab(label="Horas Extras por Filial", children=[
            dcc.Graph(id='horas-extras-filial-acumulado',
                      figure=px.bar(horas_extras_filial_acumulado, x='Unidade', y='Crédito',
                                    title='Quantidade de Horas Extras por Filial - Acumulado')),
            dcc.Graph(id='horas-extras-filial-mes',
                      figure=px.line(horas_extras_filial_mes, x='Mês', y='Crédito', color='Unidade',
                                     title='Quantidade de Horas Extras por Filial - Mês a Mês'))
        ]),
        dcc.Tab(label="Horas Extras por Colaborador", children=[
            dcc.Graph(id='horas-extras-colaborador-mes',
                      figure=px.line(horas_extras_colaborador_mes, x='Mês', y='Crédito', color='Funcionário Nome',
                                     title='Quantidade de Horas Extras por Colaborador - Mês a Mês')),
            dcc.Graph(id='saldo-positivo-top10',
                      figure=px.bar(saldo_positivo_top10, x='Funcionário Nome', y='Crédito',
                                    title='Top 10 Colaboradores com Saldo Positivo')),
            dcc.Graph(id='saldo-negativo-top10',
                      figure=px.bar(saldo_negativo_top10, x='Funcionário Nome', y='Débito',
                                    title='Top 10 Colaboradores com Saldo Negativo'))
        ]),
        dcc.Tab(label="Faltas e Atrasos", children=[
            dcc.Graph(id='faltas-atrasos-colaborador-mes',
                      figure=px.line(faltas_atrasos_colaborador_mes, x='Mês', y='Faltas e Atrasos', color='Funcionário Nome',
                                     title='Quantidade de Faltas/Atrasos por Colaborador - Mês a Mês')),
            dcc.Graph(id='faltas-atrasos-colaborador-acumulado',
                      figure=px.bar(faltas_atrasos_colaborador_acumulado, x='Funcionário Nome', y='Faltas e Atrasos',
                                    title='Quantidade de Faltas/Atrasos por Colaborador - Acumulado')),
            dcc.Graph(id='faltas-atrasos-filial-mes',
                      figure=px.line(faltas_atrasos_filial_mes, x='Mês', y='Faltas e Atrasos', color='Unidade',
                                     title='Quantidade de Faltas/Atrasos por Filial - Mês a Mês')),
            dcc.Graph(id='faltas-atrasos-filial-acumulado',
                      figure=px.bar(faltas_atrasos_filial_acumulado, x='Unidade', y='Faltas e Atrasos',
                                    title='Quantidade de Faltas/Atrasos por Filial - Acumulado'))
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
