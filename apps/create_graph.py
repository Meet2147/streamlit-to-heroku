
import streamlit as st
from apps.create_user import *
import requests
import streamlit as st
import streamlit.components.v1 as components

pixela_endpoint = "https://pixe.la/v1/users"
def app():
    
    st.title('Create Graph')
    token = st.text_input('Token')
    username = st.text_input('Username')
    NAME = st.text_input("enter a name for your graph: ")
    UNIT = st.text_input("Enter units like km, hours etc: ")
    TYPE = st.text_input("Enter units type like int, float etc: ")
    COLOR = st.text_input("Enter any color from the mentioned colors shibafu, momiji, sora, ichou, ajisai, kuro: ")
    graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
    GRAPH_ID = st.text_input("enter a graphid: ")
    graph_config = {
        "id": GRAPH_ID,
        "name": NAME,
        "unit": UNIT,
        "type": TYPE,
        "color": COLOR
    }

    headers = {
        "X-USER-TOKEN": token
    }

    response = requests.post(url= graph_endpoint, json=graph_config , headers=headers)
    #st.write(response.text)
    graph_page = f"{graph_endpoint}/{GRAPH_ID}"
    #st.write(graph_page)
    

# embed streamlit docs in a streamlit app
    components.iframe(graph_page)