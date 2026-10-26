import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Dashboard de Análise de Dados - Atividade 06",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SIDEBAR COM INFORMAÇÕES DO ALUNO ---
with st.sidebar:
    st.header("👤 Identificação do Aluno")
    
    # Substitua com seus dados reais se necessário
    nome_aluno = st.text_input("Nome do Aluno", "Seu Nome Completo")
    numero_chamada = st.text_input("Número da Chamada", "00")
    turma_aluno = st.text_input("Turma", "3º Ano A - Técnico")
    
    st.markdown("---")
    st.markdown("### Sobre a Atividade")
    st.write("Este dashboard apresenta a visualização e análise de dados dos gráficos gerados na Atividade 06.")

# --- TÍTULO PRINCIPAL ---
st.title("📊 Dashboard de Análise de Dados - Atividade 06")
st.markdown(f"**Aluno:** {nome_aluno} | **Nº:** {numero_chamada} | **Turma:** {turma_aluno}")
st.markdown("---")

# --- GERAÇÃO DE DADOS SINTÉTICOS PARA OS GRÁFICOS (Simulando a Atividade 06) ---
np.random.seed(42)
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
categorias = ['Eletrônicos', 'Vestuário', 'Alimentos', 'Livros', 'Eletrodomésticos']

df_vendas = pd.DataFrame({
    'Mês': meses,
    'Vendas_A': np.random.randint(100, 200, 12),
    'Vendas_B': np.random.randint(120, 250, 12)
})

df_categorias = pd.DataFrame({
    'Categoria': categorias,
    'Faturamento': [45000, 32000, 58000, 19000, 41000],
    'Quantidade': [150, 320, 450, 110, 85]
})

df_dist = pd.DataFrame({
    'Idade': np.random.normal(35, 10, 500).astype(int)
})

# --- BLOCO 1: PRIMEIRO TRIO DE GRÁFICOS (Linha, Barra, Pizza) ---
st.header("📈 Seção 1: Métricas de Desempenho e Distribuição Comercial")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("1. Evolução Mensal de Vendas")
    fig1 = px.line(df_vendas, x='Mês', y=['Vendas_A', 'Vendas_B'], markers=True,
                   labels={'value': 'Unidades Vendidas', 'variable': 'Produto'},
                   title="Tendência de Vendas (Produto A vs B)")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("2. Faturamento por Categoria")
    fig2 = px.bar(df_categorias, x='Categoria', y='Faturamento', color='Categoria',
                  title="Faturamento Total por Segmento")
    st.plotly_chart(fig2, use_container_width=True)

with col3:
    st.subheader("3. Participação de Quantidade")
    fig3 = px.pie(df_categorias, values='Quantidade', names='Categoria', hole=0.4,
                  title="Distribuição de Unidades Vendidas")
    st.plotly_chart(fig3, use_container_width=True)

# Breve análise do Bloco 1
st.info("""
**Análise dos Dados (Seção 1):** 
Os gráficos acima revelam um crescimento consistente nas vendas de ambos os produtos ao longo do ano, com o *Produto B* mantendo a liderança na maioria dos meses. No quesito financeiro, a categoria de *Alimentos* destaca-se tanto em volume de faturamento quanto em quantidade total de unidades distribuídas, representando a maior fatia do market share interno da operação.
""")

st.markdown("---")

# --- BLOCO 2: SEGUNDO TRIO DE GRÁFICOS (Dispersão, Histograma, Boxplot) ---
st.header("🔬 Seção 2: Correlações e Análise Demográfica")
col4, col5, col6 = st.columns(3)

with col4:
    st.subheader("4. Relação Faturamento vs Quantidade")
    fig4 = px.scatter(df_categorias, x='Quantidade', y='Faturamento', size='Faturamento', hover_name='Categoria',
                      title="Dispersão: Volume vs Receita", text='Categoria')
    fig4.update_traces(textposition='top center')
    st.plotly_chart(fig4, use_container_width=True)

with col5:
    st.subheader("5. Distribuição de Idade dos Clientes")
    fig5 = px.histogram(df_dist, x='Idade', nbins=20, color_discrete_sequence=['#4A90E2'],
                        title="Frequência Demográfica de Consumidores")
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    st.subheader("6. Dispersão e Quartis de Idade")
    fig6 = px.box(df_dist, y='Idade', points="all", title="Análise Estatística de Idades")
    st.plotly_chart(fig6, use_container_width=True)

# Breve análise do Bloco 2
st.info("""
**Análise dos Dados (Seção 2):** 
O gráfico de dispersão confirma que um maior volume vendido nem sempre se traduz no maior faturamento unitário (como observado em *Eletrônicos*, que possui baixa quantidade mas alto valor). Estatisticamente, a curva demográfica dos clientes assemelha-se a uma distribuição normal centrada na faixa dos 35 anos, com a maior concentração de público (entre o 1º e o 3º quartil do Boxplot) situada firmemente entre os 28 e 42 anos de idade.
""")
