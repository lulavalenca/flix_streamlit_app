import streamlit as st 
from genres.page import show_genres

def main():
    st.title("Flix App")
    
    menu_options = st.sidebar.selectbox(
        'Selecione uma opção',
        ['Inicio', 'Generos', 'Atores/Atrizes', 'Filmes', 'Avaliações']
    )
    
    if menu_options == 'Inicio':
        st.write('Inicio')
        
    if menu_options == 'Generos':
        show_genres()

    if menu_options == 'Atores/Atrizes':
        st.write('Atores/Atrizes')

    if menu_options == 'Filmes':
        st.write('Filmes')

    if menu_options == 'Avaliações':
        st.write('Avaliações')

if __name__ == "__main__":
    main()  