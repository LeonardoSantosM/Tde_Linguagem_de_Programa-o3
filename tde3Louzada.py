# =========================
# QUESTÃO 1 - IMPORTAÇÕES
# =========================
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# =========================
# QUESTÃO 2 - LEITURA E INSPEÇÃO
# =========================
df = pd.read_csv("vendas_brasil_clean_aula6_plotly.csv")

print(df.head())
print(df.shape)
print(df.dtypes)

df['data_venda'] = pd.to_datetime(df['data_venda'])


# =========================
# QUESTÃO 4 - GRÁFICO DE BARRAS
# =========================
df_bar = df.groupby('canal_venda').agg({
    'receita': 'sum',
    'quantidade': 'sum'
}).reset_index()

df_bar = df_bar.sort_values(by='receita', ascending=False)

fig_bar = px.bar(
    df_bar,
    x='canal_venda',
    y='receita',
    hover_data=['quantidade'],
    title='Receita por Canal de Venda'
)

fig_bar.show()


# =========================
# QUESTÃO 5 - GRÁFICO DE LINHA
# =========================
df['mes'] = df['data_venda'].dt.to_period('M').astype(str)

df_line = df.groupby('mes')['receita'].sum().reset_index()

fig_line = px.line(
    df_line,
    x='mes',
    y='receita',
    title='Receita Mensal'
)

fig_line.show()


# =========================
# QUESTÃO 6 - SCATTER PLOT
# =========================
fig_scatter = px.scatter(
    df,
    x='receita',
    y='lucro',
    color='categoria',
    hover_data=['produto', 'canal_venda', 'uf', 'margem_lucro'],
    title='Lucro vs Receita'
)

fig_scatter.show()


# =========================
# QUESTÃO 7 - MAPA
# =========================
fig_map = px.scatter_mapbox(
    df,
    lat='latitude',
    lon='longitude',
    size='receita',
    color='receita',
    hover_name='produto',
    zoom=3,
    mapbox_style='open-street-map',
    title='Distribuição Geográfica das Vendas'
)

fig_map.show()


# =========================
# QUESTÃO 10 - MELHORIA DE CLAREZA
# =========================
fig_bar.update_layout(
    title='Receita Total por Canal de Venda',
    xaxis_title='Canal de Venda',
    yaxis_title='Receita (R$)'
)

fig_bar.show()


# =========================
# QUESTÃO EXTRA (OPCIONAL)
# =========================
fig_extra = px.bar(
    df,
    x='uf',
    y='receita',
    title='Receita por Estado'
)

fig_extra.show()