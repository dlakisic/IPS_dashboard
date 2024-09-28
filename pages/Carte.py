import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

import streamlit as st
import plotly.graph_objects as go
import plotly_express as px
from data.data import merge_df, dept

st.set_page_config(page_title="Carte de l'IPS", page_icon="🗺️", layout="wide")
st.title("🗺️ Carte de l'IPS")

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

# Description des données
st.markdown("""
    Cette carte interactive vous permet d'explorer l'Indice de Position Sociale (IPS) moyen par département en France
    ainsi que la répartition des établissements scolaires sur le territoire.
    
    L'IPS est un indicateur qui mesure le niveau socio-économique moyen des élèves d'un établissement scolaire.
    Il est calculé à partir de différents critères tels que le niveau d'éducation des parents, le revenu familial, etc.
    Plus l'IPS est élevé, plus le niveau socio-économique moyen des élèves est élevé.
""")


# Création de la carte choroplèthe
fig = px.choropleth_mapbox(
    merge_df.groupby("departement").mean(numeric_only=True).reset_index(),
    geojson=dept,
    locations='departement',
    color='ips',
    color_continuous_scale="jet",
    range_color=(85, 125),
    mapbox_style="carto-positron",
    featureidkey="properties.code",
    zoom=4.5,
    center={"lat": 47.081012, "lon": 2.398782},
    opacity=0.5
)

# Mise en page de la carte
fig.update_layout(
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    height=600,
    width=900
)

# Ajout des points scatter_mapbox
scatter_fig = px.scatter_mapbox(
    merge_df,
    lat="latitude",
    lon="longitude",
    hover_name="nom_de_l_etablissment",
    hover_data=["nom_de_la_commune", "secteur", "niveau", "effectifs", "ips", "ecart_type_de_l_ips"],
    zoom=4.5,
    color="ips",
    color_continuous_scale="jet"
)

scatter_fig.update_traces(
    hovertemplate="<b>%{hovertext}</b><br>📍 Commune : %{customdata[0]}<br>🔹 Secteur : %{customdata[1]}<br>🏫 Niveau : %{customdata[2]}<br>👥 Effectifs : %{customdata[3]}<br>🔢 IPS : %{customdata[4]}<br>σ IPS : %{customdata[5]}"
)

# Mise en page des points scatter_mapbox
scatter_fig.update_layout(
    mapbox_style="carto-positron",
    mapbox_zoom=4.5,
    mapbox_center={"lat": 47.081012, "lon": 2.398782},
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    height=600,
    width=900
)

# Ajout des points scatter_mapbox à la carte choroplèthe
for data in scatter_fig.data:
    fig.add_trace(data)

# Affichage de la carte
st.plotly_chart(fig, use_container_width=True)

# Description des résultats
st.markdown("""
    👉 Vous pouvez explorer la carte en utilisant les outils de zoom et de déplacement.
    Survolez les points pour obtenir des informations détaillées sur chaque établissement scolaire.
    
    La carte choroplèthe représente l'IPS moyen par département en utilisant une échelle de couleurs.
    Plus la couleur d'un département tend vers le rouge, plus l'IPS moyen y est élevé.
    
    Les points scatter_mapbox représentent les établissements scolaires.
    Leur couleur est basée sur leur IPS respectif.
    
    Utilisez les filtres sur le côté pour affiner les résultats en fonction de l'académie, du département,
    de la commune, de l'année scolaire et du niveau d'éducation.
""")

# Affichage du dataframe
st.subheader("📊 Données des établissements scolaires")
st.dataframe(merge_df)

# Affichage du footer
st.markdown("""
    🌐 Source des données : [Open Data Éducation](https://data.education.gouv.fr/)
    💡 Des questions ? [Contactez-nous](mailto:dino.lakisic@efrei.net)
""")

