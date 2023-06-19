import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

import streamlit as st
import plotly_express as px
from data.data import merge_df


st.set_page_config(page_title = "Analyse",
                   page_icon = "🔎",
                   layout = "wide"
)
st.title("Analyse")

# ---- SIDEBAR ----
st.sidebar.header("Filtres")

# Sélection des académies
academie = st.sidebar.multiselect(
    "Académie :",
    options=merge_df["academie"].unique(),
)

# Filtrer les départements en fonction des académies sélectionnées
departements_disponibles = merge_df.loc[merge_df["academie"].isin(academie), "departement"].unique()

# Sélection des départements
departement = st.sidebar.multiselect(
    "Département :",
    options=departements_disponibles,
)

# Filtrer les communes en fonction des académies et départements sélectionnés
communes_disponibles = merge_df.loc[(merge_df["academie"].isin(academie)) & (merge_df["departement"].isin(departement)), "nom_de_la_commune"].unique()

# Sélection des communes
commune = st.sidebar.multiselect(
    "Commune :",
    options=communes_disponibles,
)

# Sélection des années scolaires
annee_scolaire = st.sidebar.multiselect(
    "Année scolaire :",
    options=merge_df["rentree_scolaire"].unique(),
)

# Sélection du niveau
niveau = st.sidebar.multiselect(
    "Niveau :",
    options=merge_df["niveau"].unique(),
)

# ---- MAIN ----

st.subheader("Tableau complet")
st.dataframe(merge_df)

# Appliquer les filtres
st.subheader("Sélectionnez des filtres pour afficher votre sélection.")
filtered_df = merge_df.loc[(merge_df["academie"].isin(academie)) & (merge_df["departement"].isin(departement)) & (merge_df["nom_de_la_commune"].isin(commune)) & (merge_df["rentree_scolaire"].isin(annee_scolaire)) & (merge_df["niveau"].isin(niveau))].set_index('numero_uai')

# Afficher le dataframe filtré
st.dataframe(filtered_df)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(px.pie(merge_df, names='secteur', title='Répartition des écoles par secteur', template="plotly_dark"))
    st.markdown("""Ce graphique montre la répartition des écoles par secteur. Chaque secteur est représenté par une part de secteur colorée. Lorsque vous survolez une part de secteur, vous verrez les informations supplémentaires telles que le secteur, les effectifs et l'IPS de l'établissement associé.""")

with col2:
    st.plotly_chart(px.scatter(merge_df.sample(n=1000, random_state=42), x='ips', y='effectifs', title= "Échantillon de 1000 points comparant l'ips à l'effectif", hover_data={'nom_de_l_etablissment': True, 'secteur': True, 'effectifs': True, 'ips': True}))
    st.markdown("""Ce graphique montre un échantillon de 1000 points qui compare l'IPS (indicateur de performance scolaire) à l'effectif des établissements scolaires. Chaque point représente un établissement, et sa position sur l'axe des x est déterminée par l'IPS, tandis que sa position sur l'axe des y est déterminée par l'effectif. Lorsque vous survolez un point, vous verrez des informations détaillées telles que le nom de l'établissement, le secteur, les effectifs et l'IPS associés.""")

st.plotly_chart(px.bar(merge_df.groupby('academie').size().reset_index(name='count'), x= 'academie', y='count', title='Nombre d\'établissements scolaires par académie'))
st.markdown("""Ce graphique montre le nombre d'établissements scolaires par académie. Chaque barre représente une académie et sa hauteur est proportionnelle au nombre d'établissements dans cette académie.""")