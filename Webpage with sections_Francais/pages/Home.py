import streamlit as st
import requests
from streamlit_lottie import st_lottie
# Insert at the very top of Home.py
import subprocess
import sys

subprocess.run([sys.executable, "-m", "pip", "install", "streamlit-lottie"], check=True)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/577440fb-123c-4245-9bf6-947b5f020a59/btPr877Yuv.json")


# Original text translated into formal French

st.markdown(
    """
    <style>
    .custom-message {
        color: white;
        background-color: #4CAF50;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        font-size: 16px;
    }
    </style>
    <div class="custom-message">
        Pour une meilleure expérience, veuillez consulter cette application sur un ordinateur.
    </div>
    """,
    unsafe_allow_html=True,
)

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.image("./Assets/RCL93391.jpg", width=250)
    with right_column:
        st.title("Kaviyarasu", anchor=False)
        st.write("Ingénieur industriel")
        if st.button("📧 Prenez contact avec moi"):
            st.switch_page("Views/Contact_me.py")

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("\n")
        st.subheader("Qui suis-je ?", anchor=False)
        st.write(
            """
            - Ingénieur industriel visant à optimiser l’efficacité de la production.
            - Débutant dans la création de diagrammes de modèles industriels.
            - Passionné par la durabilité.
            - Développeur Python émergent.
            """
        )
        with st.container():
            st.subheader("Un ingénieur industriel de France", anchor=False)
            st.write("J’aide les entreprises à optimiser leurs processus de production en utilisant des modèles et diagrammes d’entreprise, tout en privilégiant la durabilité. En combinant des analyses basées sur les données avec l’automatisation, je rends les flux de travail plus efficaces tout en garantissant leur durabilité à long terme. J’utilise également Python pour développer des solutions qui simplifient les tâches et favorisent une prise de décision éclairée.", anchor=False)
    with right_column:

        st_lottie(lottie_coding, height=470, key="Industrial coding")
