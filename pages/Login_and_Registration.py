import streamlit as st
import pandas as pd
import hashlib
import pickle
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition
import pages

from pages import Mon_Espace_DiabINT



# Define a function to read the user data from the CSV file
def read_data():
    data = pd.read_csv("data/user_data.csv")
    return data

# Define a function to write the user data to the CSV file
def write_data(data):
    data.to_csv("data/user_data.csv", index=False)

# Create a function to simulate a login check
def simulate_login(username, password):
    if username == "example_user" and password == "example_password":
        return True
    else:
        return False
    
# Function to hash the password using SHA-256 algorithm
def hash_password(password):
    hash_object = hashlib.sha256(password.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig


pickle_in = open('models/logisticRegr.pkl', 'rb')
classifier = pickle.load(pickle_in)




def Diabetes_Predict():
    html_temp = """
    <div style="background-color:tomato;padding:1.5px">
    <h1 style="color:white;text-align:center;">Système de Gestion du Diabète 💉</h1>
    </div><br>"""
    st.markdown(html_temp,unsafe_allow_html=True)
   

    st.sidebar.header('Gestion du Diabète')
    name = st.text_input("Entrez votre nom:",key=1)
    pregnancy = st.number_input("Nombre de grossesse(s) si vous êtes une femme:",step=1.,key=2)
    glucose = st.number_input("Concentration du Glucose sanguin :",step=10.,key=3)
    bp =  st.number_input("Pression artérielle diastolique (mm Hg):",step=10.,key=4)
    skin = st.number_input("Épaisseur du pli cutané du triceps (mm):",step=5.,key=5)
    insulin = st.number_input("Insuline sérique sur 2 heures (mu U/ml):",step=10.,key=6)
    poids= st.number_input("Poids (en kg):",step=10.,key=7)
    taille= st.number_input("Taille (en m):",step=0.1,key=7)
    bmi=poids/(taille ** 2)
    #bmi = st.number_input("Body mass index (weight in kg/(height in m)^2):",step=10.,key=7)
    dpf = st.number_input("Fonction Pedigree de Diabetes(sur 100 membres de votre famille, combien sont diabétiques ?",step=0.1,key=8)
    age = st.number_input("Age:",step=5.,key=9)
    submit = st.button('Prédire 🔍')
    if submit:
        prediction = classifier.predict([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]])
        # html = f"""
        #         <html>
        #             <body>
        #                 <h1>Diabetic Monitoring Form</h1>
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
        #     subject="Diabetic Monitoring Form",
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
            st.success(name.upper()+'!!! Vous êtes en bon état ! Votre équilibre glucose/insuline est bon😃')
        else:
            st.warning(name.upper()+'... Attention, il semble que votre rapport glucose/insuline soit déséquilibré. Lisez les conseils sur notre page ! ☹️')
  


# Diabetes_Predict()




# Create a Streamlit app
def loginAndRegister():
    # st.sidebar.subheader(st.session_state)
    st.title("Formulaire de connexion et d'inscription")

    # Create a menu with two options: Login and Register
    menu = ["Login", "Register"]
    choice = st.sidebar.selectbox("Sélectionnez une option", menu)

    # Read the user data from the CSV file
    data = read_data()
    # Define variables for the user inputs
    


    # If the user selects "Register"
    if choice == "Register":
        # st.title('Register Form')
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        if st.button("Register"):
            # Check if the username is already in use
            if username in list(data["Username"]):
                st.warning("Username already exists. Please choose a different username.")
            # Check if the password and confirm password fields match
            elif password != confirm_password:
                st.warning("Passwords do not match. Please try again.")
            # If the username is new and the passwords match, add the user data to the CSV file
            else:
                hashed_password = hash_password(password)
                new_data = pd.DataFrame({"Username": [username], "Password": [hashed_password]})
                data = pd.concat([data, new_data], axis=0).reset_index(drop=True)
                write_data(data)
                st.success("Registration successful. Please log in.")
                # return True
        # return False
    
    # If the user selects "Login"
    elif choice == "Login":
        # st.title('Login Form')
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            # Check if the username and password are valid
            hashed_password = hash_password(password)
            if (username in list(data["Username"])) and (hashed_password == list(data[data["Username"]==username]["Password"])[0]):
                st.success("Logged in successfully.")
                # Store user data in session state
                if "user_data" not in st.session_state:
                    st.session_state["user_data"] = [username]
                # Diabetes_Predict()
                return True
                # st.stop()
                
            
            else:
                st.warning("Incorrect username or password. Please try again.")
        return False
                # st.stop()
                


# loginAndRegister()

# Run the app
if __name__ == "__main__":

    # Check if user is logged in
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # Create the login and registration forms
    if not st.session_state.logged_in:
        if loginAndRegister():
            st.session_state.logged_in = True


    # Show the diabetes prediction form if user is logged in
    if st.session_state.logged_in:
        # st.subheader("Diabetes Monitoring Form")
        Mon_Espace_DiabINT.Diabetes_Predict()


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
