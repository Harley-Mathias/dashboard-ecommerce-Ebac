# ---------------------------------------------------------
# APP DASH - EBAC ECOMMERCE
# Visualização dos gráficos criados na atividade anterior
# ---------------------------------------------------------

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# -----------------------------
# 1. Carregar os dados
# -----------------------------
df = pd.read_csv("ecommerce_estatistica.csv")

# -----------------------------
# 2. Criar os gráficos
# -----------------------------

# Gráfico 1 – Distribuição de Preços
fig1 = px.histogram(
    df, x="Preço", nbins=20,
    title="Distribuição dos Preços",
    color_discrete_sequence=["#6a0dad"]
)

# Gráfico 2 – Boxplot dos Preços
fig2 = px.box(
    df, y="Preço",
    title="Boxplot dos Preços",
    color_discrete_sequence=["#6a0dad"]
)

# Gráfico 3 – Relação entre Preço e Avaliações
fig3 = px.scatter(
    df, x="Preço", y="N_Avaliações",
    title="Relação entre Preço e Número de Avaliações",
    trendline="ols"
)

# Gráfico 4 – Distribuição das Notas
fig4 = px.histogram(
    df, x="Nota", nbins=10,
    title="Distribuição das Notas",
    color_discrete_sequence=["#6a0dad"]
)

# Gráfico 5 – Boxplot das Notas
fig5 = px.box(
    df, y="Nota",
    title="Boxplot das Notas",
    color_discrete_sequence=["#6a0dad"]
)

# Gráfico 6 – Curva de densidade das Notas
fig6 = px.density_contour(
    df, x="Nota", y="N_Avaliações",
    title="Curva de Densidade das Notas"
)

# Gráfico 7 – Regressão entre Desconto e Vendas
fig7 = px.scatter(
    df,
    x="Desconto",
    y="Qtd_Vendidos_Cod",
    trendline="ols",
    title="Impacto do Desconto nas Vendas",
)

# -----------------------------
# 3. Criar layout com abas
# -----------------------------

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        html.H1("Dashboard - Análise de Ecommerce", className="text-center mt-4"),
        html.Hr(),

        dcc.Tabs(
            [
                dcc.Tab(label="Distribuição de Preços", children=[
                    html.Div([
                        dcc.Graph(figure=fig1)
                    ])
                ]),

                dcc.Tab(label="Boxplot de Preços", children=[
                    html.Div([
                        dcc.Graph(figure=fig2)
                    ])
                ]),

                dcc.Tab(label="Preço x Avaliações", children=[
                    html.Div([
                        dcc.Graph(figure=fig3)
                    ])
                ]),

                dcc.Tab(label="Distribuição das Notas", children=[
                    html.Div([
                        dcc.Graph(figure=fig4)
                    ])
                ]),

                dcc.Tab(label="Boxplot das Notas", children=[
                    html.Div([
                        dcc.Graph(figure=fig5)
                    ])
                ]),

                dcc.Tab(label="Densidade das Notas", children=[
                    html.Div([
                        dcc.Graph(figure=fig6)
                    ])
                ]),

                dcc.Tab(label="Desconto x Vendas", children=[
                    html.Div([
                        dcc.Graph(figure=fig7)
                    ])
                ]),
            ]
        )
    ],
    fluid=True
)

# -----------------------------
# 4. Rodar app
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
