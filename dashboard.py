import dash
from dash import dcc, html
import plotly.express as px
import preparando_dashboard as pdb

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard de Análise de Ponto de Funcionários"),
    dcc.Tabs([
        dcc.Tab(label="Horas Extras por Filial", children=[
            dcc.Graph(id='horas-extras-filial-acumulado',
                      figure=px.bar(pdb.horas_extras_filial_acumulado, x='Unidade', y='Crédito',
                                    title='Quantidade de Horas Extras por Filial - Acumulado')),
            dcc.Graph(id='horas-extras-filial-mes',
                      figure=px.line(pdb.horas_extras_filial_mes, x='Mês', y='Crédito', color='Unidade',
                                     title='Quantidade de Horas Extras por Filial - Mês a Mês'))
        ]),
        dcc.Tab(label="Horas Extras por Colaborador", children=[
            dcc.Graph(id='horas-extras-colaborador-mes',
                      figure=px.line(pdb.horas_extras_colaborador_mes, x='Mês', y='Crédito', color='Funcionário Nome',
                                     title='Quantidade de Horas Extras por Colaborador - Mês a Mês')),
            dcc.Graph(id='saldo-positivo-top10',
                      figure=px.bar(pdb.saldo_positivo_top10, x='Funcionário Nome', y='Crédito',
                                    title='Top 10 Colaboradores com Saldo Positivo')),
            dcc.Graph(id='saldo-negativo-top10',
                      figure=px.bar(pdb.saldo_negativo_top10, x='Funcionário Nome', y='Débito',
                                    title='Top 10 Colaboradores com Saldo Negativo'))
        ]),
        dcc.Tab(label="Faltas e Atrasos", children=[
            dcc.Graph(id='faltas-atrasos-colaborador-mes',
                      figure=px.line(pdb.faltas_atrasos_colaborador_mes, x='Mês', y='Faltas e Atrasos', color='Funcionário Nome',
                                     title='Quantidade de Faltas/Atrasos por Colaborador - Mês a Mês')),
            dcc.Graph(id='faltas-atrasos-colaborador-acumulado',
                      figure=px.bar(pdb.faltas_atrasos_colaborador_acumulado, x='Funcionário Nome', y='Faltas e Atrasos',
                                    title='Quantidade de Faltas/Atrasos por Colaborador - Acumulado')),
            dcc.Graph(id='faltas-atrasos-filial-mes',
                      figure=px.line(pdb.faltas_atrasos_filial_mes, x='Mês', y='Faltas e Atrasos', color='Unidade',
                                     title='Quantidade de Faltas/Atrasos por Filial - Mês a Mês')),
            dcc.Graph(id='faltas-atrasos-filial-acumulado',
                      figure=px.bar(pdb.faltas_atrasos_filial_acumulado, x='Unidade', y='Faltas e Atrasos',
                                    title='Quantidade de Faltas/Atrasos por Filial - Acumulado'))
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)

