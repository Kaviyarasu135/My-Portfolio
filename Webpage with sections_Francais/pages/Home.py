import streamlit as st
from pathlib import Path
from PIL import Image
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
#st.info("For a better experience, please view this application on a computer.")
# Get the folder this script is in (pages/)
BASE_DIR = Path(__file__).parent

profile_pic = BASE_DIR / "Assets" / "RCL93391.JPG"

profile_pic = Image.open(profile_pic)

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.image(profile_pic, width=215)
    with right_column:
        st.title("Kaviyarasu", anchor=False)
        st.write("Ingénieur industriel")
        if st.button("📧 Prenez contact avec moi"):
            st.switch_page("pages/Contact_me.py")


st.subheader("Qui suis-je ?", anchor=False)
st.write(
            """
            - Ingénieur industriel visant à optimiser l’efficacité de la production.
            - Débutant dans la création de diagrammes de modèles industriels.
            - Passionné par la durabilité.
            - Développeur Python émergent.
            """
        )
st.subheader("Un ingénieur industriel en France", anchor=False)
st.write(
    "J’aide les entreprises à optimiser leurs processus de production en utilisant des modèles et diagrammes d’entreprise, tout en privilégiant la durabilité. En combinant des analyses basées sur les données avec l’automatisation, je rends les flux de travail plus efficaces tout en garantissant leur durabilité à long terme. J’utilise également Python pour développer des solutions qui simplifient les tâches et favorisent une prise de décision éclairée."
)























