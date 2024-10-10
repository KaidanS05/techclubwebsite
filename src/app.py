import streamlit as st
import os
from PIL import Image
from pages import page1
from pages import page2
from pages import page3
from pages import page4

st.set_page_config(
            page_title="NOVA Tech Club",
            layout="wide"
        )

class MultiApp:
    self = "Contact Form"
    def __init__(self):
        self.apps = []
        
    def add_app(self, title, func):
        self.apps.append({title: title, "function": func})
        
    def run(self):
        st.sidebar.markdown("## Main Menu")
        app = st.selectbox(
            "Select Page",
            ("Home Page", "Current Projects", "Achievements", "Contact Form"),
        )
        st.sidebar.markdown("---")

app = MultiApp()

app.add_app("Home Page", page1)
app.add_app("Current Projects", page2)
app.add_app("Achievements", page3)
app.add_app("Contact Form", page4)

app.run()