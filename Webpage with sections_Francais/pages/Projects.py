import streamlit as st

st.title("Recherche & projets")
st.write("Une sélection de mes travaux de recherche et de mes projets d’ingénierie.")
st.divider()

st.subheader("BASTIR · Recherche doctorale")
st.caption("ESTP · Depuis octobre 2026 · En cours")
st.write(
    "**Jumeau numérique pour le bilan d’approvisionnement en ressources minérales issues des sols, "
    "des terres et des infrastructures pour la construction et la réhabilitation.**"
)
st.write(
    "Cette thèse explore l’intégration de données sur les ressources minérales, "
    "les bâtiments et les territoires afin d’éclairer l’évaluation des ressources mobilisables. "
    "Les premiers travaux portent notamment sur la revue bibliographique, la découverte de "
    "sources institutionnelles et l’exploration géospatiale dans QGIS."
)
st.caption("Axes étudiés : géomatique · données sur le bâti · matériaux · jumeaux numériques")
st.divider()

st.subheader("Fiabilité des données climatiques et matérialité")
st.caption("Stage de recherche · ESTP, Cachan · Mars–août 2026")
st.write(
    "Analyse et traitement de données climatiques pour améliorer leur exploitation "
    "dans une démarche d’évaluation environnementale et de matérialité. "
    "Travaux réalisés sur les jeux de données EXPLORE2, TRACC et DRIAS, "
    "avec des scripts de traitement, des tableaux de bord et des analyses statistiques."
)
st.caption("Méthodes : Python · Excel · visualisation · analyse en composantes principales")
st.divider()

st.subheader("Projets d’ingénierie antérieurs")
with st.expander("Automatisation de la mesure de puissance avec des automates programmables"):
    st.write(
        "Projet lié à l’instrumentation et à l’automatisation industrielle : "
        "mesure et suivi de paramètres électriques à l’aide d’automates programmables (PLC)."
    )
with st.expander("Recharge dynamique de véhicules électriques"):
    st.write(
        "Étude d’un concept de recharge sans fil de véhicules électriques en mouvement, "
        "reposant sur le transfert d’énergie sans fil."
    )
with st.expander("Safe Pulse · Analyse stratégique et durabilité"):
    st.write(
        "Projet académique d’évaluation d’une entreprise fictive du secteur des technologies "
        "portables, utilisant notamment les analyses SWOT, PESTEL et les cinq forces de Porter."
    )
