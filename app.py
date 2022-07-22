import streamlit as st
from multiapp import MultiApp
from apps import create_user, create_graph, create_pixel



app = MultiApp()
st.markdown("""
            
# This is a multi-page app developed by Meet Jethwa
            
""")

app.add_app("Create User", create_user.app)
app.add_app("Create Graph", create_graph.app)
app.add_app("Create Pixel", create_pixel.app)

app.run()