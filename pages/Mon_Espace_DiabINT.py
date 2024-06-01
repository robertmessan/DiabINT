import streamlit as st

import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition
import pages
from PIL import Image
from pages import Login_and_Registration


im2=Image.open("images/logo_MonMedecin.jpg")
st.set_page_config(page_title="Ma Glycémie",page_icon=im2, layout="wide")

pickle_in = open('models/logisticRegr.pkl', 'rb')
classifier = pickle.load(pickle_in)

#img_path = 'data/diabete1.png'
def Diabetes_Predict():
    try:
        # st.button('LOGOUT')
        # Display user data
        st.write(st.session_state["user_data"])
        username=st.session_state["user_data"][0]
        # st.subheader(f"Welcome!!! {username} ")
        html_temp = """
        <div style="background-color:tomato;padding:1.5px">
        <h1 style="color:white;text-align:center;">Système de Gestion du Diabète 💉</h1>
        </div><br>"""
        st.markdown(html_temp,unsafe_allow_html=True)
     
        msg= f"""
           <div style="background-color:#666565;padding:3px;display:flex;align-items:center;justify-content:center;border-radius:10px;">
           <h3 style="margin:auto;text-align:center;"> Logged in as \t <span> {username}</span><h5>
           
           </div><br>
        """
       
        # st.sidebar.header(f'Welcome!!! {username}')
        # st.sidebar.markdown(msg,unsafe_allow_html=True)
        
        if st.sidebar.button('LOGOUT🔁'):
            # Clear user data from session state
            # st.session_state.pop("user_data", None)
            # Login_and_Registration.loginAndRegister()
            Login_and_Registration.loginAndRegister()
            st.session_state.logged_in = False
            st.session_state['user_data'] = None
            
            st.success('Logged out successfully.')
            return False    
    
            
    
            # st.stop()
        
        st.header('Diabetes Monitoring System')
        name = st.text_input("Entrez votre nom:",value=username)
        pregnancy = st.number_input("Nombre de grossesse(s) si vous êtes une femme:",step=1.)
        glucose = st.number_input("Concentration du Glucose sanguin :",step=10.)
        bp =  st.number_input("Pression artérielle diastolique (mm Hg):",step=10.)
        skin = st.number_input("Épaisseur du pli cutané du triceps (mm):",step=5.)
        insulin = st.number_input("Insuline sérique sur 2 heures (mu U/ml):",step=10.)
        #poids= st.number_input("Poids (en kg):",step=10.,key=7)
        #taille= st.number_input("Taille (en m):",step=0.1,key=7)
        #bmi=poids/(taille ** 2)
        bmi = st.number_input("indice de masse corporelle (poids en kg/(taille en m)^2):",step=10.,key=7)
        dpf = st.number_input("Fonction Pedigree de Diabetes(sur 100 membres de votre famille, combien sont diabétiques(entre 0 et 1) ?",step=0.1,key=8)
        age = st.number_input("Age:",step=5.,key=9)
        
        # Création d'un DataFrame avec les données entrées par l'utilisateur
        user_data = pd.DataFrame({
            'Variable': ['glucose', 'pression_artérielle', 'pli_cutané', 'insuline', 'indice_masse_corporelle', 'fonction_pedigree'],
            'Value': [glucose, bp, skin, insulin, bmi, dpf]
        })
        
        # Intervalles normaux pour chaque variable (à adapter selon les normes médicales)
        normal_ranges = {
            'glucose': (70, 140),
            'pression_artérielle': (60, 130),
            'pli_cutané': (10, 30),
            'insuline': (40, 90),
            'indice_masse_corporelle': (18.5, 30),
            'fonction_pedigree': (0.1, 1),
        }
        submit = st.button('Prédire 🔍')
        if submit:
            prediction = classifier.predict([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]])
            # html = f"""
            #         <html>
            #             <body>
            #                 <h1>Diabetic Prediction Form</h1>
            #                 <p><strong>Name:</strong> {name}</p>
            #                 <p><strong>Age:</strong> {age}</p>
            #                 <p><strong>Pregnancy:</strong> {glucose}</p>
            #                 <p><strong>Blood Pressure:</strong> {bp}</p>
            #                 <p><strong>Skin fold thickness:</strong> {skin}</p>
            #                 <p><strong>2-hour serun Insulin:</strong> {insulin}</p>
            #                 <p><strong>Body mass index:</strong> {bmi}</p>
            #                 <p><strong>Pedigree function:</strong> {dpf}</p>
            #             </body>
            #         </html>
            #         """
            # # Convert the HTML content to a PDF file
            # pdfkit.from_string(html, "form.pdf")
    
            # # Create a SendGrid message and attach the PDF file
            # message = Mail(
            #     from_email="19c16@sdmit.in",
            #     to_emails="cturuby@gmail.com",
            #     subject="Diabetic Prediction Form",
            #     html_content="Please find attached the PDF file with your form data.")
            # with open("form.pdf", "rb") as f:
            #     data = f.read()
            # attachment = Attachment(
            #     FileContent(data),
            #     FileName("form.pdf"),
            #     FileType("application/pdf"),
            #     Disposition("attachment")
            # )
            # message.attachment = attachment
    
            #  # Send the email using SendGrid
            # try:
            #     # sg = SendGridAPIClient("YOUR_API_KEY")
            #     sg=SendGridAPIClient('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')
            #     response = sg.send(message)
            #     st.success("Form submitted successfully. Check your email for the PDF file.")
            # except Exception as e:
            #     st.error("Failed to send the email. Please try again later.")
            #     st.write(str(e))
    
    
            #Printing the result
            if prediction == 0:
                # st.success(name.upper()+'!!! You're healthy! Your glucose/insulin balance is good😃')
                html_temp = f"""
                        <div style="background-color:#748c08;padding:1.5px;border-radius:20px;">
                        <h4 style="color:white;text-align:center;">{name.upper()}!!! Vous êtes en bon état ! Votre équilibre glucose/insuline est bon😃</h4>
                        </div><br>"""
                st.markdown(html_temp,unsafe_allow_html=True)
            else:
                # st.warning(name.upper()+'... we are really sorry to say, but it seems like you are Diabetic. ☹️')
                html_temp = f"""
                        <div style="background-color:#ad0f03;padding:1.5px;border-radius:20px;">
                        <h4 style="color:white;text-align:center;">{name.upper()} ... Attention, il semble que votre rapport glucose/insuline soit déséquilibré. Lisez les conseils sur notre page ! ☹️</h4>
                        </div><br>"""
                st.markdown(html_temp,unsafe_allow_html=True)
            # Intervalles normaux pour chaque variable (à adapter selon les normes médicales)
            
            # Comparaison des valeurs avec les intervalles normaux
            # Barres d'erreur pour les intervalles normaux
            normal_means = [sum(range_) / 2 for range_ in normal_ranges.values()]
            normal_errors = [(max_ - min_) / 2 for min_, max_ in normal_ranges.values()]
            
            # Comparaison des valeurs avec les intervalles normaux

            plt.figure(figsize=(10, 6))
            for i, (var, (min_val, max_val)) in enumerate(normal_ranges.items()):
                if var in user_data['Variable'].values:  # Vérifie si la variable est saisie par l'utilisateur
                    plt.subplot(2, 3, i+1)
                    user_value = user_data[user_data['Variable'] == var]['Value'].iloc[0]
                    if min_val <= user_value <= max_val:
                        color = 'green'
                    elif user_value < min_val:
                        color = 'yellow'
                    else:
                        color = 'red'
                    plt.axhline(y=normal_means[i], color='blue', linestyle='--', label='Moyenne du cas normal')
                    plt.axhspan(normal_ranges[var][0], normal_ranges[var][1], color='blue', alpha=0.3, label='Plage Normale')
                    plt.bar([name], [user_value], color=color)
                    plt.title(var)
                    plt.xticks(rotation=45)
            plt.legend()
            plt.tight_layout()
            st.pyplot(plt)
            #img_path = 'prediction_plot.png'
            #plt.savefig(img_path)
            #st.image(img_path, use_column_width=True)

        #st.subheader("Envoyer mes résultats à mon Médecin")
        # Afficher le formulaire de contact
        #contact_form = """
        #<form action="https://formsubmit.co/robertmessan30@gmail.com" method="POST">
           # <input type="hidden" name="_captcha" value="false">
            #<input type="hidden" name="name"  placeholder="{name}">
            #<input type="email" name="email" placeholder="votre email">
           # <input type="hidden" name="image" value="{img_path}">
            #<input type="hidden" name="prediction" value="{prediction}">
            #<textarea name="message" style="display:none;">Résultat de la prédiction et image en pièce jointe.</textarea>
            #<input type="hidden" name="_next" value="https://voyag-int.rf.gd" />
            #<button type="submit">Envoyez mes résultats à mon médecin</button>
        #</form>
        #""" .format(doctor_email=doctor_email, name=name, email=email, image=img_path,prediction=prediction)            
        #st.markdown(contact_form, unsafe_allow_html=True)
            
    except Exception as e:
        Login_and_Registration.loginAndRegister()
        st.write("Cliquez à nouveau sur la section Mon Espace DiabINT pour avoir accès à votre espace après le loggin")

    
if __name__ == "__main__":
    Diabetes_Predict()


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

