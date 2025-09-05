import streamlit as st
import requests
#from streamlit_lottie import st_lottie

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

st.title("Expériences", anchor=False)

st.markdown("<h3><u>Kone Elevators and Escalators (Stagiaire R&D) :</u></h3>", unsafe_allow_html=True)
st.write("**(Juillet 2023 - Mai 2024)**")
st.write("**1) Programmation PLC et automatisation :**")
st.write(
    """
    - Développement et optimisation de programmes PLC à l’aide d’automates Beckhoff, Configuration de modules d’entrée et de sortie pour améliorer les performances du système.
    - Réalisation du dépannage et le débogage des systèmes d’automatisation pour identifier et résoudre les problèmes matériels et logiciels.
    - Contribution à l’intégration de systèmes de contrôle en temps réel, Garantie une communication fluide entre différents composants industriels.
    """
)
st.write("**2) Vérification et validation des composants du système :**")
st.write(
    """
    - Réalisation des tests et une validation des composants du système pour garantir leur conformité aux normes industrielles et aux exigences de sécurité opérationnelle.
    - Contribution à effectuer des tests fonctionnels, des analyses d’erreurs et du débogage pour améliorer la fiabilité du système.
    - Collaboration avec des équipes pluridisciplinaires pour l’affinement des spécifications de conception et vérifier le respect des critères de qualité et de performance.
    """
)
st.write("**3) Durabilité et efficacité énergétique :**")
st.write(
    """
    - Contribution à des pratiques industrielles durables Par l’analyse des processus à travers le prisme du triple bilan : impact économique, environnemental et social.
    - Assistance à l’identification de solutions d’automatisation rentables Visant à améliorer l’efficacité opérationnelle tout en minimisant le gaspillage de ressources.
    - Soutien à la recherche sur des matériaux écologiques et des stratégies de réduction des déchets pour aligner la production sur les objectifs de durabilité environnementale.
    - Participation à des discussions sur la sécurité des travailleurs, l’ergonomie et l’automatisation éthique pour garantir que la technologie améliore les conditions de travail.
    """
)
st.write("**4) Gestion de la production et optimisation des flux de travail :**")
st.write(
    """
    - Acquisition d'une expérience pratique en gestion de la production, se concentrant sur la planification des ressources, l’ordonnancement et l’optimisation des processus.
    - Contribution à l’analyse des goulots d’étranglement dans les flux de production et Proposition d'améliorations pour accroître l’efficacité.
    - Collaboration avec des équipes pluridisciplinaires pour assurer une intégration fluide des solutions d’automatisation dans les lignes de production existantes.
    """
)
st.write("**5) Diagrammes industriels et conception de systèmes :**")
st.write(
    """
    - Création et interprétation des diagrammes industriels, y compris des schémas électriques, des organigrammes et des plans de systèmes de contrôle.
    - Assistance à la conception et la documentation des systèmes d’automatisation, Garantie d'une représentation précise des composants électriques et mécaniques.
    - Collaboration étroite avec des ingénieurs et des concepteurs Pour l’analyse et l’affinement des diagrammes industriels, améliorant la clarté et l’efficacité des systèmes.
    """
)
st.markdown("<h3><u>Sarmangal (Stagiaire en analyse) :</u></h3>", unsafe_allow_html=True)
st.write("**(Janvier 2023 - Juillet 2023)**")
st.write("**1) Gestion de la production et optimisation des flux de travail :**")
st.write(
    """
    - Analyse et rationalisation des flux de production, avec identification des inefficacités et recommandation d’améliorations basées sur les données afin d’augmenter la productivité.
    - Contribution à la mise en œuvre de mesures de contrôle de la qualité, afin de garantir des normes de production cohérentes et conformes aux réglementations industrielles.
    - Exploration de stratégies pour intégrer des pratiques de production durables, en équilibrant les impacts économiques, environnementaux et sociaux dans les opérations industrielles.
    """
)
st.write("**2) Durabilité et efficacité des ressources :**")
st.write(
    """
    - Évaluation des processus de production selon une perspective de durabilité, afin de garantir une utilisation optimale des ressources, la réduction des déchets et des pratiques de fabrication éthiques.
    - Réalisation d’une analyse des flux de matériaux pour suivre la consommation des ressources et identifier des opportunités d’optimisation et d’efficacité des coûts.
    - Exploré des stratégies pour intégrer des pratiques de production durables, équilibrant les impacts économiques, environnementaux et sociaux dans les opérations industrielles.
    """
)
st.write("**3) Diagrammes industriels et visualisation des processus :**")
st.write(
    """
    - Création et interprétation de diagrammes de flux de processus, de diagrammes industriels et de graphiques de contrôle de la qualité, pour visualiser les étapes de production et les interactions entre systèmes.
    - Utilisation de techniques de schématisation pour représenter les opérations de fabrication, favorisant une meilleure prise de décision et des améliorations des processus.
    - Soutien à la recherche sur des matériaux écologiques et des stratégies de réduction des déchets pour aligner la production sur les objectifs de durabilité environnementale.
    - Application de connaissances en planification de la production et en documentation, afin de garantir la traçabilité, la standardisation et une efficacité accrue des flux de travail.
    """
)
st.write("**4) Contrôle et assurance de la qualité :**")
st.write(
    """
    - Contribution à l’analyse des défauts et des incohérences, avec garantie du respect des critères de qualité et des normes réglementaires.
    - Collaboration avec des superviseurs pour améliorer les processus d’inspection, réduire les erreurs et accroître la fiabilité globale des produits.
    - Aide au développement de procédures standardisées pour le suivi de la qualité, en assurant une cohérence entre les différents lots de production.
    """
)
st.write("**5) Analyse des données et suivi des performances :**")
st.write(
    """
    - Collecte et analyse de données de production pour identifier des tendances, des schémas et des domaines d’amélioration continue.
    - Contribution à la mesure des indicateurs clés de performance (KPI) liés à l’efficacité, aux taux de défauts et à l’utilisation des ressources.
    - Fourniture de recommandations exploitables basées sur l’analyse des données, en soutien à des initiatives d’amélioration continue.
    """
)
st.write("**6) Collaboration technique et documentation :**")
st.write(
    """
    - Collaboration étroite avec des équipes pluridisciplinaires (production, assurance qualité, durabilité) pour aligner les stratégies et les objectifs.
    - Documentation des résultats, des améliorations de processus et des normes de qualité, assurant une communication claire et un transfert de connaissances efficace.
    - Participation à des discussions sur l’automatisation, la durabilité et la gestion de la production, en contribuant à une approche holistique de l’efficacité industrielle.
    """
)




