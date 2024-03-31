
import streamlit as st
import pandas as pd


html_temp = """
<div style="background-color:#f2b016;padding:1.5px">
<h1 style="color:white;text-align:center;">Système de recommandation alimentaire 🥗</h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)

# New code for food recommendation


# Load data
foods_df = pd.read_csv('data/food_dataset.csv')

def check_veg(row):
    if "veg" in row["Veg_Non"].lower():
        return "veg"
    elif "non-veg" in row["Veg_Non"].lower():
        return "non-veg"
    else:
        return "unknown"

# Define function to filter food based on nutrient, disease, and food type
def filter_food(nutrient, disease):
    filtered_food = foods_df[(foods_df['Nutrient'].str.contains(nutrient)) & 
                             (foods_df['Disease'].str.contains(disease)) 
                            #  (foods_df['Veg_Non'].str.contains(food_type))
                            ]
    
    return filtered_food

# Define Streamlit app




st.success('Bienvenue ! Veuillez indiquer vos préférences en matière de nutriments et de maladies pour recevoir des recommandations alimentaires.')

    
    # User input for nutrient, disease, and food type
nutrient = st.selectbox('Sélectionnez le nutriment sur lequel vous souhaitez vous concentrer:', ['fiber', 'vitamin_a', 'calcium', 'magnesium', 'sodium',
       'vitamin_c', 'protien', 'vitamin_e', 'iron', 'selenium',
       'carbohydrates', 'chloride', 'potassium', 'vitamin_d', 'manganese',
       'phosphorus', 'iodine'])
disease = st.selectbox('Choisissez la maladie:',['diabeties','cancer', 'obesity','hypertension','goitre','anemia','pregnancy',
        'rickets','scurvy','kidney_disease','heart_disease','eye_disease'])
# food_type = st.selectbox('veg', ['veg', 'non-veg'])
    
    # Filter food based on user input
# filtered_food = filter_food(nutrient, disease, food_type)

filtered_food = filter_food(nutrient, disease)

#Testing code
# df=pd.DataFrame(filter_food)
hide=['Meal_Id','Price']
df=filtered_food.drop(columns=hide)


if st.button('TROUVER UN REPAS 🔍'):
    if filtered_food.empty:
        st.write('Désolé, aucune recommandation alimentaire n\'a été trouvée.')
    else:
        st.write('Voici quelques recommandations pour vous:')
        # st.write(filtered_food)
        st.write(df)


    # Display filtered food

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







st.markdown("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[Retourner sur la page d'accueil](https://github.com/robertmessan)\n\n\n\n")
st.markdown("\n\n\n\n\n[Kossi Robert MESSAN](https://www.linkedin.com/in/kossi-robert-messan-252954223/)")

