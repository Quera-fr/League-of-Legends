from functions import *

st.set_page_config(page_title="Leag of Legends Dashboard",
                     page_icon="https://freepngimg.com/save/85643-blue-league-legends-icons-of-symbol-garena/1600x1600",
                     layout="wide")

streamlit_lol.show_sidebar()
st.title("Historique des Champions")

database = DataBase('database_lol')
df = pd.DataFrame(database.select_table('champions'))

# Show data
if st.checkbox("Afficher l'historique des champions en fonction de la date de collecte"):
    date = st.selectbox('Choisir la date de collecte', df['time'].unique())
    st.write(df[df.time == date])

if st.checkbox("Afficher l'historique des champions en fonction du rôle"):
    role = st.multiselect('Choisir le rôle', df['role'].unique())
    st.write(df[df.role.apply(lambda x: x in role)])

if st.checkbox("Afficher l'historique des champions en fonction du nom"):
    name = st.multiselect('Choisir le nom', df['id_champion'].unique())
    df_champion = df[df.id_champion.apply(lambda x: x in name)]

    for i in range(len(df_champion)):
        col1, col2 = st.columns(2)
        with col1:
            st.title(df_champion.iloc[i]['id_champion'])
            st.write('Rôle : ' + df_champion.iloc[i]['role'])
            st.write(df_champion.iloc[i]['desciption'])
            
        with col2:
            st.image(df_champion.iloc[i]['img'])


st.title("League of Legends Bot !")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Posez-moi votre question sur les champions de League of Legends !"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = streamlit_lol.chat_openAI(prompt, database)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})