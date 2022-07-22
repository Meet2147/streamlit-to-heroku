import streamlit as st
import requests
from datetime import datetime
import streamlit as st
import streamlit.components.v1 as components

pixela_endpoint = "https://pixe.la/v1/users"
pixela_new = "https://pixe.la/@"
def app():
    at = "@"
    st.title('Create User')
    token = st.text_input('Token')
    username = st.text_input('Username')
    agreeTermsofService = st.selectbox("Agree Terms",('yes','no'))
    notMinor = st.selectbox("Not a Minor",('yes', 'no'))
    user_params = {
        "token":token,
        "username": username,
        "agreeTermsofService":agreeTermsofService,
        "notMinor":notMinor
        
    }
    response = requests.post(url=pixela_endpoint, json=user_params)
    #st.write(response.json())
    user_page = f"{pixela_new}{username}"
    st.write(user_page)
    # st.write(response.text)
    components.iframe(user_page,width=800,height=600)
    