from pathlib import Path
import streamlit as st

st.title("Contact & CV")
st.write("Vous souhaitez échanger sur un sujet de recherche, un projet ou une collaboration ?")
st.markdown(
    "[LinkedIn](https://linkedin.com/in/kaviyarasu-sakthivel) · "
    "[GitHub](https://github.com/Kaviyarasu135)"
)
st.caption("Orléans, France")

st.divider()
st.subheader("CV")
st.warning(
    "Les PDF actuellement disponibles dans le dépôt sont d’anciennes versions. "
    "Leur remplacement par des CV à jour en français et en anglais reste à valider."
)
st.write("Un CV actualisé sera ajouté ici après vérification des informations et des coordonnées publiques.")

st.divider()
st.subheader("Envoyer un message")
st.write("Le formulaire de contact existant est conservé, avec son service d’envoi actuel.")
st.markdown("""
<form action="https://formsubmit.co/bdd6b1c863e3ab54935da1039d5473e7" method="POST">
  <input type="hidden" name="_captcha" value="false">
  <label>Votre nom<br><input name="name" type="text" required style="width:100%;padding:9px;margin:6px 0 14px 0"></label><br>
  <label>Votre adresse e-mail<br><input name="email" type="email" required style="width:100%;padding:9px;margin:6px 0 14px 0"></label><br>
  <label>Votre message<br><textarea name="message" required rows="5" style="width:100%;padding:9px;margin:6px 0 14px 0"></textarea></label><br>
  <button type="submit" style="padding:10px 20px;border:0;border-radius:8px;cursor:pointer">Envoyer</button>
</form>
""", unsafe_allow_html=True)
