

# Import necessary libraries
import pandas as pd
import streamlit as st
import plotly.express as px


html_temp = """
<div style="background-color:#440270;padding:1.5px">
<h1 style="color:white;text-align:center;"> Carte du monde des Spécialistes du diabète🌎 </h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)





st.subheader('Carte du monde des Spécialistes du diabète🌎')
data1=pd.read_csv("data/dataR.csv")
professions_diabete = ['Endocrinologue-diabétologue', 'Médecin spécialiste en médecine interne', 'Cardiologue',
                       'Gastro-entérologue et hépatologue', 'Ophtalmologiste', 'Néphrologue', 'Neurologue',
                       'Pédiatre', 'Chirurgien-dentiste spécialiste en médecine bucco-dentaire',
                       'Dermatologue et vénérologue','Médecin généraliste']
df_selected = data1

# Créer une boîte de sélection pour choisir une profession

selected_profession = st.selectbox("Choisissez une profession",professions_diabete )
# Filtrer les données en fonction de la profession sélectionnée
df_selected = df_selected[df_selected['Profession'] == selected_profession]

# Extraire les coordonnées de latitude et longitude à partir de la variable 'Coordonnées'
df_selected[['Latitude', 'Longitude']] = df_selected['Coordonnées'].apply(lambda x: pd.Series(x.split(','))).astype(float)

# Grouper les données par région pour obtenir le nombre de professionnels par région
df_grouped = df_selected.groupby('Nom Officiel Région').size().reset_index(name='Nombre de Professionnels')

# Fusionner les données groupées avec le DataFrame principal pour obtenir le nombre de professionnels par région
df_selected = df_selected.merge(df_grouped, on='Nom Officiel Région')

# Afficher les professionnels sur la carte avec le nombre de professionnels par région
fig = px.scatter_mapbox(df_selected, lat='Latitude', lon='Longitude', hover_name='Nom Officiel Région',
                        hover_data=['Nombre de Professionnels', 'Nom du professionnel', 'Profession', 'Adresse', 'Commune'],
                        color='Nombre de Professionnels', size='Nombre de Professionnels',
                        color_continuous_scale='Viridis',
                        zoom=5, width=800,height=600)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(geo=dict(showframe=False, showcoastlines=False, projection_type="equirectangular"))

# Afficher la carte
st.plotly_chart(fig)
st.markdown("<center><span style='color:green'>Statistiques des spécialistes du diabète</span></center>", unsafe_allow_html=True)

st.markdown(' ')
st.markdown("Prenez en compte de ces informations avant votre voyage. Vous pouvez rechercher des statistiques relatives aux spécialistes du diabète de votre destination !")



# Load the diabetes dataset
df = pd.read_csv("data/countrywise_data.csv")

# Create a Streamlit app
# st.title("Diabetes Map Chart of the world")

st.subheader('Estimation du diabète (20-79 ans)')

# Create a selectbox for the user to choose the year
year = st.selectbox("Select a Year", ["2000", "2011", "2021", "2030", "2045"])

# Create a choropleth map chart using Plotly Express
fig = px.choropleth(df, locations="Country/Territory", locationmode="country names",
                    color=year, hover_name="Country/Territory", range_color=[0, 20],
                    title=f"Prévalence du diabète par pays en {year}", width=800, height=600,template = "plotly_dark")
fig.update_layout(geo=dict(showframe=False, showcoastlines=False, projection_type="equirectangular"))

# Display the map chart in Streamlit
st.plotly_chart(fig)

st.markdown("<center><span style='color:green'>Rapport sur le diabète de tous les pays 2000-2045</span></center>", unsafe_allow_html=True)


st.markdown(' ')
st.markdown("Selon la Fédération internationale du diabète, on estime que 463 millions de personnes dans le monde étaient atteintes de diabète en 2019, soit 9,3 % de la population adulte mondiale. Ce chiffre devrait atteindre 700 millions d'ici 2045.")
st.markdown("La prévalence du diabète varie considérablement selon les régions, les taux les plus élevés étant observés dans les pays à revenu faible ou intermédiaire. En 2019, les pays où la prévalence du diabète est la plus élevée sont Tokelau (25,4 %), Nauru (24,3 %) et Maurice (22,8 %), tandis que les pays où la prévalence est la plus faible sont la Papouasie-Nouvelle-Guinée (2,8 %), la Tanzanie (2,9 %) et l'Éthiopie (3,1 %).")

hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)


st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")



st.markdown("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[Retourner sur la page d'accueil](https://voyag-int.rf.gd)\n\n\n\n")
st.markdown("\n\n\n\n\n[Kossi Robert MESSAN](https://www.linkedin.com/in/kossi-robert-messan-252954223/)")

