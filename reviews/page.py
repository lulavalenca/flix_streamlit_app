import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

reviews = [
    {
        "id": 1,
        "stars": 2,
    },
    {
        "id": 2,
        "stars": 3,
    },
    {
        "id": 3,
        "stars": 4,
    },
]


def show_reviews():
    st.write("Lista de Avaliações:")
    AgGrid(
        pd.DataFrame(reviews),
        reload=True,
        key="reviews_grid",
    )
