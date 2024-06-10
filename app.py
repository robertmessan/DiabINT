import streamlit as st
import pickle
import pandas as pd
from PIL import Image
import numpy as np
import datetime as dt
import altair as alt

im2=Image.open("images/logo_MonMedecin.jpg")
im1=Image.open("data/diabetes_image.jpg")
st.set_page_config(page_title="DiabINT_SudParis",page_icon=im2, layout="wide")
@st.cache_data#(allow_output_mutation=True)
def load(scaler_path, model_path):
    with open(scaler_path, "rb") as scaler:
        sc = pickle.load(scaler)
    with open(model_path, "rb") as model:
        model = pickle.load(model)
    return sc , model

def inference(row, scaler, model, feat_cols):
    df = pd.DataFrame([row], columns = feat_cols)
    X = scaler.transform(df)
    features = pd.DataFrame(X, columns = feat_cols)
    if (model.predict(features)==0):
        return "Votre situation est normale, vous êtes en bon état!"
    else: return "Il y a de très forte chance qu'il y ait un fort déséquilibre entre votre taux d'insuline et votre taux de sucre!"

st.title('Voyager avec DiabINT')
st.markdown('<h3 style="color: green;">Suivez de plus près votre équilibre taux de glucose/taux d\'insuline pour voyager en toute tranquilité. Déterminer en temps réel l\'influence de votre alimentation sur cet équilibre pour profiter pleinement de votre voyage. Voyagez sans souci, voyagez avec DiabINT!</3>', unsafe_allow_html=True)

image = Image.open('images/logo_MonMedecin.jpg')
st.image(image, use_column_width=True)

html_temp = """
<div style="background-color:#800080;padding:1.5px">
<h1 style="color:white;text-align:center;">
  <a href="/DiabInfo" style="color:white;text-decoration:none;">M'informer sur le diabète 📃</a>
</h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)
html_temp1 = """
<div style="background-color:#800080;padding:1.5px">
<h1 style="color:white;text-align:center;">
  <a href="/DiabStatistics" style="color:white;text-decoration:none;">Trouver les bonnes statistiques 📊</a>
</h1>
</div><br>"""
st.markdown(html_temp1,unsafe_allow_html=True)
html_temp2 = """
<div style="background-color:#800080;padding:1.5px">
<h1 style="color:white;text-align:center;">
    <a href="/DiabExercices" style="color:white;text-decoration:none;">Faire des exercices pour régulariser mon taux de glycémie 🏃🏻‍♂️</a>
</h1>
</div><br>"""
st.markdown(html_temp2,unsafe_allow_html=True)

html_temp3 = """
<div style="background-color:#800080;padding:1.5px">
<h1 style="color:white;text-align:center;">
    <a href="/Mon_Espace_DiabINT" style="color:white;text-decoration:none;">Mon espace personnel 🔒</a>
</h1>
</div><br>"""
st.markdown(html_temp3,unsafe_allow_html=True)

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
