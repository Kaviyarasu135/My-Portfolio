from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url):
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

lottie_coding = load_lottieurl("https://lottie.host/eca8ed12-aeeb-4985-8f5f-a771d4e8c66e/OxQl13pWPU.json")
lottie_Master = load_lottieur2("https://lottie.host/b432d721-58a8-47b1-9cd7-88f9ee336801/GqqplW3NG5.json")
lottie_Bachelor = load_lottieur3("https://lottie.host/26c18ef8-8936-4611-abcd-99d1722004e1/pRUZDGYZHe.json")

# Original text translated into formal French
st.header("Mes activités", anchor=False)
st.write(
            """
            Je suis un ingénieur industriel spécialisé dans l’optimisation durable des entreprises grâce à l’utilisation de logiciels avancés, y compris Python. Je me concentre sur l’analyse basée sur les données, l’optimisation des processus et la modélisation des flux d’entreprise pour améliorer l’efficacité et faciliter une transition harmonieuse vers la durabilité.
            - Optimisation des flux de production et d’entreprise.
            - Création de visualisations claires pour améliorer les opérations commerciales.
            - Accompagnement des entreprises vers des pratiques écologiques et résilientes.
            - Utilisation de la technologie pour améliorer les performances opérationnelles.
            - Développement et entraînement de modèles pour une prise de décision plus intelligente à l’aide de Python.
            """
        )
st.subheader("Master", anchor=False)
st.write(
            """
            Je suis étudiant en Master d’ingénierie industrielle, spécialisé dans les entreprises intelligentes et connectées. Je me concentre sur l’optimisation des opérations commerciales en intégrant des systèmes intelligents, garantissant efficacité, durabilité et innovation. Je travaille avec aisance aussi bien de manière autonome qu’en équipe, dirigeant des équipes et des projets avec une approche orientée vers les résultats.
            - Alignement des technologies avec les besoins commerciaux pour une croissance durable.
            - Amélioration des opérations grâce à des systèmes intelligents basés sur les données.
            - Compétence à travailler de manière autonome et en équipe.
            - Direction d’équipes pour atteindre efficacement les objectifs industriels.
            - Application d’une pensée analytique pour améliorer les performances des entreprises.
            """
        )

st.subheader("Licence", anchor=False)
st.write(
            """
            Je suis titulaire d’une licence en ingénierie électrique et électronique, avec une solide expertise dans la conception, l’analyse et l’optimisation des systèmes électriques. J’aime relever des défis techniques complexes, que ce soit en travaillant seul ou en équipe. Doté d’un esprit stratégique et d’une expérience en leadership, je veille à ce que les projets soient menés efficacement tout en favorisant l’innovation dans les systèmes électriques et électroniques.
            - Expertise dans la conception, l’optimisation et l’amélioration des performances des circuits.
            - Expérience dans la direction d’équipes pour obtenir des résultats à fort impact.
            - Approche analytique rigoureuse pour diagnostiquer et améliorer l’efficacité des systèmes.
            - Orientation vers la connexion entre la technologie et les applications électriques du monde réel.
            """
        )