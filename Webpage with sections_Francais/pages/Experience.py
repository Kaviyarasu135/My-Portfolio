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
    - Développé et optimisé des programmes PLC à l’aide d’automates Beckhoff, configurant des modules d’entrée et de sortie pour améliorer les performances du système.
    - Effectué le dépannage et le débogage des systèmes d’automatisation pour identifier et résoudre les problèmes matériels et logiciels.
    - Contribué à l’intégration de systèmes de contrôle en temps réel, garantissant une communication fluide entre différents composants industriels.
    """
)
st.write("**2) Vérification et validation des composants du système :**")
st.write(
    """
    - Réalisé des tests et une validation des composants du système pour garantir leur conformité aux normes industrielles et aux exigences de sécurité opérationnelle.
    - Contribué à effectuer des tests fonctionnels, des analyses d’erreurs et du débogage pour améliorer la fiabilité du système.
    - Collaboré avec des équipes pluridisciplinaires pour affiner les spécifications de conception et vérifier le respect des critères de qualité et de performance.
    """
)
st.write("**3) Durabilité et efficacité énergétique :**")
st.write(
    """
    - Contribué à des pratiques industrielles durables en analysant les processus à travers le prisme du triple bilan : impact économique, environnemental et social.
    - Assisté dans l’identification de solutions d’automatisation rentables qui amélioraient l’efficacité opérationnelle tout en minimisant le gaspillage de ressources.
    - Soutenu la recherche sur des matériaux écologiques et des stratégies de réduction des déchets pour aligner la production sur les objectifs de durabilité environnementale.
    - Participé à des discussions sur la sécurité des travailleurs, l’ergonomie et l’automatisation éthique pour garantir que la technologie améliore les conditions de travail.
    """
)
st.write("**4) Gestion de la production et optimisation des flux de travail :**")
st.write(
    """
    - Acquis une expérience pratique en gestion de la production, se concentrant sur la planification des ressources, l’ordonnancement et l’optimisation des processus.
    - Contribué à l’analyse des goulots d’étranglement dans les flux de production et proposé des améliorations pour accroître l’efficacité.
    - Collaboré avec des équipes pluridisciplinaires pour garantir une intégration fluide des solutions d’automatisation dans les lignes de production existantes.
    """
)
st.write("**5) Diagrammes industriels et conception de systèmes :**")
st.write(
    """
    - Créé et interprété des diagrammes industriels, y compris des schémas électriques, des organigrammes et des plans de systèmes de contrôle.
    - Assisté dans la conception et la documentation des systèmes d’automatisation, garantissant une représentation précise des composants électriques et mécaniques.
    - Collaboré étroitement avec des ingénieurs et des concepteurs pour analyser et affiner les diagrammes industriels, améliorant la clarté et l’efficacité des systèmes.
    """
)
st.markdown("<h3><u>Sarmangal (Stagiaire en analyse) :</u></h3>", unsafe_allow_html=True)
st.write("**(Janvier 2023 - Juillet 2023)**")
st.write("**1) Gestion de la production et optimisation des flux de travail :**")
st.write(
    """
    - Analysé et rationalisé les flux de production, identifiant les inefficacités et recommandant des améliorations basées sur les données pour augmenter la productivité.
    - Contribué à la mise en œuvre de mesures de contrôle de la qualité, garantissant des normes de production cohérentes et conformes aux réglementations industrielles.
    - Collaboré avec différentes équipes pour optimiser les plannings de production, minimiser les temps d’arrêt et améliorer l’efficacité de la fabrication.
    """
)
st.write("**2) Durabilité et efficacité des ressources :**")
st.write(
    """
    - Évalué les processus de production à travers une perspective de durabilité, garantissant une utilisation optimale des ressources, la réduction des déchets et des pratiques de fabrication éthiques.
    - Réalisé une analyse des flux de matériaux pour suivre la consommation des ressources, identifiant des domaines pour l’optimisation et l’efficacité des coûts.
    - Exploré des stratégies pour intégrer des pratiques de production durables, équilibrant les impacts économiques, environnementaux et sociaux dans les opérations industrielles.
    """
)
st.write("**3) Diagrammes industriels et visualisation des processus :**")
st.write(
    """
    - Créé et interprété des diagrammes de flux de processus, des diagrammes industriels et des graphiques de contrôle de la qualité pour visualiser les étapes de production et les interactions des systèmes.
    - Utilisé des techniques de diagrammes pour représenter les opérations de fabrication, favorisant une meilleure prise de décision et des améliorations des processus.
    - Soutenu la recherche sur des matériaux écologiques et des stratégies de réduction des déchets pour aligner la production sur les objectifs de durabilité environnementale.
    - Appliqué des connaissances en planification de la production et en documentation, garantissant une traçabilité, une standardisation et une efficacité des flux de travail améliorées.
    """
)
st.write("**4) Contrôle et assurance de la qualité :**")
st.write(
    """
    - Contribué à l’analyse des défauts et des incohérences, garantissant que la production respectait les critères de qualité et les normes réglementaires.
    - Collaboré avec des superviseurs pour améliorer les processus d’inspection, réduisant les erreurs et augmentant la fiabilité globale des produits.
    - Aidé à développer des procédures standardisées pour le suivi de la qualité, garantissant une cohérence entre différents lots de production.
    """
)
st.write("**5) Analyse des données et suivi des performances :**")
st.write(
    """
    - Collecté et analysé des données de production, utilisant des informations pour identifier des tendances, des schémas et des domaines d’amélioration.
    - Contribué à la mesure des indicateurs clés de performance (KPI) liés à l’efficacité, aux taux de défauts et à l’utilisation des ressources.
    - Fourni des recommandations exploitables basées sur l’analyse des données pour soutenir des initiatives d’amélioration continue.
    """
)
st.write("**6) Collaboration technique et documentation :**")
st.write(
    """
    - Collaboré étroitement avec des équipes pluridisciplinaires, y compris les divisions de production, d’assurance qualité et de durabilité, pour aligner les stratégies.
    - Documenté les résultats, les améliorations des processus et les normes de qualité, garantissant une communication claire et un transfert de connaissances.
    - Participé à des discussions sur l’automatisation, la durabilité et la gestion de la production, contribuant à une approche holistique de l’efficacité industrielle.
    """
)


