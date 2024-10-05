import streamlit as st
from streamlit_option_menu import option_menu

from rules import rulesBisaya, rulesEnglish
from tools import tools
from charlie_gpt import charlieGPT

with st.sidebar:
    selected = option_menu(
        "Menu", 
        [
            "Rules",
            "Tools",
            "Charlie GPT"
        ], 
        icons=[
            'check-circle-fill',
            'google-play',
            "robot"
        ], menu_icon="list", default_index=2
    )

if selected == "Rules":
    rulesBisaya()
elif selected == "Tools":
    tools()
elif selected == "Charlie GPT":
    charlieGPT()