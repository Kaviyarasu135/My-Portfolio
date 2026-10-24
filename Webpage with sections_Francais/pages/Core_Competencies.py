import streamlit as st
import pandas as pd

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
    st.subheader(
        "🤝 Collaboration et communication",
        anchor=False
    )
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
    st.subheader(
        "⚖️ Intégrité et persévérance",
        anchor=False
    )
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

st.html("""
<style>
.language-block {
    width: 100%;
    font-family: inherit;
}

.language-block h2 {
    font-size: 2rem;
    font-weight: 700;
    margin: 0 0 18px 0 !important;
    padding: 0;
}

.language-item {
    margin: 0 !important;
    padding: 0 !important;
}

.language-item h3 {
    font-size: 1.35rem;
    font-weight: 600;
    margin: 0 0 4px 0 !important;
    padding: 0 !important;
}

.language-level {
    color: #999;
    font-size: 0.9rem;
    margin: 0 0 5px 0 !important;
    padding: 0 !important;
}

.language-description {
    font-size: 1rem;
    line-height: 1.5;
    margin: 0 !important;
    padding: 0 !important;
}

.language-divider {
    display: block;
    width: 100%;
    height: 0;
    border: none;
    border-top: 1px solid rgba(128,128,128,0.4);
    margin: 10px 0 !important;
    padding: 0 !important;
}
</style>

<div class="language-block">

    <h2>Compétences linguistiques</h2>

    <div class="language-item">
        <h3>Français</h3>
        <p class="language-level">
            C1 - Avancé
        </p>
        <p class="language-description">
            Communication professionnelle, réunions
            et activités de recherche.
        </p>
    </div>

    <hr class="language-divider">

    <div class="language-item">
        <h3>Anglais</h3>
        <p class="language-level">
            C2 - Avancé
        </p>
        <p class="language-description">
            Communication scientifique, rédaction
            académique et échanges internationaux.
        </p>
    </div>

    <hr class="language-divider">

    <div class="language-item">
        <h3>Tamoul</h3>
        <p class="language-level">
            Langue maternelle
        </p>
        <p class="language-description">
            Maîtrise native.
        </p>
    </div>

</div>
""")



