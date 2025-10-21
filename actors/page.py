import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


actors = [
    {"id": 1, "name": "The Rock"},
    {"id": 2, "name": "Kevin Hart"},
    {"id": 3, "name": "Scarlett Johansson"},
]


def show_actors():
    st.write("Lista de Atores/Atrizes:")
    AgGrid(
        pd.DataFrame(actors),
        reload=True,
        key="actors_grid",
    )

    st.title("Cadastrar novo Ator/Atriz")
    name = st.text_input("Nome do Ator/Atriz")

    if st.button("Cadastrar"):
        st.success(f'Ator/Atriz "{name}" cadastrado com sucesso!')
