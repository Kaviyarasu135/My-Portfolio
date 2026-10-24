
import streamlit as st
from pathlib import Path


BASE_DIR = Path(__file__).parent
profile_pic = BASE_DIR / "Assets" / "Kaviyarasu_Image.jpeg"

col1, col2 = st.columns(
    [1, 2],
    gap="large",
    vertical_alignment="center"
)

with col1:
    st.image(str(profile_pic), width=230)

with col2:

    st.title("Kaviyarasu", anchor=False)

    st.subheader(
        "Doctorant-chercheur à l'ESTP",
        anchor=False
    )

    st.write(
        "**Génie industriel | Jumeaux numériques | "
        "Construction durable**"
    )

    st.caption("Orléans, France")

    st.write(
        """
        Diplômé d'un master en génie industriel
        de Centrale Nantes, je poursuis actuellement
        un doctorat à l'ESTP.

        Mes travaux de recherche portent sur
        l'utilisation des jumeaux numériques
        et des données géospatiales pour
        l'évaluation des ressources minérales
        destinées à la construction
        et à la réhabilitation.
        """
    )

    if st.button(
        "Me contacter",
        type="primary"
    ):
        st.switch_page("pages/Contact_me.py")

st.divider()

st.header("Mon profil", anchor=False)

st.write(
    """
    Mon parcours associe l'ingénierie électrique,
    le génie industriel et la recherche appliquée.

    Après des expériences en automatisation
    industrielle et en analyse de production,
    je me suis orienté vers l'analyse de données
    environnementales et les méthodes numériques
    appliquées aux problématiques de durabilité.

    Cette évolution me permet d'aborder
    les problématiques de recherche
    avec une perspective interdisciplinaire,
    reliant ingénierie, données
    et environnement.
    """
)

st.header("Domaines d'intérêt", anchor=False)

col1, col2 = st.columns(2, gap="large")

with col1:

    st.markdown("**Jumeaux numériques**")
    st.write(
        "Exploration des approches numériques "
        "pour la représentation et l'analyse "
        "des systèmes physiques."
    )

    st.markdown("**Géomatique et analyse de données**")
    st.write(
        "Exploitation de données géospatiales "
        "et environnementales pour l'analyse "
        "et l'aide à la décision."
    )

with col2:

    st.markdown("**Construction durable**")
    st.write(
        "Étude des ressources minérales "
        "et des matériaux mobilisables "
        "pour la construction."
    )

    st.markdown("**Ingénierie industrielle**")
    st.write(
        "Automatisation, analyse des systèmes "
        "et optimisation des processus."
    )

st.divider()

st.header("Recherche actuelle", anchor=False)

st.markdown(
    "**BASTIR - Jumeau numérique pour le bilan "
    "d'approvisionnement en ressources minérales**"
)

st.write(
    """
    Mes travaux doctoraux à l'ESTP visent
    à étudier l'intégration de données
    territoriales, géologiques et relatives
    aux infrastructures dans une approche
    de jumeau numérique.

    Cette recherche s'inscrit dans
    les enjeux de gestion durable des
    ressources pour la construction
    et la réhabilitation.
    """
)

if st.button("Découvrir mes projets"):
    st.switch_page("pages/Projects.py")


