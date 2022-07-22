import streamlit as st
from apps.create_user import *
import requests
import streamlit as st
import streamlit.components.v1 as components

def app():
    st.title('Create Pixel')
    token = st.text_input('Token')
    username = st.text_input('Username')
    GRAPH_ID = st.text_input("Enter your graphid: ")
    QUANTITY = st.text_input("Enter the quantity in hours: ")
    date = st.date_input("enter the date: ")
    
    pixel_creation_endpoint = f"{pixela_endpoint}/{username}/graphs/{GRAPH_ID}"

    # print(today)

    pixel_data = {
        "date": date.strftime("%Y%m%d"),
        "quantity": QUANTITY,
    }
    headers = {
        "X-USER-TOKEN": token
    }

    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
    
    st.write(pixel_creation_endpoint)
    components.iframe(pixel_creation_endpoint,width=900,height=300)