import streamlit as st
from streamlit_lottie import st_lottie
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import requests


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


# Donut chart
#st.subheader("Temps consacré aux activités quotidiennes (Graphique en anneau)")
fig_donut = go.Figure(
    data=[go.Pie(
        labels=activities,
        values=time_spent,
        hole=0.3,
        textinfo="percent+label",
        textposition="inside",  # Adjusted to avoid overlap
        marker=dict(colors=[color_mapping[a] for a in activities],
                    line=dict(color='#000000', width=1)),
        hoverinfo="none"
    )]
)

fig_donut.update_layout(
    showlegend=True,  # Enable legend for clarity
    title="Temps consacré aux activités quotidiennes",
    font=dict(size=12),  # Smaller font to reduce clutter
    margin=dict(t=50, b=50, l=50, r=50),
)

st.plotly_chart(fig_donut, use_container_width=True, config={"displayModeBar": False}, key="donut_chart")