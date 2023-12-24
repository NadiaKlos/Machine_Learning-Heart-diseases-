import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(
    page_title="Heart diseases",
    page_icon="🫀",
)

st.sidebar.image("https://www.visiblebody.com/hubfs/learn/assets/glossary/circulatory/circulatory-system-cardiac-cycle-gif.gif")
st.sidebar.markdown("## **Subject Area** :\n*__Health and Medicine__*")
st.sidebar.markdown("## **Dataset Characteristics** :\n*__Multivariate__*")
st.sidebar.markdown("## **Feature Type** :\n*__Integer__*")


st.title("Bienvenue dans votre app santé !")
st.write("Voici les données que nous utiliserons pour cette étude")
st.image('https://polyclinique2sm.com/wp-content/uploads/2022/05/cardiologie.jpg')

Heart_disease=pd.read_csv('Heart_Disease_Data.csv')
Heart_disease.replace('?', np.nan, inplace=True)
Heart_disease=Heart_disease.dropna()
nouveaux_noms = {'cp': 'chest_pain_type', 'trestbps': 'resting_blood_pressure','chol': 'cholesterol','fbs': 'fasting_blood_sugar',
                 'restecg': 'resting electrocardiographic', 'thalach': 'maximum_heart_rate','exsang': 'induced angina',
                 'oldpeak': 'ST depression'}
Heart_disease = Heart_disease.rename(columns=nouveaux_noms)

st.write("Les données : ",Heart_disease.head(30))
st.write("Nombres de lignes : ", Heart_disease.shape[0])
st.write("Nombre de colonnes : ", Heart_disease.shape[1])

st.markdown("<h3 style='color: red;'>Informations sur les colonnes :</h3>", unsafe_allow_html=True)
st.write("""
- **age**: L'âge des patients en années.
- **sex**: Le sexe des patients. 1 représente les hommes, 0 représente les femmes.
- **chest_pain_type**: Le type de douleur thoracique ressentie par les patients, souvent classifié en quatre catégories.
- **resting_blood_pressure**: La pression artérielle mesurée au repos en mm Hg (millimètres de mercure).
- **cholesterol**: Le taux de cholestérol mesuré en mg/dl (milligrammes par décilitre).
- **fasting_blood_sugar**: Le taux de sucre dans le sang à jeun. 1 indique une glycémie supérieure à 120 mg/dl, 0 indique le contraire.
- **resting electrocardiographic**: L'activité électrique cardiaque au repos, souvent notée en trois catégories.
- **maximum_heart_rate**: La fréquence cardiaque maximale atteinte par les patients.
- **exang**: Angine de poitrine induite par l'exercice. 1 indique la présence, 0 l'absence.
- **ST depression**: La dépression du segment ST induite par l'exercice par rapport au repos.
- **slop**: La pente du segment ST de l'ECG à l'exercice.
- **ca**: Le nombre de vaisseaux sanguins principaux colorés par fluoroscopie.
- **thal**: Le résultat du test au thallium.
""")


    





