
import streamlit as st

st.title("À propos de moi", anchor=False)

st.write(
    """
    Je suis doctorant-chercheur à l'ESTP à Orléans
    et diplômé d'un master en génie industriel
    de Centrale Nantes.

    Mon parcours académique et professionnel
    m'a conduit de l'ingénierie électrique et electronique
    et de l'automatisation industrielle vers
    l'analyse de données, la recherche
    environnementale et les approches numériques
    appliquées à la construction durable.

    Mes travaux actuels s'intéressent à
    l'utilisation des jumeaux numériques et
    des données géospatiales pour mieux
    comprendre et évaluer les ressources
    minérales destinées à la construction
    et à la réhabilitation.
    """
)

st.divider()

st.header("Parcours académique", anchor=False)

st.subheader(
    "Doctorat - ESTP",
    anchor=False
)

st.caption(
    "Depuis octobre 2026 | Orléans, France"
)

st.write(
    """
    Je poursuis actuellement un doctorat
    consacré au développement d'une approche
    de jumeau numérique pour le bilan
    d'approvisionnement en ressources minérales
    issues des sols, des terres et des
    infrastructures pour la construction
    et la réhabilitation.

    Cette recherche mobilise des connaissances
    en ingénierie, en gestion des ressources,
    en systèmes d'information géographique
    et en intégration de données.

    Elle vise à explorer des méthodes
    permettant de mieux caractériser les
    ressources disponibles et de contribuer
    à une gestion plus durable des matériaux
    de construction.
    """
)
st.subheader(
    "Master en génie industriel - Centrale Nantes",
    anchor=False
)

st.caption(
    "2024 - 2026 | Nantes, France"
)

st.write(
    """
    J'ai obtenu mon master en génie industriel
    à Centrale Nantes où j'ai approfondi
    mes connaissances en systèmes industriels,
    analyse de données, optimisation des
    processus et durabilité.

    Cette formation m'a permis de développer
    une approche transversale des problématiques
    d'ingénierie, en reliant les dimensions
    techniques, organisationnelles
    et environnementales.

    Mon stage de fin d'études à l'ESTP 
    consacré à la fiabilité des données
    climatiques a renforcé mon intérêt
    pour la recherche appliquée.
    """
)

st.subheader(
    "Licence en génie électrique et électronique",
    anchor=False
)

st.caption(
    "KPR Institute of Engineering | "
    "2020 - 2024 | Inde"
)

st.write(
    """
    Ma formation initiale en génie électrique
    et électronique m'a apporté des bases
    techniques en systèmes électriques,
    électronique, automatisation et
    analyse de systèmes.

    Elle m'a également permis de développer
    une compréhension des systèmes industriels
    et de leurs applications pratiques,
    notamment dans le domaine
    de l'automatisation.
    """
)

st.divider()

st.header(
    "Centres d'intérêt scientifiques",
    anchor=False
)

col1, col2 = st.columns(2, gap="large")

with col1:

    st.markdown("**Jumeaux numériques**")
    st.write(
        "Exploration des approches numériques "
        "pour représenter, analyser et "
        "mieux comprendre les systèmes physiques."
    )

    st.markdown("**Données et géomatique**")
    st.write(
        "Traitement et analyse de données, "
        "systèmes d'information géographique "
        "et représentation spatiale."
    )

with col2:

    st.markdown("**Construction durable**")
    st.write(
        "Gestion des ressources minérales, "
        "matériaux de construction et "
        "valorisation des ressources existantes."
    )

    st.markdown("**Ingénierie et environnement**")
    st.write(
        "Analyse environnementale, "
        "fiabilité des données et "
        "développement de méthodes "
        "d'aide à la décision."
    )

st.divider()

st.header("Mon approche", anchor=False)

st.write(
    """
    J'aborde les problématiques d'ingénierie
    et de recherche avec une démarche
    analytique, structurée et ouverte
    à différentes disciplines.

    Je m'intéresse particulièrement
    aux situations dans lesquelles
    les outils numériques et l'exploitation
    de données peuvent contribuer
    à mieux comprendre des systèmes complexes.

    Mon objectif est de développer
    progressivement des compétences
    complémentaires en recherche,
    en ingénierie et en sciences des données,
    tout en conservant une attention
    particulière à leurs applications
    concrètes et à leurs implications
    environnementales.
    """
)


