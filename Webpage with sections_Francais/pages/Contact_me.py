import streamlit as st
import requests
from streamlit_lottie import st_lottie

def load_lottieur2(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
lottie_contact = load_lottieur2("https://lottie.host/0b9baeae-3718-4b3f-b4eb-1061f7ead868/2emklHnw0a.json")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/Style.css")

# Original text translated into formal French

with st.container():
    st.header("Prenez contact avec moi", anchor=False)

    contact_form = """
    <form action="https://formsubmit.co/kaviyarasu.fr@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Votre nom" required>
        <input type="email" name="email" placeholder="Votre adresse e-mail" required>
        <textarea name="message" placeholder="Votre message ici" required></textarea>
        <button type="submit">Envoyer</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
