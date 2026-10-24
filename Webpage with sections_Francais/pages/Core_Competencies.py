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
st.markdown(
    """
    <div style="line-height: 1.5;">

        <h3 style="margin: 0;">Français</h3>
        <p style="color: gray; margin: 4px 0;">
            C1 - Niveau avancé
        </p>
        <p style="margin: 6px 0;">
            Communication professionnelle, réunions
            et activités de recherche.
        </p>

        <hr style="margin: 10px 0;
                   border: none;
                   border-top: 1px solid #555;">

        <h3 style="margin: 0;">Anglais</h3>
        <p style="color: gray; margin: 4px 0;">
            C2 - Maîtrise
        </p>
        <p style="margin: 6px 0;">
            Communication scientifique, rédaction
            académique et échanges internationaux.
        </p>

        <hr style="margin: 10px 0;
                   border: none;
                   border-top: 1px solid #555;">

        <h3 style="margin: 0;">Tamoul</h3>
        <p style="color: gray; margin: 4px 0;">
            Langue maternelle
        </p>
        <p style="margin: 6px 0;">
            Maîtrise native.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


