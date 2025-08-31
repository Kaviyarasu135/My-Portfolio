import streamlit as st


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/Style.css")

# Original text translated into formal French
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

st.write(contact_form, unsafe_allow_html=True)



