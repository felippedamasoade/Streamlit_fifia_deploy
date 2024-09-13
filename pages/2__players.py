import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)



df_data = st.session_state["data"]

clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[(df_data['Club'] == club)]
players = df_players['Name'].value_counts().index
player = st.sidebar.selectbox("Jogador", players)


player_stars = df_data[df_data['Name'] == player].iloc[0]


st.image(player_stars['Photo'])
st.title(player_stars['Name'])

st.markdown(f"**Clube:** {player_stars['Club']}")
st.markdown(f"*Posição:** {player_stars['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stars['Age']}")
col1.markdown(f"**Altura:** {player_stars['Height(cm.)'] / 100}")
col1.markdown(f"**Peso:** {player_stars['Weight(lbs.)'] * 0.453:.2f}")
st.divider()

st.subheader(f'Overall {player_stars['Overall']}')
st.progress(int(player_stars['Overall']))


col1, col2, col3, col4 = st.columns(4)
col1.metric(label='Valor de Mercado', value=f"£{player_stars['Value(£)']:,}")
col2.metric(label='Remuneração semanal', value=f"£{player_stars['Wage(£)']:,}")
col3.metric(label='Clausula de Rescição', value=f"£{player_stars['Release Clause(£)']:,}")