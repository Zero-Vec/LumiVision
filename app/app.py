import streamlit as st
import start_page
import chat_page


st.logo("logo_new.png", size="large")
start_page = st.Page("start_page.py", title="欢迎", icon="💞")
chat_page = st.Page("chat_page.py", title="视讯灵眸", icon="🤖")

pages = [start_page, chat_page]
pg = st.navigation(pages) # 导航栏
st.set_page_config(
    page_title="视讯灵眸",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🤖",
)

pg.run()
