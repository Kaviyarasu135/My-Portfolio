import streamlit as st

import plotly.graph_objects as go
import pandas as pd

try:
    import plotly.graph_objects as go
    st.write("Plotly is installed and loaded successfully!")
except ModuleNotFoundError:
    st.error("Plotly is NOT installed properly.")

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

#st.title("Objectif de vie", anchor=False)

#st.write("La véritable croissance ne vient pas seulement de s’améliorer soi-même, mais aussi d’élever les autres au fur et à mesure de son progrès. Les moments les plus gratifiants surviennent souvent en aidant les autres à atteindre leurs objectifs, créant ainsi un sentiment partagé de croissance et de finalité. Chaque petit acte de soutien peut déclencher le parcours de quelqu’un d’autre, et en retour, enrichir notre propre chemin.")

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
    "Developpment personnel",
    "Perfectionnement en programmation Python",
    "Cyclisme",
    "Recherche d’un jeu vidéo à explorer"
]

time_spent = [2.4, 2.4, 2.4, 3.8, 1.68, 3.12, 2.4, 2.4, 2.4]

color_mapping = {
    "Lecture de littérature professionnelle": "#FFDDC1",
    "Apprentissage interdisciplinaire": "#FFABAB",
    "Lecture de science-fiction": "#FFD6A5",
    "Amélioration de la maîtrise du français": "#FFC3A0",
    "Moments de pause": "#E0BBE4",
    "Developpment personnel": "#D5AAFF",
    "Perfectionnement en programmation Python": "#85E3FF",
    "Cyclisme": "#B9FBC0",
    "Recherche d’un jeu vidéo à explorer": "#A0CED9"
}


# Bar chart
#st.title("Nouveau graphique")
#st.subheader("Temps consacré aux activités quotidiennes (Graphique en barres)")
fig_bar = go.Figure(
    data=[go.Bar(
        x=activities,
        y=time_spent,
        marker=dict(color=[color_mapping[a] for a in activities]),
        hoverinfo="none"
    )]
)

fig_bar.update_layout(
    title="Temps consacré aux activités quotidiennes (Graphique en barres)",
    xaxis_title="Activités",
    yaxis_title="Temps consacré (heures)",
    showlegend=False,
    font=dict(size=14),
    hovermode=False
)


st.plotly_chart(fig_bar, use_container_width=True, config={"displayModeBar": False}, key="bar_chart")





