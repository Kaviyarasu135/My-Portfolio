import streamlit as st

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


# Original text translated into formal French

st.title("Projets", anchor=False)

st.markdown("<h3><u>Analyse stratégique et durabilité d’une entreprise (Safe Pulse) :</u></h3>", unsafe_allow_html=True)

st.write("**Aperçu :**")
st.write(
    """
    Ce projet portait sur l’analyse stratégique et durable d’une entreprise fictive (*Safe Pulse*), 
    un acteur potentiel du secteur des technologies portables. 
    L’objectif n’était pas de créer une entreprise, mais d’appliquer divers outils d’analyse 
    pour évaluer la viabilité, la compétitivité et l’intégration de la durabilité 
    dans un modèle d’affaires innovant.
    """
)

st.write("**Analyses réalisées :**")
st.write(
    """
    - Analyse externe & interne pour identifier l’environnement global et les ressources internes.
    - Porter’s Five Forces pour comprendre la pression concurrentielle et les barrières à l’entrée.
    - Analyse PESTEL pour évaluer les facteurs politiques, économiques, sociaux, technologiques, environnementaux et juridiques.
    - Analyse de la chaîne de valeur pour mettre en évidence les activités génératrices de valeur. 
    - Analyse SWOT pour résumer les forces, les faiblesses, les opportunités et les menaces.
    - Durabilité organisationnelle avec l’approche Sustainability 2.0 et 3.0 pour relier stratégie et ODD.
    """
)

st.write("**Compétences et apprentissages :**")
st.write(
    """
    - Application pratique des outils de management stratégique (SWOT, PESTEL, Porter, chaîne de valeur).  
    - Développement de compétences en analyse de durabilité et intégration des ODD de l’ONU dans une stratégie.  
    - Renforcement de l’esprit critique pour évaluer les avantages concurrentiels durables.  
    - Amélioration des compétences en travail d’équipe, recherche, et communication des résultats.  
    - Compréhension approfondie de la façon dont l’innovation et la durabilité s’articulent dans un modèle d’affaires.  
    """
)

st.write("**Résultats :**")
st.write(
    """
    - Acquisition d’une vision systémique reliant stratégie, durabilité et innovation.  
    - Capacité à évaluer la compétitivité d’une entreprise à l’aide d’outils structurés.  
    - Expérience académique valorisante pour les projets futurs en management durable et ingénierie industrielle.  
    """
)

st.markdown("<h3><u>Automatisation de la mesure de puissance à l’aide de PLC :</u></h3>", unsafe_allow_html=True)
st.write("**Aperçu :**")
st.write("Une mesure précise de la puissance est essentielle pour l’efficacité énergétique industrielle. Les relevés manuels sont chronophages et sujets aux erreurs. Ce projet introduit une mesure de puissance automatisée à l’aide d’automates programmables (PLC) pour permettre une surveillance en temps réel de la tension, du courant, de la consommation d’énergie et de l’efficacité du système. Le système améliore la gestion énergétique, détecte les anomalies et soutient la maintenance prédictive.")
st.write("**Objectifs :**")
st.write(
    """
    - Automatiser la mesure de puissance en temps réel avec des systèmes basés sur PLC.
    - Permettre une surveillance continue de la tension, du courant et du facteur de puissance.
    - Réduire les erreurs humaines et éliminer la collecte manuelle de données.
    - Mettre en œuvre des alertes automatisées pour les fluctuations et défaillances de puissance.
    - Améliorer l’efficacité énergétique grâce à des analyses basées sur les données.
    """
)
st.write("**Technologies utilisées :**")
st.write(
    """
    - Automates programmables (PLC) pour l’automatisation et la mesure de puissance.
    - Capteurs industriels pour un suivi précis des paramètres électriques.
    - IoT et analyses basées sur le cloud pour la surveillance à distance et la maintenance prédictive.
    """
)
st.write("**Caractéristiques principales :**")
st.write(
    """
    - Mesure continue sans intervention manuelle.
    - Notifications instantanées pour les conditions de puissance anormales.
    - Enregistrement de l’historique de la consommation d’énergie pour analyse.
    - Analyse de données pour la détection précoce des défaillances.
    """
)
st.write("**Résultats et impact :**")
st.write(
    """
    - Amélioration de l’efficacité opérationnelle en éliminant les erreurs de collecte manuelle des données.
    - Réduction du gaspillage énergétique en améliorant l’efficacité énergétique des opérations industrielles.
    - Renforcement de la maintenance prédictive, entraînant des économies de coûts et une optimisation des performances du système.
    - Identification des inefficacités et prévention des défaillances des équipements, réduisant ainsi les coûts.
    - Fourniture d’informations en temps réel pour une meilleure gestion énergétique, facilitant une prise de décision éclairée.
    """
)
st.markdown("<h3><u>Chargement dynamique des véhicules électriques :</u></h3>", unsafe_allow_html=True)
st.write("**Aperçu :**")
st.write("""Les véhicules électriques (VE) sont essentiels pour réduire les émissions de carbone, mais leur adoption est freinée par des temps de charge longs, l’anxiété liée à l’autonomie et les limitations des infrastructures. Ce projet vise à mettre en œuvre une charge sans fil dynamique, permettant aux VE de se recharger en mouvement grâce à une infrastructure routière intégrée. Utilisant une technologie avancée de transfert d’énergie sans fil (WPT), ce système améliore l’efficacité énergétique et le confort des utilisateurs.""")
st.write("**Objectifs :**")
st.write(
    """
    - Développer un système de transfert d’énergie sans fil pour la recharge des VE en mouvement.
    - Réduire la dépendance aux stations de recharge fixes et minimiser les temps d’arrêt.
    - Optimiser l’efficacité du transfert d’énergie grâce à la configuration des bobines.
    - Intégrer de manière fluide avec les infrastructures urbaines et autoroutières.
    - Promouvoir la durabilité en accélérant l’adoption des VE et en réduisant la dépendance aux combustibles fossiles.
    """
)
st.write("**Technologies utilisées :**")
st.write(
    """
    - Transfert d’énergie sans fil (WPT) pour la transmission d’énergie dynamique.
    - Électronique de puissance et systèmes embarqués pour la gestion de l’énergie en temps réel.
    - IoT, contrôle et surveillance en temps réel via des microcontrôleurs.
    """
)
st.write("**Résultats et impact :**")
st.write(
    """
    - Amélioration de l’autonomie des VE en réduisant la dépendance aux stations de recharge fixes.
    - Réduction des temps d’arrêt de recharge, améliorant l’efficacité globale et la durabilité.
    - Promotion d’un transport écologique en réduisant la dépendance aux combustibles fossiles.
    """
)
st.write("**Impact :**")
st.write(
    """
    - Réduction des arrêts de recharge pour une expérience de conduite fluide.
    - Atténuation de l’anxiété liée à l’autonomie et stimulation de l’adoption des VE.
    - Optimisation de l’infrastructure : réduction de la dépendance aux stations de recharge fixes.
    - Avantages environnementaux : réduction des émissions de gaz à effet de serre grâce à une utilisation accrue des VE.
    """
)

