import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

st.set_page_config(
    page_title="Heart diseases",
    page_icon="🫀",
)

st.sidebar.image("https://www.visiblebody.com/hubfs/learn/assets/glossary/circulatory/circulatory-system-cardiac-cycle-gif.gif")
st.sidebar.markdown("## **Subject Area** :\n*__Health and Medicine__*")
st.sidebar.markdown("## **Dataset Characteristics** :\n*__Multivariate__*")
st.sidebar.markdown("## **Feature Type** :\n*__Integer__*")

Heart_disease=pd.read_csv('Heart_Disease_Data.csv')
Heart_disease.replace('?', np.nan, inplace=True)
Heart_disease=Heart_disease.dropna()
nouveaux_noms = {'cp': 'chest_pain_type', 'trestbps': 'resting_blood_pressure','chol': 'cholesterol','fbs': 'fasting_blood_sugar',
                 'restecg': 'resting electrocardiographic', 'thalach': 'maximum_heart_rate','exsang': 'induced angina',
                 'oldpeak': 'ST depression'}
Heart_disease = Heart_disease.rename(columns=nouveaux_noms)

#for column in Heart_disease.columns:
 #   Heart_disease[column] = pd.to_numeric(Heart_disease[column], errors='coerce').astype('Int64')



df = pd.DataFrame(Heart_disease)
X = Heart_disease[['sex','age','chest_pain_type','exang','ST depression','ca','thal']]
Y = Heart_disease['pred_attribute']

svm = SVC()
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Interface Streamlit pour saisir les valeurs des caractéristiques
st.title('Prédiction des pathologies cardiovasculaires')
st.markdown("<h3 style='color: green;'>Rappel des informations sur les variables :</h3>", unsafe_allow_html=True)
st.write("""
- **age**: L'âge des patients en années.
- **sex**: Le sexe des patients. 1 représente les hommes, 0 représente les femmes.
- **chest_pain_type**: Le type de douleur thoracique ressentie par les patients, souvent classifié en quatre catégories.
- **maximum_heart_rate**: La fréquence cardiaque maximale atteinte par les patients.
- **exang**: Angine de poitrine induite par l'exercice. 1 indique la présence, 0 l'absence.
- **ST depression**: La dépression du segment ST induite par l'exercice par rapport au repos.
- **ca**: Le nombre de vaisseaux sanguins principaux colorés par fluoroscopie.
- **thal**: Le résultat du test au thallium.
""")

user_inputs = {}
for column in X.columns:
    try:
        user_inputs[column] = st.selectbox(f"Sélectionnez la valeur pour '{column}'", range(int(X[column].min()), int(X[column].max()) + 1))
    except ValueError:
        st.write(f"La colonne '{column}' ne peut pas être convertie en nombres entiers.")
        
if st.button('Valider🟩'):
    with st.spinner('The model is running🏃🏃🏃...'):
        new_data_values = [user_inputs[column] for column in X.columns]
        new_data_scaled = scaler.transform([new_data_values])
        svm.fit(X_scaled, Y)
        prediction = svm.predict(new_data_scaled)
        if prediction[0] == 0:
            st.image("https://usagif.com/wp-content/uploads/firework-1.gif")
            st.write("Félicitations🥳! Vous avez peu de chance d'avoir une pathologie cardiovasculaire actuellement. \nToutefois, pour plus de prudence, nous vous invitons à consulter un spécialiste.")
        else:
            st.image("https://i.pinimg.com/originals/01/6c/c3/016cc3790e87db8262301c5982b7f127.gif")
            st.write("‼️ Attention vous avez de fortes chances de présenter une pathologie cardiovasculaire en ce moment, nous vous invitons à consulter un spécialiste au plus vite.")
        
