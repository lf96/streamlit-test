import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Players",
    page_icon="🏃‍♂️",
    layout="wide",
)

df = st.session_state["data"]

clubes = df["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)
df_filtered = df[df["Club"] == club]

players = df_filtered["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players)

player_stats = df_filtered[df_filtered["Name"] == player].iloc[0]

st.image(player_stats["Photo"])
st.header(player_stats["Name"])
st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)']/100} m")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453592:.2f} kg")

st.divider()

st.subheader(f"Overall: {player_stats['Overall']}")
st.progress(int(player_stats["Overall"]))

col1, col2, col3, col4 = st.columns(4)
col1.metric("Valor de Mercado", f"£ {player_stats['Value(£)']:,}")
col2.metric("Remuneraçào semanal", f"£ {player_stats['Wage(£)']:,}")
col3.metric("Cláusula de rescisão", f"£ {player_stats['Release Clause(£)']:,}")