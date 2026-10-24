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

# st.title("Valeurs fondamentales", anchor=False)

# st.write("**1) Honnêteté :**")
# st.write(
#     """
#     - Valoriser la vérité avant le confort, rechercher des retours authentiques.
#     - Privilégier des relations honnêtes, même lorsque cela est difficile à entendre.
#     """
# )
# st.write("**2) Engagement :**")
# st.write(
#     """
#     - S’investir pleinement dans ses objectifs, surmonter les défis avec détermination.
#     - Rester concentré et déterminé dans la poursuite de ses ambitions.
#     """
# )
# st.write("**3) Discipline :**")
# st.write(
#     """
#     - Croire en un effort constant et en la constance pour atteindre le succès.
#     - Adhérer à des routines, faire confiance au processus même dans les moments difficiles.
#     """
# )
# st.write("**4) Constance :**")
# st.write(
#     """
#     - Se focaliser sur le progrès à long terme plutôt que sur des résultats rapides.
#     - Atteindre ses objectifs grâce à des améliorations quotidiennes constantes.
#     """
# )


# st.title("Maîtrise des langues")

# languages = ["Français", "Anglais"]
# proficiency = [75, 90]

# for lang, level in zip(languages, proficiency):
#     st.write(f"**{lang}**")
#     st.progress(level / 100)

# st.title("Temps consacré dans ma journée", anchor=False)

# activities = [
#     "Lecture de littérature professionnelle",
#     "Apprentissage interdisciplinaire",
#     "Lecture de science-fiction",
#     "Amélioration de la maîtrise du français",
#     "Moments de pause",
#     "Développement personnel",
#     "Perfectionnement en programmation Python",
#     "Cyclisme",
#     "Recherche d’un jeu vidéo à explorer"
# ]

# time_spent = [2.4, 2.4, 2.4, 3.8, 1.68, 3.12, 2.4, 2.4, 2.4]

# # Create a DataFrame for Streamlit's bar chart
# df = pd.DataFrame({
#     'Activités': activities,
#     'Temps consacré ': time_spent
# })

# # Display the bar chart using Streamlit's built-in function
# st.bar_chart(df.set_index('Activités'))



# ==========================================
# COMPÉTENCES PERSONNELLES
# ==========================================

st.title("Compétences personnelles", anchor=False)

st.write(
    """
    Au-delà des compétences techniques, mon parcours
    repose sur une approche rigoureuse du travail,
    une curiosité intellectuelle et une volonté
    constante d'apprendre et de progresser.
    """
)
st.divider()

st.header("Savoir-être et méthodes de travail", anchor=False)

col1, col2 = st.columns(2, gap="large")

with col1:

    st.subheader("🎯 Rigueur et organisation", anchor=False)

    st.write(
        """
        - Adopter une approche méthodique dans
          l'analyse et la résolution de problèmes.
        - Organiser les tâches selon les priorités
          et les objectifs à atteindre.
        - Accorder une importance particulière
          à la précision et à la qualité du travail.
        """
    )

    st.subheader("🧠 Curiosité et apprentissage", anchor=False)

    st.write(
        """
        - Explorer de nouvelles technologies,
          méthodes et disciplines.
        - Développer continuellement mes
          connaissances et compétences.
        - Relier les connaissances de différents
          domaines pour aborder les problèmes
          sous plusieurs perspectives.
        """
    )

with col2:

    st.subheader("🤝 Collaboration et communication", anchor=False)

    st.write(
        """
        - Échanger des idées et des connaissances
          dans des équipes pluridisciplinaires.
        - Communiquer les informations techniques
          de manière claire et structurée.
        - Valoriser l'écoute, les retours
          constructifs et la coopération.
        """
    )

    st.subheader("⚖️ Intégrité et persévérance", anchor=False)

    st.write(
        """
        - Privilégier l'honnêteté intellectuelle
          et la transparence.
        - Maintenir mon engagement face
          aux difficultés et aux défis.
        - Considérer les erreurs comme des
          occasions d'apprentissage et
          d'amélioration continue.
        """
    )

st.divider()

# ==========================================
# LANGUES
# ==========================================

st.header("Compétences linguistiques", anchor=False)

st.markdown("#### Français")
st.caption("C1 - Niveau avancé")
st.write(
    "Communication professionnelle, réunions "
    "et activités de recherche."
)

st.divider()

st.markdown("#### Anglais")
st.caption("C2 - Maîtrise")
st.write(
    "Communication scientifique, rédaction académique "
    "et échanges internationaux."
)

st.divider()

st.markdown("#### Tamoul")
st.caption("Langue maternelle")
st.write("Maîtrise native.")




