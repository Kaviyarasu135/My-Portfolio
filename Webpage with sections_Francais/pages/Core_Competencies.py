import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
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



