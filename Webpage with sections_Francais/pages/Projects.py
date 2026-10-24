
import streamlit as st

st.title("Projets et travaux de recherche", anchor=False)

st.write(
    """
    Mon parcours associe recherche appliquée, analyse
    de données, ingénierie industrielle et durabilité.

    Les projets présentés ci-dessous illustrent
    l'évolution de mes travaux, de l'automatisation
    industrielle vers l'analyse environnementale
    et les approches numériques pour la construction.
    """
)

st.divider()
st.header(
    "BASTIR - Jumeau numérique et ressources minérales",
    anchor=False
)
st.caption(
    "Recherche doctorale | ESTP | Octobre 2026 – En cours"
)
st.markdown("**Présentation du projet**")
st.write(
    """
    Ma recherche doctorale porte sur le développement
    d'une approche de jumeau numérique pour le bilan
    d'approvisionnement en ressources minérales issues
    des sols, des terres et des infrastructures,
    destinées à la construction et à la réhabilitation.

    Elle s'inscrit dans une réflexion sur la gestion
    des ressources, la valorisation des matériaux
    existants et l'intégration de données territoriales.
    """
)
st.markdown("**Objectifs de recherche**")
st.markdown(
    """
    - Étudier les méthodes existantes d'évaluation
      des ressources minérales pour la construction.
    - Explorer les données disponibles sur les
      bâtiments, les carrières et les ressources
      géologiques.
    - Examiner les relations spatiales entre
      infrastructures, territoires et ressources.
    - Étudier l'intégration de données hétérogènes
      dans une approche de jumeau numérique.
    - Contribuer à une meilleure compréhension
      des ressources potentiellement mobilisables
      pour la construction et la réhabilitation.
    """
)
st.markdown("**Travaux en cours**")
st.markdown(
    """
    - Revue bibliographique sur les jumeaux
      numériques, l'urban mining et la gestion
      des matériaux de construction.
    - Exploration de sources de données
      géographiques institutionnelles,
      notamment IGN et BRGM.
    - Prise en main de QGIS et des services
      géographiques WMS, WMTS et WFS.
    - Étude préliminaire de méthodes d'analyse
      et de représentation spatiale des ressources.
    """
)
st.caption(
    "Domaines : Jumeaux numériques · SIG · "
    "Données géospatiales · Ressources minérales"
)
st.info(
    "Projet de recherche en cours : les objectifs "
    "présentés ne constituent pas des résultats "
    "scientifiques déjà obtenus."
)
st.divider()

st.header(
    "Fiabilité des données climatiques et matérialité",
    anchor=False
)
st.caption(
    "Stage de recherche | ESTP, Cachan | Mars – Août 2026"
)
st.markdown("**Présentation du projet**")
st.write(
    """
    Ce projet de recherche appliquée portait sur
    l'analyse de la fiabilité des données climatiques
    et leur utilisation dans le contexte des
    évaluations de matérialité environnementale,
    notamment en lien avec les cadres ESRS et EFRAG.

    L'objectif était d'examiner l'exploitation
    de données climatiques et de développer
    des méthodes permettant de faciliter
    leur traitement, leur comparaison
    et leur interprétation.
    """
)
st.markdown("**Travaux réalisés**")
st.markdown(
    """
    - Exploration et traitement de jeux de données
      climatiques, notamment EXPLORE2 et TRACC(DRIAS).
    - Développement de scripts Python pour
      organiser et analyser les données.
    - Réalisation d'analyses statistiques,
      dont l'analyse en composantes principales (ACP).
    - Étude d'indicateurs climatiques,
      notamment les nuits tropicales.
    - Création de visualisations et de tableaux
      de bord pour faciliter l'interprétation
      des informations.
    - Analyse de la cohérence et de la fiabilité
      des données utilisées dans les évaluations
      environnementales.
    """
)
st.markdown("**Livrables**")

st.write(
    """
    Développement d'outils de traitement,
    de visualisations et de supports d'analyse,
    accompagnés d'un rapport de recherche
    présentant les méthodes et les résultats.
    """
)

st.caption(
    "Outils et méthodes : Python · Excel · "
    "Analyse statistique · ACP · Données climatiques"
)

st.divider()

st.header("Projets d'ingénierie antérieurs", anchor=False)

st.write(
    """
    Ces projets réalisés au cours de ma formation
    m'ont permis d'explorer différents domaines,
    notamment l'automatisation, les systèmes
    électriques et la stratégie industrielle.
    """
)
with st.expander(
    "Automatisation de la mesure de puissance avec PLC"
):
    st.markdown("**Présentation**")

    st.write(
        """
        Projet portant sur l'automatisation
        de la mesure et du suivi de paramètres
        électriques à l'aide d'automates
        programmables industriels (PLC).
        """
    )

    st.markdown("**Objectifs étudiés**")

    st.markdown(
        """
        - Automatiser la mesure de paramètres
          électriques tels que la tension,
          le courant et la puissance.
        - Explorer les possibilités de suivi
          et d'acquisition de données.
        - Réduire les interventions manuelles
          dans les opérations de mesure.
        - Étudier l'utilisation des données
          collectées pour l'analyse énergétique.
        """
    )
    st.caption(
        "Domaines : Automatisation · PLC · "
        "Instrumentation · Systèmes électriques"
    )
with st.expander(
    "Recharge dynamique des véhicules électriques"
):
    st.markdown("**Présentation**")

    st.write(
        """
        Projet consacré à l'étude d'un système
        de recharge sans fil permettant
        théoriquement l'alimentation de véhicules
        électriques pendant leur déplacement.

        L'approche repose sur le transfert
        d'énergie sans fil (WPT) et son
        intégration potentielle aux
        infrastructures routières.
        """
    )
    st.markdown("**Objectifs étudiés**")

    st.markdown(
        """
        - Examiner le principe de transfert
          d'énergie sans fil.
        - Étudier les contraintes techniques
          associées à la recharge dynamique.
        - Explorer les configurations possibles
          des systèmes de transfert énergétique.
        - Analyser le potentiel de cette
          technologie pour la mobilité électrique.
        """
    )
    st.caption(
        "Domaines : Électronique de puissance · "
        "WPT · Mobilité électrique"
    )

with st.expander(
    "Safe Pulse - Analyse stratégique et durabilité"
):

    st.markdown("**Présentation**")

    st.write(
        """
        Projet académique consacré à l'analyse
        stratégique d'une entreprise fictive
        spécialisée dans les technologies portables.

        L'objectif était d'étudier la viabilité
        d'un modèle d'affaires en mobilisant
        des outils de management stratégique
        et d'analyse de durabilité.
        """
    )

    st.markdown("**Analyses réalisées**")

    st.markdown(
        """
        - Analyse SWOT pour identifier les
          forces, faiblesses, opportunités
          et menaces.
        - Analyse PESTEL de l'environnement
          externe de l'entreprise.
        - Modèle des cinq forces de Porter
          pour étudier la concurrence.
        - Analyse de la chaîne de valeur.
        - Étude des enjeux de durabilité
          et de leur intégration
          à la stratégie de l'entreprise.
        """
    )

    st.caption(
        "Domaines : Stratégie · Management · "
        "Durabilité · Analyse organisationnelle"
    )


