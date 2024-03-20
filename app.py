import streamlit as st
import joblib
import pandas as pd
from PIL import Image
import numpy as np
import datetime as dt
import altair as alt

im1=Image.open("data/diabetes_image.jpg")
st.set_page_config(page_title="Robert",page_icon=im1, layout="wide")
@st.cache_data#(allow_output_mutation=True)
def load(scaler_path, model_path):
    sc = joblib.load(scaler_path)
    model = joblib.load(model_path)
    return sc , model

def inference(row, scaler, model, feat_cols):
    df = pd.DataFrame([row], columns = feat_cols)
    X = scaler.transform(df)
    features = pd.DataFrame(X, columns = feat_cols)
    if (model.predict(features)==0):
        return "Votre situation est normale, vous êtes en bon état!"
    else: return "Il y a de très forte chance qu'il y ait un fort déséquilibre entre votre taux d'insuline et votre taux de sucre!"

st.title('Voyager avec DiabINT')
st.write("Suivez au plus près votre équilibre taux de glucose/taux d'insuline pour voyager en toute tranquilité. Déterminer en tant réel l'influence de votre alimentation sur cette équilibre pour profiter pleinement de votre voyage. Voyagez sans souci, voyagez avec DiabINT!")
image = Image.open('data/diabetes_image.jpg')
st.image(image, use_column_width=True)
st.write("remplissez s'il vous plaît vos dernières informations pour avoir une vue précise de votre équilibre hormonal! ")

age =           st.sidebar.number_input("Votre âge", 1, 150, 25, 1)
pregnancies=0
sex = st.sidebar.radio("Sexe", ("Masculin", "Féminin"))
if sex == "Féminin":
    pregnancies = st.sidebar.number_input("Nombre de grossesses(passées)", 0, 20, 0, 1)
glucose =       st.sidebar.slider("Taux de glucose", 0, 200, 25, 1)
skinthickness = st.sidebar.slider("Epaisseur du pli cutané", 0, 99, 20, 1)
bloodpressure = st.sidebar.slider('Pression artérielle', 0, 122, 69, 1)
insulin =       st.sidebar.slider("Insuline", 0, 846, 79, 1)
poids=          st.sidebar.slider("Votre poids(en Kg)", 15.0, 450.0, 65.0, 1.0)
taille=          st.sidebar.slider("Votre taille(en m)", 1.0, 3.0,1.35, 0.01)
dpf=0.471
bmi = poids/(taille**2)
row = [pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, dpf, age]

if (st.button('Voir les résultats')):
    feat_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

    sc, model = load('models/scaler.joblib', 'models/model.joblib')
    result = inference(row, sc, model, feat_cols)
    st.write(result)


#Partie tableau de bord


if st.button("Visualiser le tableau de bord"):
    # Charger les données
    @st.cache_data
    def load_data():
        df = pd.read_csv('https://raw.githubusercontent.com/bradleyhrc/glucose-data/main/bhc-glucose-data.csv')
        df['Device Timestamp'] = pd.to_datetime(df['Device Timestamp'], format='%d-%m-%Y %H:%M')
        df['Date'] = df['Device Timestamp'].dt.date
        df['Time'] = df['Device Timestamp'].dt.time
        df['Hour'] = pd.DatetimeIndex(df['Device Timestamp']).hour
        df['Minute'] = pd.DatetimeIndex(df['Device Timestamp']).minute
        df['Minute'] = df['Minute'].apply(lambda x: round((x / 10), 0) * 10)
        df.loc[df['Minute'] >= 30, 'Hour'] += 0.5
        df['Glucose'] = np.where(pd.isnull(df['Historic Glucose mmol/L']), df['Scan Glucose mmol/L'], df['Historic Glucose mmol/L'])
        df = df.drop(df[df['Record Type'] == 6].index)
        df = df.drop(columns=['Historic Glucose mmol/L', 'Scan Glucose mmol/L'])
        df.loc[df['Glucose'] > 8.0, 'Range'] = 'High'
        df.loc[df['Glucose'] < 3.9, 'Range'] = 'Low'
        df.loc[(df['Glucose'] <= 8.0) & (df['Glucose'] >= 3.9), 'Range'] = 'Target'
        return df

    df = load_data()

    # Sidebar
    st.sidebar.title("Réglages")
    device_picker = st.sidebar.radio("Sélecteur d'appareil", ['FreeStyle Libre', 'FreeStyle LibreLink'])
    start_date = st.sidebar.date_input("Date de début", dt.date(2019, 8, 12))
    end_date = st.sidebar.date_input("Date de Fin", dt.date(2024, 4, 10), min_value=start_date, max_value=dt.date(2024, 4, 10))

    # Filter data
    filtered_df = df[(df['Device'] == device_picker) & (df['Date'] >= start_date) & (df['Date'] <= end_date)]

    # Glucose Plot
    st.subheader("Taux de Glucose")
    glucose_plot = alt.Chart(filtered_df).mark_line().encode(
        x='Time',
        y=alt.Y('Glucose', scale=alt.Scale(domain=[0, 20]), title='Blood Glucose (Mmol/L)'),
        color=alt.Color('Range', scale=alt.Scale(domain=['High', 'Low', 'Target'], range=['#77dd77', 'black', '#f75d59']), legend=None)
    ).properties(
        width=600,
        height=300,
        title='Taux de Glucodse de DiabINT'
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    )
    st.altair_chart(glucose_plot, use_container_width=True)

    # Glucose Table
    st.subheader("Table du Taux de Glucose ")
    st.write(filtered_df[['Device', 'Device Timestamp', 'Date', 'Range', 'Glucose']].sort_values(by='Device Timestamp').reset_index(drop=True).head(10))

    # Time in Target Barplot
    st.subheader("Rapport sur le taux de Glucose Normal vs Anormal")
    time_in_target_pipeline = filtered_df.groupby(['Range']).size().reset_index(name='Count')
    time_in_target_barplot = alt.Chart(time_in_target_pipeline).mark_bar().encode(
        x='Range',
        y='Count',
        color=alt.Color('Range', scale=alt.Scale(domain=['High', 'Low', 'Target'], range=['#f75d59', 'black', '#77dd77']), legend=None)
    ).properties(
        width=600,
        height=200,
        title='taux de Glucose Normal vs Anormal'
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    )
    st.altair_chart(time_in_target_barplot, use_container_width=True)

    # Average Glucose
    st.subheader("Taux de Glucose moyen par jour")
    mean_glucose_pipeline = filtered_df.groupby(['Hour']).agg({'Glucose': 'mean'}).reset_index()
    mean_glucose_plot = alt.Chart(mean_glucose_pipeline).mark_area(opacity=0.5).encode(
        x='Hour',
        y='Glucose'
    ).properties(
        width=600,
        height=300,
        title='Taux de Glucose moyen par jour'
    ).interactive()

    st.altair_chart(mean_glucose_plot, use_container_width=True)
