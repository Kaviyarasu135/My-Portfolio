from pathlib import Path
import streamlit as st
from PIL import Image


st.markdown(
    """
    <style>
    h3 {
        position: relative;
    }
    h3 a {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#st.info("For a better experience, please view this application on a computer.")
# Get the folder this script is in (pages/)
BASE_DIR = Path(__file__).parent

# Build absolute paths from the current script location
resume_file_anglais = BASE_DIR / "Assets" / "Anglais.pdf"
resume_file_francais = BASE_DIR / "Assets" / "Francais.pdf"
profile_pic = BASE_DIR / "Assets" / "RCL93391.JPG"


with open(resume_file_anglais, "rb") as pdf_file_anglais:
    PDFbyte_anglais = pdf_file_anglais.read()

with open(resume_file_francais, "rb") as pdf_file_francais:
    PDFbyte_francais = pdf_file_francais.read()

profile_pic = Image.open(profile_pic)

col1, col2 = st.columns(2, gap="small")
with col2:
    st.image(profile_pic, width=215)
    if st.button(" Prenez contact avec moi"):#📧
            st.switch_page("pages/Contact_me.py")


# Original text translated into formal French

with col1:
    st.title("Kaviyarasu", anchor=False)
    st.write("Ingénieur & Passionné de Développement durable")
    st.write("Kaviyarasu.Sakthivel@eleves.ec-nantes.fr | 0780831482 | Nantes, France")
    st.write("[LinkedIn](https://linkedin.com/in/kaviyarasu-sakthivel) | kaviyarasu.streamlit.app")
    st.write("\n")
  
    st.download_button(
        label="Télécharger le CV ",
        data=PDFbyte_francais,
        file_name=resume_file_francais.name,
        mime="application/octet-stream",
    )

st.markdown("<h3><u>Expérience et qualifications</u></h3>", unsafe_allow_html=True)
st.write(
    """
- Ingénieur industriel spécialisé dans l’optimisation des processus de production pour améliorer les performances et la rentabilité.
- Passionné par la durabilité, intégrant des facteurs économiques, sociaux et environnementaux dans les opérations industrielles.
- Solide expérience pratique en programmation de PLC avec des automates Beckhoff.
- Analytique et adaptable, axé sur l’amélioration continue dans la fabrication et la modélisation industrielle.
    """
)
st.markdown("<h3><u>Formation</u></h3>", unsafe_allow_html=True)
st.write(
    """
- Master en ingénierie industrielle| École Centrale de Nantes (2024 - 2026)
- Licence en ingénierie électrique et électronique | KPR Institute of Engineering (2020 - 2024)
    """
)
st.markdown("<h3><u>Historique professionnel</u></h3>", unsafe_allow_html=True)
st.write("**Stagiaire R&D | Kone Elevators and Escalators**")
st.write("(07/2023 - 05/2024 | Chennai, Inde)")
st.write(
    """
- Développé des programmes PLC à l’aide d’automates Beckhoff, configuré des modules d’entrée/sortie et effectué le dépannage des systèmes.
- Appliqué des principes de durabilité pour optimiser les processus et soutenir les initiatives de réduction des déchets.
- Contribué à la planification des ressources, identifié les goulots d’étranglement et proposé des améliorations de l’efficacité.
    """
)
st.write("**Stagiaire en analyse de la qualité | Sarmangal**")
st.write("(01/2023 - 07/2023 | Coimbatore, Inde)")
st.write(
    """
- Évalué les processus de production à travers une perspective de durabilité, mettant l’accent sur l’efficacité des ressources et les pratiques de fabrication éthiques.
- Identifié les inefficacités et recommandé des améliorations pour améliorer la qualité et réduire le gaspillage de matériaux.
- Créé et interprété des diagrammes de flux de processus et des graphiques de contrôle de la qualité pour optimiser la production.
    """
)
st.markdown("<h3><u>Compétences techniques</u></h3>", unsafe_allow_html=True)
st.write(
    """
- Programmation : Python (Pandas, NumPy, Matplotlib, etc.), programmation de PLC (Beckhoff).
- Analyse et visualisation de données : Excel, Python (Streamlit, etc.).
- Systèmes industriels : durabilité, gestion de la production, gestion de projets.
- Fabrication : optimisation des processus, contrôle de la qualité.
    """
)
st.markdown("<h3><u>Projets</u></h3>", unsafe_allow_html=True)
st.write(
    """
- Chargement dynamique des véhicules électriques
- Automatisation de la mesure de puissance à l’aide de PLC
- Analyse stratégique et durabilité d’une entreprise
    """
)
st.markdown("<h3><u>Langues</u></h3>", unsafe_allow_html=True)
st.write(
    """
- **Anglais** (C2 – Septembre 2025)
- **Français** (B2 – Septembre 2025)
    """
)
#- **Tamoul** (Langue maternelle)
st.markdown("<h3><u>Temps consacré dans une journée</u></h3>", unsafe_allow_html=True)
st.write(
    """
- Lecture de littérature professionnelle
- Apprentissage interdisciplinaire
- Amélioration de la maîtrise du français
- Lecture de science-fiction
- Developpment personnel
- Moments de pause
- Perfectionnement en programmation Python
- Recherche d’un jeu vidéo à explorer
- Renforcement de la pensée logique et des capacités de résolution de problèmes
    """
)
st.markdown("<h3><u>Valeurs fondamentales</u></h3>", unsafe_allow_html=True)
st.write(
    """
- **Honnêteté** – Intégrité avant la commodité dans chaque décision.
- **Engagement** – Rester concentré sur la croissance à long terme.
- **Discipline** – Une approche structurée du travail et de l’apprentissage.
- **Constance** – De petites actions persistantes mènent à de grands résultats.
    """
)

st.markdown("<h3><u>Objectif de vie</u></h3>", unsafe_allow_html=True)
st.write(
    """
"La véritable croissance ne vient pas seulement de s’améliorer soi-même, mais aussi d’élever les autres au fur et à mesure de son progrès."
    """

)







