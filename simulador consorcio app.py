import streamlit as st

# Configuração inicial da página
st.set_page_config(page_title="Simulador de Consórcio Pro", layout="centered")

st.title("📊 Simulador de Consórcio Pro")
st.markdown("---")

# Seção de Entrada de Dados
st.subheader("Configurações do Plano")

# Campo: Valor do Consórcio
valor = st.number_input("Valor do Consórcio (R$):", min_value=0.0, value=50000.0, step=1000.0)

# Campo: Taxa de Rendimento (% ao mês)
taxa_input = st.number_input("Taxa de Rendimento (% ao mês):", min_value=0.0, value=0.5, step=0.1) / 100

# Slider: Prazo (A bolinha que você queria)
meses = st.slider("Prazo (Meses):", min_value=1, max_value=240, value=12)

# --- LÓGICA DE CÁLCULO ---
# FÓRMULA DE JUROS COMPOSTOS: M = P * (1 + i)^n
valor_final = valor * ((1 + taxa_input) ** meses)
rendimento = valor_final - valor

# --- EXIBIÇÃO DOS RESULTADOS ---
st.markdown("---")
st.subheader("Resultados da Projeção")

# Criando duas colunas para os resultados ficarem bonitos no celular
col1, col2 = st.columns(2)

with col1:
    st.metric("Rendimento", f"R$ {rendimento:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

with col2:
    st.metric("Total Acumulado", f"R$ {valor_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# Estilização extra para o Rendimento ficar verde (estilo do seu original)
st.markdown(f"""
    <div style="background-color: #d4edda; padding: 20px; border-radius: 10px; text-align: center;">
        <h2 style="color: #155724; margin: 0;">Rendimento Total</h2>
        <h1 style="color: #28a745; margin: 10px 0;">R$ {rendimento:,.2f}</h1>
    </div>
""", unsafe_allow_html=True)

st.info("💡 Mova a barra acima para ver o rendimento mudar instantaneamente!")