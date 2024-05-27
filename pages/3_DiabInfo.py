import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

im2=Image.open("images/logo_MonMedecin.jpg")
im1=Image.open("data/diabetes_image.jpg")
st.set_page_config(page_title="Mes Infos",page_icon=im2, layout="wide")

html_temp = """
<div style="background-color:#748c08;padding:1.5px">
<h1 style="color:white;text-align:center;">Vue Globale du Diabète 📃</h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)


st.title('C\'est quoi le Diabète?')
st.subheader('Dans cette Section:')
st.markdown(" 👉:blue[Quels sont les différents types de diabète ?]") 
st.markdown(" 👉:blue[A quel point le diabète est-il fréquent ?]") 
st.markdown(" 👉:blue[Qui est le plus susceptible de développer un diabète de type 2 ?]")
st.markdown(" 👉:blue[Quels sont les problèmes de santé que peuvent développer les personnes atteintes de diabète ?]") 
st.markdown(' ')
st.markdown('Le diabète est une maladie qui survient lorsque votre glycémie, également appelée taux de sucre dans le sang, est trop élevée. La glycémie est votre principale source d\'énergie et provient des aliments que vous consommez. **:blue[L\'insuline]**, une **:blue[hormone]** produite par le **:blue[pancréas]**, aide le glucose provenant des aliments à pénétrer dans vos cellules pour être utilisé comme source d\'énergie. Parfois, votre corps ne produit pas suffisamment d\'insuline, ou pas du tout, ou n\'utilise pas bien l\'insuline. Le glucose reste alors dans votre sang et n\'atteint pas vos cellules.')
st.markdown(' ')
st.markdown('Au fil du temps, avoir trop de glucose dans votre sang peut entraîner des problèmes de santé. Bien que le diabète n\'ait pas de cure, vous pouvez prendre des mesures pour gérer votre diabète et rester en bonne santé.')
st.markdown(' ')
st.markdown('Parfois, les gens appellent le diabète "un soupçon de sucre" ou "diabète limite". Ces termes suggèrent que quelqu\'un n\'a pas vraiment de diabète ou a une forme moins grave, mais chaque cas de diabète est sérieux.')

image = Image.open('./images/diabetes.png')

st.image(image, caption='En France, plus de 4 millions de personnes vivaient avec le diabète en 2021. La prévalence de cette maladie chronique ne cesse d\'augmenter, passant de 5,6 % en 2015 à 6,07 % en 2021. Cette forte augmentation du nombre de cas de diabète nous place face à une véritable épidémie. Aujourd\'hui, la prise en charge du diabète représente un véritable enjeu socio-économique et de santé publique. Au cœur de ces préoccupations, nos modes de vie, mais pas seulement ...')

st.title("Quels sont les différents types de diabète ?")
st.markdown(' ')
st.markdown('Les types de diabète les plus courants sont:')
st.markdown('-> Diabète de type 1')
st.markdown('-> Diabète de type 2')
st.markdown('-> Diabète gestationnel')

st.subheader('a) Diabète de type 1')
# st.markdown(' ')
st.markdown('Si vous êtes atteint de diabète de type 1, votre corps ne produit pas d\'insuline. Votre système immunitaire attaque et détruit les cellules du pancréas qui produisent l\'insuline. Le diabète de type 1 est généralement diagnostiqué chez les enfants et les jeunes adultes, bien qu\'il puisse apparaître à tout âge. Les personnes atteintes de diabète de type 1 doivent prendre de l\'insuline tous les jours pour rester en vie.')

st.subheader('b) Diabète de type 2')
# st.markdown(' ')
st.markdown('Si vous souffrez de diabète de type 2, votre corps ne produit pas ou n\'utilise pas bien l\'insuline. Le diabète de type 2 peut se développer à tout âge, même pendant l\'enfance. Toutefois, ce type de diabète survient le plus souvent chez les personnes d\'âge moyen ou plus âgées. Le type 2 est le type de diabète le plus courant.')

st.subheader('c) Diabète gestationnel')
# st.markdown(' ')
st.markdown('Le diabète gestationnel se développe chez certaines femmes enceintes. La plupart du temps, ce type de diabète disparaît après la naissance du bébé. Cependant, si vous avez souffert de diabète gestationnel, vous avez plus de chances de développer un diabète de type 2 plus tard dans votre vie. Parfois, le diabète diagnostiqué pendant la grossesse est en fait un diabète de type 2.')

st.subheader('c) les autres types de diabète')
st.markdown('Le diabète monogénique, qui est une forme héréditaire de diabète, et le diabète lié à la mucoviscidose sont des types de diabète moins courants.')
st.markdown(' ')

st.title('A quel point le diabète est-il fréquent?')
st.markdown('En France, plus de **:red[4 millions de personnes vivaient avec le diabète en 2021]**. La prévalence de cette maladie chronique est en constante augmentation, passant de 5,6 % en 2015 à 6,07 % en 2021. Cette forte augmentation du nombre de cas de diabète nous place face à une véritable épidémie. La prise en charge du diabète représente aujourd\'hui un véritable enjeu socio-économique et de santé publique.')


import altair as alt

# Get the data from the user



# uploaded_file = st.file_uploader("Choose a file")

# # Read the data into a pandas DataFrame
# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)

#     # Convert year column to datetime type
#     df['year'] = pd.to_datetime(df['year'], format='%Y')

#     # Create a line chart using Altair
#     chart = alt.Chart(df).mark_line().encode(
#         x=alt.X('year', axis=alt.Axis(title='Year')),
#         y=alt.Y('population_diabetes', axis=alt.Axis(title='Population Diabetes')),
#         tooltip=[alt.Tooltip('year', format='%Y'), alt.Tooltip('population_diabetes', format=',')]
#     ).properties(
#         width=700,
#         height=400
#     )

#     # Show the chart in Streamlit
#     st.altair_chart(chart, use_container_width=True)



df = pd.read_csv('./data/analysis.csv')

# Convert year column to datetime type
df['year'] = pd.to_datetime(df['year'], format='%Y')

# Create a line chart using Altair
chart = alt.Chart(df).mark_line().encode(
x=alt.X('year', axis=alt.Axis(title='Year')),
y=alt.Y('population_diabetes', axis=alt.Axis(title='Population Diabetes')),
tooltip=[alt.Tooltip('year', format='%Y'), alt.Tooltip('population_diabetes', format=',')]
).properties(
width=700,
height=400
)

# Show the chart in Streamlit
st.altair_chart(chart, use_container_width=True)
# st.markdown('<center>**:red[Rapport sur le Diabète en France 2000-2045]**</center>', unsafe_allow_html=True)
st.markdown("<center><span style='color:green'>Rapport sur le Diabète en France 2000-2045</span></center>", unsafe_allow_html=True)

st.markdown(' ')
st.title('Quelles sont les personnes les plus susceptibles de développer un diabète de type 2 ?')
st.markdown('Vous êtes plus susceptible de développer un diabète de type 2 si vous avez 45 ans ou plus, si vous avez des antécédents familiaux de diabète ou si vous êtes en surpoids. La sédentarité, la race et certains problèmes de santé tels que l\'hypertension artérielle influent également sur le risque de développer un diabète de type 2. Vous êtes également plus susceptible de développer un diabète de type 2 si vous avez un prédiabète ou si vous avez souffert d\'un diabète gestationnel pendant votre grossesse. En savoir plus sur les facteurs de risque du diabète de type 2.')



st.title('Quels sont les problèmes de santé que peuvent développer les personnes atteintes de Diabète?')
st.markdown('Au fil du temps, l\'hyperglycémie entraîne des problèmes tels que')
st.markdown('🔴 Maladie cardiaque')
st.markdown('🔴 Accident vasculaire cérébral')
st.markdown('🔴 Maladie du rein')
st.markdown('🔴 Problèmes oculaires')
st.markdown('🔴 Maladie dentaire')
st.markdown('🔴 Lésions nerveuses')
st.markdown('🔴 Problèmes de pieds')


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







