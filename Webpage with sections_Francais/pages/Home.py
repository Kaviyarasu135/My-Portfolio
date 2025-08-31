import streamlit as st
from pathlib import Path

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

# Get the path to the current script (Home.py)
script_path = Path(__file__)
# Construct the path to the image by going up one directory and then into Assets
image_path = script_path.parent.parent / "Assets" / "RCL93391.jpg"

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        #st.write(" ")
        st.image(str(image_path), width=250)
        #st.image("Webpage with sections_Francais/Assets/RCL93391.jpg", width=250)
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
st.subheader("Un ingénieur industriel de France", anchor=False)
st.write("J’aide les entreprises à optimiser leurs processus de production en utilisant des modèles et diagrammes d’entreprise, tout en privilégiant la durabilité. En combinant des analyses basées sur les données avec l’automatisation, je rends les flux de travail plus efficaces tout en garantissant leur durabilité à long terme. J’utilise également Python pour développer des solutions qui simplifient les tâches et favorisent une prise de décision éclairée.", anchor=False)








