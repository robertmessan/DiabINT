

# Import necessary libraries
import pandas as pd
import streamlit as st
import plotly.express as px


html_temp = """
<div style="background-color:#440270;padding:1.5px">
<h1 style="color:white;text-align:center;">Diabetes specialists Map chart of the world🌎 </h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)





st.subheader('Diabetes specialists Map chart of the world🌎')
data1=pd.read_csv("data/dataR.csv")
professions_diabete = ['Endocrinologue-diabétologue', 'Médecin spécialiste en médecine interne', 'Cardiologue',
                       'Gastro-entérologue et hépatologue', 'Ophtalmologiste', 'Néphrologue', 'Neurologue',
                       'Pédiatre', 'Chirurgien-dentiste spécialiste en médecine bucco-dentaire',
                       'Dermatologue et vénérologue','Médecin généraliste']
df_selected = data1

# Créer une boîte de sélection pour choisir une profession

selected_profession = st.selectbox("Choisissez une profession",professions_diabete )

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
st.markdown("<center><span style='color:green'>Diabetes specialists statistics</span></center>", unsafe_allow_html=True)

st.markdown(' ')
st.markdown('Take this information into consideration before your travel. You can search for statistics related to diabetes specialists of your destination!')



# Load the diabetes dataset
df = pd.read_csv("data/countrywise_data.csv")

# Create a Streamlit app
# st.title("Diabetes Map Chart of the world")

st.subheader('Diabetes estimates (20-79 y)')

# Create a selectbox for the user to choose the year
year = st.selectbox("Select a Year", ["2000", "2011", "2021", "2030", "2045"])

# Create a choropleth map chart using Plotly Express
fig = px.choropleth(df, locations="Country/Territory", locationmode="country names",
                    color=year, hover_name="Country/Territory", range_color=[0, 20],
                    title=f"Diabetes Prevalence by Country in {year}", width=800, height=600,template = "plotly_dark")
fig.update_layout(geo=dict(showframe=False, showcoastlines=False, projection_type="equirectangular"))

# Display the map chart in Streamlit
st.plotly_chart(fig)

st.markdown("<center><span style='color:green'>Diabetes report of all the countries 2000-2045</span></center>", unsafe_allow_html=True)


st.markdown(' ')
st.markdown('According to the International Diabetes Federation, an estimated 463 million people worldwide had diabetes in 2019, representing 9.3% of the global adult population. This figure is expected to rise to 700 million by 2045.')
st.markdown('The prevalence of diabetes varies widely by region, with the highest rates found in low- and middle-income countries. In 2019, the countries with the highest prevalence of diabetes were Tokelau (25.4%), Nauru (24.3%), and Mauritius (22.8%), while the countries with the lowest prevalence were Papua New Guinea (2.8%), Tanzania (2.9%), and Ethiopia (3.1%).')

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

