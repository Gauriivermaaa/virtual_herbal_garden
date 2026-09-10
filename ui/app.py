import streamlit as st

from config import (
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT
)

from auth import init_db

from styles.theme import apply_theme

from components.sidebar import render_sidebar

from views.login import login_page
from views.home import home_page
from views.garden import garden_page
from views.herb_details import herb_page
from views.chat import chat_page
from views.upload import upload_page


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# DATABASE INIT
# --------------------------------------------------

init_db()


# --------------------------------------------------
# APPLY THEME
# --------------------------------------------------

apply_theme()


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_email" not in st.session_state:
    st.session_state.user_email = ""

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# LOGIN STATE
# --------------------------------------------------

if not st.session_state.logged_in:

    login_page()

else:

    render_sidebar()

    if st.session_state.page == "Home":
        home_page()

    elif st.session_state.page == "Garden":
        garden_page()

    elif st.session_state.page == "Herb":
        herb_page()

    elif st.session_state.page == "Chat":
        chat_page()

    elif st.session_state.page == "Upload":
        upload_page()