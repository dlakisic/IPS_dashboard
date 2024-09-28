import sys
import os

parent_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(parent_dir, ".."))
sys.path.append(parent_dir)

import streamlit as st
from data.data import merge_df, dept

st.set_page_config(page_title="Accueil",
                   page_icon="🎓",
                   layout="wide"
                   )

st.title("Accueil")

# ---- CONTACT ----

current_dir = os.getcwd()
image_path = os.path.join(current_dir, "Dino_carré.png")
image_url = "https://media.licdn.com/dms/image/C4D03AQHhaTl4QT42ug/profile-displayphoto-shrink_400_400/0/1612262833161?e=1692835200&v=beta&t=3CktyzxF6FdYgKXtb7QrEB4B2ojs0N2ty1OLwMOksWU"

st.sidebar.markdown(
    """
    <style>
    .sidebar-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    .sidebar-image {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        object-fit: cover;
        margin: 20px 0;
    }
    .sidebar-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .sidebar-subtitle {
        font-size: 18px;
        margin-bottom: 20px;
    }
    .contact-button {
        background-color: #1D2951;
        border: none;
        color: white;
        padding: 8px 16px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border-radius: 8px;
        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.25);
        margin-top: 10px;
    }
    .contact-section img {
        margin-top: 10px;
        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.25);
    }
    </style>
    <div class="sidebar-content">
        <div class="sidebar-title">Dino LAKISIC</div>
        <img class="sidebar-image" src="https://media.licdn.com/dms/image/v2/C4D03AQHhaTl4QT42ug/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1612262834996?e=1730332800&v=beta&t=wpDPvARUrfMvugXlP2YwLeACf06ZqD66ygasjj-RFm4">
        <div class="sidebar-subtitle">Data Manager</div>
        <div class="contact-section">
            <div style="font-size: 18px; font-weight: bold;">Contacts</div>
            <div>
                <a href="https://www.linkedin.com/in/dino-lakisic/">
                    <img src="https://img.shields.io/badge/Dino%20LAKISIC-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/dino-lakisic/">
                </a>
            </div>
            <div>
                <a href="https://github.com/dlakisic">
                    <img src="https://img.shields.io/badge/Dino%20LAKISIC-100000?style=for-the-badge&logo=github&logoColor=white&link=https://github.com/dlakisic">
                </a>
            </div>
            <div>
                <a href="mailto:dino.lakisic@efrei.net">
                    <button class="contact-button">Contactez-moi par e-mail</button>
                </a>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)





st.title("Description")

st.markdown("""📚 Le projet "Analyse de l'Indice de Position Sociale des Écoles Françaises" est une application Streamlit conçue pour offrir des informations et des insights approfondis sur l'indice de position sociale des écoles en France. L'indice de position sociale est une mesure qui permet de comprendre la composition sociale de l'environnement des écoles.

Notre application se base sur des données fiables et récentes provenant de différentes sources, telles que le Ministère de l'Éducation nationale français, l'Insee et d'autres organismes compétents. En utilisant ces données, nous calculons un indice de position sociale pour chaque école, ce qui permet de classer les établissements en fonction de la composition socio-économique de leurs élèves.

💡 L'objectif principal de cette application est de fournir aux parents, aux chercheurs et aux décideurs politiques un outil facile à utiliser pour explorer les disparités socio-économiques entre les écoles françaises. Les utilisateurs pourront visualiser des statistiques clés telles que la répartition des élèves selon différentes catégories socio-économiques, les écarts de performances académiques entre les écoles et les indicateurs de réussite scolaire en fonction du milieu social.

🔍 Caractéristiques principales de l'application :

- 📊 Tableau de bord interactif : Les utilisateurs pourront sélectionner des critères spécifiques tels que la région, le département ou la commune pour afficher les données correspondantes.

- 📈 Visualisations graphiques : Des graphiques intuitifs et informatifs seront générés pour présenter les résultats de manière claire et compréhensible. Les utilisateurs pourront explorer les distributions socio-économiques et les performances scolaires en utilisant des graphiques tels que des diagrammes en barres, des camemberts et des diagrammes en boîte.

- 🎯 Comparaisons et filtres : Les utilisateurs pourront comparer plusieurs écoles entre elles et appliquer des filtres pour affiner leurs recherches, par exemple en sélectionnant une plage de valeurs spécifique pour l'indice de position sociale.

- ℹ️ Informations supplémentaires : Des informations contextuelles sur la méthodologie utilisée pour calculer l'indice de position sociale seront fournies, ainsi que des définitions clés pour faciliter la compréhension des résultats.

Nous espérons que cette application aidera à sensibiliser davantage à l'importance de l'indice de position sociale dans l'éducation en France et à susciter des discussions constructives sur les inégalités socio-économiques et les mesures potentielles pour les atténuer.

Veuillez noter que toutes les données utilisées dans cette application seront anonymisées et respecteront les règles de confidentialité en vigueur. La transparence et l'intégrité des données sont des priorités essentielles pour nous.

🚀 N'hésitez pas à explorer l'application "Analyse de l'Indice de Position Sociale des Écoles Françaises" et à partager vos commentaires pour nous aider à améliorer continuellement cette plateforme. Nous croyons en l'importance d'une éducation équitable pour tous les enfants et nous nous efforçons de contribuer à cet objectif à travers cette initiative.
""")

st.subheader("Statistiques descriptives")
st.dataframe(merge_df.describe())