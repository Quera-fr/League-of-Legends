from functions import *

# Configurations de la page
st.set_page_config(page_title="Leag of Legends Dashboard", 
                   page_icon="https://freepngimg.com/save/85643-blue-league-legends-icons-of-symbol-garena/1600x1600", 
                   layout="wide")

st.title("League of Legends Dashboard")
st.video("https://www.leagueoflegends.com/static/hero-c35bd03ceaa5f919e98b20c905044a3d.webm", start_time=0, format='video/webm')

# Afficher la sidebar
streamlit_lol.show_sidebar()

# Afficher les champions
if st.checkbox("Afficher les champions"):
    nb_champion = st.slider('Nombre de champions', 5, 150, 10)
    streamlit_lol.show_champions(streamlit_lol.champions, nb_champion)