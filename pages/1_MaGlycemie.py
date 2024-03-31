
import streamlit as st
import pickle

pickle_in = open('models/randomForest.pkl', 'rb')
classifier = pickle.load(pickle_in)

# Define the questions and answer options
questions = ["Sexe", "Polyurie (émission excessive d'urine)", "Polydipsie (soif excessive)", "Perte de poids soudaine", "Faiblesse", "Polyphagie (sensation de faim extrême et insatiable)", "Troubles de la vue", "démangeaisons", "irritabilité", "cicatrisation retardée", "parésie partielle (affaiblissement d'un muscle)", "raideur musculaire", "alopécie (calvitie)", "obésité (quantité excessive de graisse corporelle)"]
options = {
    "Sexe": ["Masculin", "Feminin"],
    "Polyurie (émission excessive d'urine)": ["Oui", "Non"],
    "Polydipsie (soif excessive)": ["Oui", "Non"],
    "Perte de poids soudaine": ["Oui", "Non"],
    "Faiblesse": ["Oui", "Non"],
    "Polyphagie (sensation de faim extrême et insatiable)": ["Oui", "Non"],
    "Troubles de la vue": ["Oui", "Non"],
    "démangeaisons": ["Oui", "Non"],
    "irritabilité": ["Oui", "Non"],
    "cicatrisation retardée": ["Oui", "Non"],
    "parésie partielle (affaiblissement d'un muscle)": ["Oui", "Non"],
    "raideur musculaire": ["Oui", "Non"],
    "alopécie (calvitie)": ["Oui", "Non"],
    "obésité (quantité excessive de graisse corporelle)": ["Oui", "Non"]
}

# Create the form using Streamlit
# st.title("Predict DIABETES with some simple questions")
html_temp = """
                    <div style="margin-top:30px;background-color:#f5de31;color:#000;padding:1.5px;border-radius:20px;">
                    <h3 style="color:#000;text-align:center;">Faire mon test pour <span style="color:red;font-size:35px;">LE DIABETE</span> en  "quelques Questions"</h3>
                    </div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)
Age = st.number_input("Entrez votre age:",step=10.0)

# Define variables to store the selected options
selected_options = []

# Display the form using Streamlit
i=0
for question in questions:
    st.subheader(question)
    option = st.radio("", options[question],key=i)
    selected_options.append(option)
    i=i+1

# Run the ML model when the user clicks the "Submit" button
if st.button("Soumettre"):
    # Convert selected_options to a list of integers (age is already an integer)
    selected_options = [Age] + [1 if option == "Oui" else 0 for option in selected_options]
    prediction = classifier.predict([selected_options])

    prediction = classifier.predict([selected_options])[0]
    proba = classifier.predict_proba([selected_options])[0][1] * 100

    if prediction == 0:
        html_temp = """
                    <div style="margin-top:30px;background-color:#748c08;padding:1.5px;border-radius:20px;">
                    <h4 style="color:white;text-align:center;">Vous n'avez pas les symptômes du diabète 😃</h4>
                    </div><br>"""
        st.markdown(html_temp,unsafe_allow_html=True)
    else:
        html_temp = """
                    <div style="background-color:#ad0f03;padding:1.5px;border-radius:20px;">
                    <h4 style="color:white;text-align:center;">Nous sommes vraiment désolés, mais il est fort probable que vous soyez diabétique. ☹️ </h4>
                    </div><br>"""
        st.markdown(html_temp,unsafe_allow_html=True)

      # Display the probability of being positive
    st.header(f"La probabilité d'être négatif pour le texte:  **:red[{100-proba:.2f}%]**")
    

#     html_code ="""
# <!DOCTYPE html>
# <html>
# <head>
#   <title>My App</title>
#   <style>
#     .gauge {
#   width: 100%;
#   max-width: 250px;
#   font-family: 'Roboto', sans-serif;
#   font-size: 32px;
#   color: #004033;
# }

# .gauge__body {
#   width: 100%;
#   height: 0;
#   padding-bottom: 50%;
#   background: #b4c0be;
#   position: relative;
#   border-top-left-radius: 100% 200%;
#   border-top-right-radius: 100% 200%;
#   overflow: hidden;
# }

# .gauge__fill {
#   position: absolute;
#   top: 100%;
#   left: 0;
#   width: inherit;
#   height: 100%;
#   background: #009578;
#   transform-origin: center top;
#   transform: rotate(0.25turn);
#   transition: transform 0.2s ease-out;
# }

# .gauge__cover {
#   width: 75%;
#   height: 150%;
#   background: #ffffff;
#   border-radius: 50%;
#   position: absolute;
#   top: 25%;
#   left: 50%;
#   transform: translateX(-50%);

#   /* Text */
#   display: flex;
#   align-items: center;
#   justify-content: center;
#   padding-bottom: 25%;
#   box-sizing: border-box;
# }

#   </style>
# </head>
# <body>
#   <div class="gauge">
#   <div class="gauge__body">
#     <div class="gauge__fill"></div>
#     <div class="gauge__cover"></div>
#   </div>
# </div>
#   <script>
#     const gaugeElement = document.querySelector(".gauge");

#     function setGaugeValue(gauge, value) {
#         if(value < 0 || value > 1) {
#         return;
#         }

#         gauge.querySelector(".gauge__fill").style.transform = `rotate(${value / 2}turn)`;
#         gauge.querySelector(".gauge__cover").textContent = `${Math.round(value * 100)}%`;
# }

# setGaugeValue(gaugeElement, 0.4);

#   </script>
# </body>
# </html>
# """
#     st.html(html_code)



import pandas as pd
import numpy as np

# Define the threshold values for each attribute
age_threshold = 40
bmi_threshold = 30
sex_threshold = 0
family_history_threshold = 0
physical_activity_threshold = 150
diastolic_pressure = 130
systolic_pressure = 80
taille=0.1

# Function to predict diabetes based on threshold values
def predict_diabetes(row):
    if row['age'] > age_threshold and bmi > bmi_threshold and row['FamilyHistory'] > family_history_threshold and row['physical_activity'] < physical_activity_threshold and row['systolic_pressure'] > systolic_pressure and row['diastolic_pressure'] > diastolic_pressure :
        return "Risque Eleve"
    else:
        return "Risque Faible"
    
html_temp = """
                    <div style="margin-top:30px;background-color:#f5de31;color:#000;padding:1.5px;border-radius:20px;">
                    <h3 style="color:#000;text-align:center;">Remplissez le deuxième FORMULAIRE <span style="color:green;font-size:35px;">pour confirmer </span>  "vos résultats"</h3>
                    </div><br>""" 
st.markdown(html_temp,unsafe_allow_html=True)  
    
age = st.number_input("Entrez votre âge:",step=5.)
poids=st.number_input("Entrez votre poids (en Kg):",step=5.)
taille=st.number_input("Entrez votre taille (en m):",value=taille,step=0.1)
bmi=poids/(taille**2)
#bmi = st.number_input("Enter BMI (Body mass index):",step=5.)
gender_map = {"Masculin": 0, "Feminin": 1}
# Create a selection menu for gender and convert to binary
gender = st.selectbox("Sélectionnez le sexe", list(gender_map.keys()))
gender_binary = gender_map[gender]
fh = {"Non": 0, "Oui": 1}
family_history = st.selectbox("Avez-vous des membres de votre famille ayant le diabète?", list(fh.keys()))
family_history_binary= fh[family_history]
physical_activity = st.number_input("Entrez votre niveau d'activité physique (en minuite par semaine): ",step=10.)
diastolic_pressure = st.number_input("Saisissez l'historique de votre tension artérielle (1ère prise):",step=10.)
systolic_pressure = st.number_input("Saisissez l'historique de votre tension artérielle(2ème prise):",step=10.)

submit = st.button('Prédire 🔍')

data = {'age': age, 'BMI': bmi, 'sex': gender_binary, 'FamilyHistory': family_history_binary, 'physical_activity': physical_activity, 'diastolic_pressure': diastolic_pressure, 'systolic_pressure': systolic_pressure }
data = pd.DataFrame(data, index=[0]) # Convert dictionary to dataframe


if submit:
    prediction = predict_diabetes(data.iloc[0])
    if prediction=="Risque Eleve":
        st.header(f"Le résultat du diagnostic(probabilité d'être diabétique):  **:red[{prediction}]**")
    elif prediction == "Risque Faible":
        st.header(f"Le résultat du diagnostic(probabilité d'être diabétique):  **:green[{prediction}]**")

st.write("Voici la donnée:\n")
st.write(data.iloc[0])

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
