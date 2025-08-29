import streamlit as st
import requests
from streamlit_lottie import st_lottie

def load_lottieur1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def load_lottieur2(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def load_lottieur3(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def load_lottieur4(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def load_lottieur5(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def load_lottieur6(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding_1_2 = load_lottieur1("https://lottie.host/287599d5-c2e8-4783-9d61-9926f0722d9b/SUfRVr1swG.json")
lottie_coding_3_4 = load_lottieur2("https://lottie.host/61ec1171-395f-4954-9297-b6c33e0a3d85/0AekzDD9CB.json")
lottie_coding_5_6 = load_lottieur3("https://lottie.host/a307861e-e8d1-482a-b1c6-9c3a7f6536c0/tEeOF8ngMa.json")
lottie_coding_7_8 = load_lottieur4("https://lottie.host/ec143494-3359-4239-9e02-d44c3ff5833d/BM9grZHnfm.json")
lottie_coding_9_10 = load_lottieur5("https://lottie.host/ca30c8ad-a569-42bb-9fd8-59e9e4b227c0/uTNhv3jh9m.json")
lottie_coding_11_12 = load_lottieur6("https://lottie.host/37954394-c814-4019-9fc4-f146d378f240/Dji5WmWaab.json")

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

st.title("Compétences", anchor=False)
st.markdown("<h3><u>Compétences personnelles :</u></h3>", unsafe_allow_html=True)

st.write("**1) Discipliné et engagé :**")
st.write(
            """
            - Maintient une approche cohérente et structurée pour atteindre ses objectifs, garantissant un progrès constant même dans des situations difficiles.
            - Se concentre sur les solutions plutôt que sur les obstacles, restant dédié à l’amélioration continue.
            - Privilégie la qualité et la précision, valorisant une exécution rigoureuse plutôt que des raccourcis.
            """
        )
st.write("**2) Orienté vers les objectifs :**")
st.write(
            """
            - Définit des objectifs clairs et suit un plan structuré pour les accomplir efficacement.
            - Décompose les défis complexes en étapes gérables, garantissant un progrès constant.
            - Aligne les objectifs sur un impact à long terme, équilibrant ambition et pragmatisme.
            """
        )
st.write("**3) Apprenant adaptable :**")
st.write(
            """
            - Assimile rapidement de nouveaux concepts et technologies, appliquant ses connaissances efficacement dans différents domaines.
            - Considère les défis comme des opportunités de croissance, faisant preuve de flexibilité dans l’apprentissage.
            - Relie les connaissances de divers domaines, améliorant la résolution de problèmes et la pensée stratégique.
            """
        )
st.write("**4) Honnête et transparent :**")
st.write(
            """
            - Valorise une communication claire et directe, garantissant confiance et responsabilité dans les interactions professionnelles.
            - Reconnaît ses forces et ses axes d’amélioration, favorisant un développement continu.
            - Encourage les retours honnêtes et une prise de décision pragmatique pour améliorer l’efficacité.
            """
        )

st.write("**5) Conscient de soi et stratégique :**")
st.write(
            """
            - Évalue les décisions en se concentrant sur les résultats à long terme et l’impact durable.
            - Équilibre ambition et définition réaliste d’objectifs, garantissant une gestion efficace des ressources.
            - Aborde les défis avec un esprit stratégique, s’adaptant aux situations évolutives tout en maintenant une clarté d’objectif.
            """
        )
st.write("**6) Résilient et persévérant :**")
st.write(
            """
            - Reste concentré sur les objectifs à long terme, persévérant face aux revers ou aux défis.
            - Considère les obstacles comme des opportunités d’apprentissage et d’amélioration plutôt que des raisons d’abandon.
            - Maintient une approche disciplinée, adaptant les stratégies si nécessaire sans perdre de vue l’objectif final.
            """
        )

st.markdown("<h3><u>Compétences techniques :</u></h3>", unsafe_allow_html=True)
st.write("**1) Programmation PLC :**")
st.write(
            """
            - A acquis une expérience pratique avec les automates Beckhoff, configurant les systèmes d’entrée et de sortie pour optimiser l’automatisation industrielle.
            - Apprécie le dépannage et le débogage des programmes PLC, garantissant un fonctionnement fluide et efficace des systèmes.
            - Pense de manière systématique lors de la programmation, garantissant une logique claire, évolutive et alignée sur les exigences de production.
            """
        )
st.write("**2) Systèmes industriels :**")
st.write(
            """
            - Comprend la nature interconnectée de l’automatisation, de la production et de l’optimisation des systèmes, garantissant des opérations fluides.
            - Pense en termes de systèmes et de processus, appliquant des compétences analytiques pour améliorer l’efficacité et la fiabilité.
            - Familier avec les diagrammes industriels, la validation des systèmes et l’optimisation des flux de travail, garantissant une documentation et une mise en œuvre claires.
            """
        )
st.write("**3) Python :**")
st.write(
            """
            - Considère Python comme un outil puissant pour l’automatisation, l’analyse de données et l’optimisation des systèmes, l’appliquant à des tâches liées à l’industrie et à la durabilité.
            - S’adapte rapidement aux nouveaux défis de programmation, tirant parti de la flexibilité de Python pour résoudre des problèmes dans l’automatisation industrielle et les flux de production.
            - Utilise une approche structurée et analytique pour coder, garantissant des solutions efficaces, évolutives et bien documentées.
            """
        )
st.write("**4) Durabilité :**")
st.write(
            """
            - Aborde la durabilité avec un esprit pratique, se concentrant sur les aspects économiques, environnementaux et sociaux des systèmes industriels.
            - Intéressé par la réduction des déchets, l’optimisation de l’utilisation des ressources et l’intégration de pratiques durables dans la production et l’automatisation.
            - Considère la durabilité comme une stratégie à long terme, garantissant l’efficacité tout en tenant compte de l’impact global des processus industriels.
            """
        )
st.write("**5) Gestion de la production :**")
st.write(
            """
            - Se concentre sur l’efficacité, l’organisation et l’amélioration continue, garantissant des flux de travail fluides et optimisés.
            - Analyse les goulots d’étranglement dans la production et propose des améliorations stratégiques pour accroître la productivité.
            - Comprend l’équilibre entre l’automatisation, la gestion des ressources et les facteurs humains dans les environnements de production.
            """
        )
st.write("**6) Gestion de projets :**")
st.write(
            """
            - Applique naturellement une pensée orientée vers les objectifs et structurée aux projets, garantissant clarté et concentration du début à la fin.
            - Planifie et exécute les tâches de manière méthodique, équilibrant efficacité et adaptabilité dans la résolution de problèmes.
            - Valorise une communication claire, des délais réalistes et une collaboration efficace, garantissant que les projets se déroulent sans heurts et atteignent leurs objectifs.
            """
        )