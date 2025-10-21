import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

movies = [
    {"id": 1, "name": "Velozes e Furiosos"},
    {"id": 2, "name": "De volta para o Futuro"},
    {"id": 3, "name": "Jason"},
]


def show_movies():
    st.write("Lista de Filmes:")
    AgGrid(
        pd.DataFrame(movies),
        reload=True,
        key="movies_grid",
    )

    st.title("Cadastrar novo Filme")
    name = st.text_input("Nome do Filme")
    if st.button("Cadastrar"):
        st.success(f'Filme "{name}" cadastrado com sucesso!')
