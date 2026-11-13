
import streamlit as st
from app import chuchubeleza

# Configuração da página
st.set_page_config(
    page_title="Dashboard Meteorológico",
    page_icon="📊",
    layout="wide"
)

# Título da aplicação
st.title("📊 Dashboard Meteorológico")
st.write("Painel de monitoramento — Jaraguá do Sul/SC")

# Botão para atualizar os dados
if st.button("🔄 Consultar novamente"):
    st.rerun()

try:
    # Consulta os dados meteorológicos
    with st.spinner("Atualizando painel..."):
        dados = chuchubeleza()

    if dados is None:
        st.error("Não foi possível obter os dados meteorológicos.")

    else:
        st.success("Painel atualizado.")

        # Indicadores principais
        st.subheader("Indicadores principais")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Latitude",
            f"{dados['latitude']:.4f} "
        )

        col2.metric(
            "Longitude",
            f"{dados['longitude']:.4f}"
        )

        col3.metric(
            "Temperatura",
            f"{dados['current']['temperature_2m']:.1f} °C"
        )

        col4.metric(
            "Velocidade do vento",
            f"{dados['current']['wind_speed_10m']:.1f} km/h"
        )

except Exception as erro:
    st.error(f"Erro ao atualizar o painel: {erro}")
