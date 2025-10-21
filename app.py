import streamlit as st
from genres.page import show_genres
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviews
from st_aggrid import AgGrid


def main():
    st.title("Flix App")

    menu_options = st.sidebar.selectbox(
        "Selecione uma opção",
        ["Inicio", "Generos", "Atores/Atrizes", "Filmes", "Avaliações"],
    )

    if menu_options == "Inicio":
        st.write("Inicio")

    if menu_options == "Generos":
        show_genres()

    if menu_options == "Atores/Atrizes":
        show_actors()

    if menu_options == "Filmes":
        show_movies()

    if menu_options == "Avaliações":
        show_reviews()


if __name__ == "__main__":
    main()
