
import streamlit as st

# ==========================================
# COMPÉTENCES TECHNIQUES
# ==========================================

st.title("Compétences techniques", anchor=False)

st.write(
    """
    Mon parcours en génie industriel et en recherche
    appliquée m'a permis de développer des compétences
    en programmation, analyse de données, automatisation
    et évaluation environnementale.

    Mes travaux doctoraux me conduisent également
    à approfondir les méthodes géospatiales et
    les approches de jumeaux numériques.
    """
)

st.divider()

# ==========================================
# COMPÉTENCES PRINCIPALES
# ==========================================

col1, col2 = st.columns(2, gap="large")

with col1:

    st.subheader(
        "Programmation et analyse de données",
        anchor=False
    )

    st.markdown(
        """
        - **Python :** traitement, structuration
          et analyse de données.
        - **Pandas et NumPy :** manipulation
          et traitement de jeux de données.
        - **Matplotlib :** visualisation de données
          et création de graphiques.
        - **Excel :** analyse de données
          et création de tableaux de bord.
        - **Analyse statistique :** analyse
          exploratoire et analyse en composantes
          principales (ACP).
        """
    )

    st.subheader(
        "Géomatique et SIG",
        anchor=False
    )

    st.markdown(
        """
        - **QGIS :** visualisation, manipulation
          et exploration de données géospatiales.
        - **Services OGC :** utilisation
          de services WMS, WMTS et WFS.
        - **Données géographiques :** exploration
          de ressources IGN et BRGM.
        - **Analyse spatiale :** systèmes de
          coordonnées, reprojection et
          premières opérations spatiales.
        """
    )

with col2:

    st.subheader(
        "Analyse environnementale et recherche",
        anchor=False
    )

    st.markdown(
        """
        - **Données climatiques :** traitement
          et analyse de données issues notamment
          d'EXPLORE2, TRACC et DRIAS.
        - **Fiabilité des données :** contrôle,
          comparaison et interprétation
          de données environnementales.
        - **Matérialité environnementale :**
          travaux liés aux cadres ESRS et EFRAG.
        - **Recherche scientifique :** recherche
          bibliographique et synthèse documentaire.
        """
    )

    st.subheader(
        "Automatisation et ingénierie industrielle",
        anchor=False
    )

    st.markdown(
        """
        - **Automates programmables :**
          programmation et configuration
          de systèmes PLC Beckhoff.
        - **Systèmes industriels :** vérification,
          validation et dépannage de composants.
        - **Production :** analyse et optimisation
          des processus industriels.
        - **Qualité :** suivi des performances
          et identification des inefficacités.
        """
    )

# ==========================================
# OUTILS SCIENTIFIQUES ET NUMÉRIQUES
# ==========================================

st.divider()

st.subheader(
    "Outils scientifiques et numériques",
    anchor=False
)

st.markdown(
    """
    - **Streamlit :** développement d'applications
      interactives et de visualisations.
    - **Zotero :** organisation et gestion
      de références bibliographiques.
    - **LaTeX :** préparation et mise en forme
      de documents scientifiques.
    """
)

# ==========================================
# DOMAINES EN COURS D'APPROFONDISSEMENT
# ==========================================

st.subheader(
    "Domaines en cours d'approfondissement",
    anchor=False
)

st.markdown(
    """
    - Jumeaux numériques appliqués
      à l'environnement bâti.
    - Analyse géospatiale des ressources
      minérales et des infrastructures.
    - Intégration et exploitation de données
      hétérogènes pour la recherche.
    """
)
