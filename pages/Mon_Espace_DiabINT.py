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
from pages import Login_and_Registration



pickle_in = open('models/logisticRegr.pkl', 'rb')
classifier = pickle.load(pickle_in)

# st.set_page_config(page_title = "Diabetes Prediction")
st.set_page_config(layout="wide")


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
        bmi=poids/(taille ** 2)
        bmi = st.number_input("indice de masse corporelle (poids en kg/(masse en m)^2):",step=10.,key=7)
        dpf = st.number_input("Fonction Pedigree de Diabetes(sur 100 membres de votre famille, combien sont diabétiques ?",step=0.1,key=8)
        age = st.number_input("Age:",step=5.,key=9)
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

