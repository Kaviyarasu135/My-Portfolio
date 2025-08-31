import streamlit as st
import pandas as pd

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

st.title("Valeurs fondamentales", anchor=False)

st.write("**1) Honnêteté :**")
st.write(
    """
    - Valorise la vérité avant le confort, recherchant des retours authentiques.
    - Privilégie des relations honnêtes, même lorsque cela est difficile à entendre.
    """
)
st.write("**2) Engagement :**")
st.write(
    """
    - S’investit pleinement dans ses objectifs, surmontant les défis avec détermination.
    - Reste concentré et déterminé dans la poursuite de ses ambitions.
    """
)
st.write("**3) Discipline :**")
st.write(
    """
    - Croit en un effort constant et en la constance pour atteindre le succès.
    - Adhère à des routines, faisant confiance au processus même dans les moments difficiles.
    """
)
st.write("**4) Constance :**")
st.write(
    """
    - Se focalise sur le progrès à long terme plutôt que sur des résultats rapides.
    - Atteint ses objectifs grâce à des améliorations quotidiennes constantes.
    """
)


st.title("Maîtrise des langues")

languages = ["Français", "Anglais"]
proficiency = [55, 90]

for lang, level in zip(languages, proficiency):
    st.write(f"**{lang}**")
    st.progress(level / 100)

st.title("Temps consacré dans ma journée", anchor=False)

activities = [
    "Lecture de littérature professionnelle",
    "Apprentissage interdisciplinaire",
    "Lecture de science-fiction",
    "Amélioration de la maîtrise du français",
    "Moments de pause",
    "Développement personnel",
    "Perfectionnement en programmation Python",
    "Cyclisme",
    "Recherche d’un jeu vidéo à explorer"
]

time_spent = [2.4, 2.4, 2.4, 3.8, 1.68, 3.12, 2.4, 2.4, 2.4]

# Create a DataFrame for Streamlit's bar chart
df = pd.DataFrame({
    'Activités': activities,
    'Temps consacré (heures)': time_spent
})

# Display the bar chart using Streamlit's built-in function
st.bar_chart(df.set_index('Activités'))

st.write("Ce graphique visualise la répartition du temps alloué à chaque activité quotidienne.")
