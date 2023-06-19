import json
import pandas as pd
import urllib
import os

def get_csv(url, filename):
    try:
        # Vérifier si l'URL est disponible
        urllib.request.urlopen(url)
        # Si l'URL est disponible, charger le contenu du fichier Excel
        df = pd.read_csv(url, sep = ";")
    except:
        # Si l'URL n'est pas disponible, charger le contenu du fichier local
        df = pd.read_csv(filename, sep = ";")
    return df


# ---- PRIMAIRE ----
url_pri = "https://www.data.gouv.fr/fr/datasets/r/896c2e97-6a64-4521-bcab-b5b0d3cf7065"
filename_pri = "fr-en-ips-ecoles-ap2022.csv"

data_pri = get_csv(url=url_pri, filename=filename_pri)


data_pri["niveau"] = "Primaire"


# ---- COLLÈGES ----
url_coll = "https://www.data.gouv.fr/fr/datasets/r/28e511a7-af0d-48c7-a8bb-2f38ec003f49"
filename_coll = "fr-en-ips-colleges-ap2022.csv"

data_coll = get_csv(url=url_coll, filename=filename_coll)


data_coll["niveau"] = "Collège"

# ---- LYCÉES ----
url_lycee = "https://www.data.gouv.fr/fr/datasets/r/df2cbcb3-da0a-4265-a24e-c36f2c787db2"
filename_lycee = "fr-en-ips-lycees-ap2022.csv"

data_lycee = get_csv(url=url_lycee, filename=filename_lycee)


data_lycee["niveau"] = "Lycée"



# ---- GÉOLOC ----
url_geo = "https://www.data.gouv.fr/fr/datasets/r/b3b26ad1-a143-4651-afd6-dde3908196fc"
filename_geo = "fr-en-adresse-et-geolocalisation-etablissements-premier-et-second-degre.csv"

df_geo = get_csv(url=url_geo, filename=filename_geo)


coord = df_geo[["numero_uai", "latitude", "longitude"]]

# Fusion des DataFrames
df_complet = pd.concat([data_pri, data_coll, data_lycee])
merge_df = pd.merge(df_complet, coord, left_on='uai', right_on="numero_uai")

# Charger les données GeoJSON
current_dir = os.path.dirname(os.path.abspath(__file__))
geojson_path = os.path.join(current_dir, '..', 'data', 'departements.geojson')
with open(geojson_path) as f:
    dept = json.load(f)

# Prétraiter les codes de département
merge_df["departement"] = merge_df['code_du_departement'].map(lambda x: x[1:] if x.startswith('0') else x)

merge_df.loc[merge_df['type_de_lycee'] == 'LPO', 'ips'] = merge_df['ips_ensemble_gt_pro']
merge_df.loc[merge_df['type_de_lycee'] == 'LEGT', 'ips'] = merge_df['ips_voie_gt']
merge_df.loc[merge_df['type_de_lycee'] == 'LP', 'ips'] = merge_df['ips_voie_pro']

merge_df.loc[merge_df['type_de_lycee'] == 'LPO', 'effectifs'] = merge_df['effectifs_ensemble_gt_pro']
merge_df.loc[merge_df['type_de_lycee'] == 'LEGT', 'effectifs'] = merge_df['effectifs_voie_gt']
merge_df.loc[merge_df['type_de_lycee'] == 'LP', 'effectifs'] = merge_df['effectifs_voie_pro']

merge_df.loc[merge_df['type_de_lycee'] == 'LEGT', 'ecart_type_de_l_ips'] = merge_df['ecart_type_de_l_ips_voie_gt']
merge_df.loc[merge_df['type_de_lycee'] == 'LP', 'ecart_type_de_l_ips'] = merge_df['ecart_type_de_l_ips_voie_pro']

merge_df.drop(['ips_ensemble_gt_pro','ips_voie_gt','ips_voie_pro','effectifs_ensemble_gt_pro','effectifs_voie_gt','effectifs_voie_pro','ecart_type_de_l_ips_voie_gt','ecart_type_de_l_ips_voie_pro'], axis = 1)