
import streamlit as st
from pathlib import Path
from html import escape

BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "Assets"

profile_pic = ASSETS_DIR / "Kaviyarasu_Image.jpeg"
cv_file = ASSETS_DIR / "Francais.pdf"

def sous_titre(texte):
    st.markdown(
        f"""
        <h4 style="
            margin-top: 18px;
            margin-bottom: 8px;
            font-weight: 600;
        ">
            <u>{escape(texte)}</u>
        </h4>
        """,
        unsafe_allow_html=True
    )

name_col, empty_col = st.columns(
    [1.2, 2.8],
    gap="large"
)

with name_col:
    st.title("Kaviyarasu", anchor=False)

col1, col2 = st.columns(
    [1.2, 2.8],
    gap="large",
    vertical_alignment="top"
)

with col1:

    if profile_pic.exists():
        st.image(
            str(profile_pic),
            use_container_width=True
        )

with col2:

    st.subheader(
        "Doctorant-chercheur à l'ESTP",
        anchor=False
    )

    st.markdown(
        "**Génie industriel · Données géospatiales · "
        "Jumeaux numériques · Construction durable**"
    )

    st.caption("Orléans, France")

    
    st.markdown(
        "[LinkedIn](https://linkedin.com/in/kaviyarasu-sakthivel)"
        "  |  "
        "[GitHub](https://github.com/Charles-Lancier/My-Portfolio)"
    )


    btn_col1, btn_col2 = st.columns(
        [1, 1.5],
        gap="small"
    )

    with btn_col1:

        if st.button(
            "Me contacter",
            use_container_width=True
        ):
            st.switch_page("pages/Contact_me.py")

    with btn_col2:

        if cv_file.exists():

            with open(cv_file, "rb") as file:

                st.download_button(
                    label="Télécharger mon CV",
                    data=file.read(),
                    file_name="CV_Kaviyarasu.pdf",
                    mime="application/pdf",
                    type="primary",
                    icon=":material/download:",
                    use_container_width=True
                )

        else:

            st.button(
                "CV indisponible",
                disabled=True,
                use_container_width=True
            )

st.divider()

st.header("Profil professionnel", anchor=False)

st.write(
    """
    Doctorant-chercheur à l'ESTP et diplômé
    d'un master en génie industriel de Centrale Nantes.

    Mon parcours associe l'ingénierie électrique,
    l'automatisation industrielle, l'analyse
    de données et la recherche environnementale.

    Mes recherches actuelles portent sur
    les jumeaux numériques et l'intégration
    de données géospatiales pour l'évaluation
    des ressources minérales destinées
    à la construction et à la réhabilitation.
    """
)

st.header("Formation", anchor=False)

sous_titre("Doctorat — ESTP")

st.caption(
    "Octobre 2026 - Octobre 2029 (prévisionnel)"
)

st.write(
    "Recherche sur les jumeaux numériques "
    "et le bilan d'approvisionnement "
    "en ressources minérales."
)

sous_titre(
    "Master en génie industriel - Centrale Nantes"
)

st.caption("2024 - 2026 | Nantes, France")

st.write(
    "Ingénierie industrielle, systèmes "
    "intelligents, analyse de données et durabilité."
)

sous_titre(
    "Licence en génie électrique et électronique "
    "- KPR Institute of Engineering"
)

st.caption("2020 - 2024 | Inde")

st.write(
    "Systèmes électriques, électronique, "
    "automatisation et ingénierie."
)

st.header("Expériences professionnelles", anchor=False)

sous_titre("Stagiaire de recherche - ESTP")

st.caption("Mars - Août 2026 | Cachan, France")

st.markdown(
    """
    - Traitement et analyse de données climatiques
      issues notamment d'EXPLORE2, TRACC et DRIAS.
    - Développement de scripts Python et
      de tableaux de bord Excel.
    - Analyses statistiques, notamment ACP,
      et visualisation de données.
    - Étude de la fiabilité des données dans
      le contexte de la matérialité environnementale.
    """
)

sous_titre(
    "Stagiaire R&D - KONE Elevators and Escalators"
)

st.caption("Juillet 2023 - Mai 2024 | Chennai, Inde")

st.markdown(
    """
    - Programmation et configuration
      d'automates industriels Beckhoff.
    - Vérification et validation de composants.
    - Participation au dépannage et
      à l'analyse de systèmes automatisés.
    - Analyse de schémas et de processus industriels.
    """
)

sous_titre("Stagiaire en analyse - Sarmangal")

st.caption("Janvier - Juillet 2023 | Coimbatore, Inde")

st.markdown(
    """
    - Analyse des processus de production.
    - Suivi d'indicateurs de qualité et de performance.
    - Analyse de données industrielles.
    - Identification de possibilités
      d'amélioration des processus.
    """
)

st.header("Recherche et projets", anchor=False)

sous_titre(
    "BASTIR - Jumeau numérique pour "
    "l'approvisionnement en ressources minérales"
)

st.caption(
    "Recherche doctorale | Depuis octobre 2026"
)

st.write(
    """
    Étude de méthodes numériques et géospatiales
    pour l'analyse des ressources minérales issues
    des sols, des terres et des infrastructures.
    """
)

sous_titre(
    "Fiabilité des données climatiques "
    "et matérialité environnementale"
)

st.caption("Recherche appliquée | 2026")

st.write(
    """
    Analyse, traitement et visualisation
    de données climatiques dans le cadre
    des évaluations environnementales.
    """
)

if st.button("Voir tous mes projets"):
    st.switch_page("pages/Projects.py")

st.header("Compétences techniques", anchor=False)

col1, col2 = st.columns(2, gap="large")

with col1:

    st.markdown("**Programmation et données**")

    st.write(
        "Python, Pandas, NumPy, Matplotlib, "
        "Excel et analyse statistique."
    )

    st.markdown("**Géomatique**")

    st.write(
        "QGIS, données géospatiales, "
        "services WMS, WMTS et WFS."
    )

with col2:

    st.markdown("**Ingénierie industrielle**")

    st.write(
        "Automates Beckhoff, systèmes électriques, "
        "automatisation et analyse de production."
    )

    st.markdown("**Recherche et environnement**")

    st.write(
        "Données climatiques, analyse environnementale, "
        "recherche bibliographique et visualisation."
    )

st.header(
    "Compétences linguistiques",
    anchor=False
)

st.markdown(
    """
    - **Français :** C1 - Avancé
    - **Anglais :** C2 - Avancé
    - **Tamoul :** Langue maternelle
    """
)





