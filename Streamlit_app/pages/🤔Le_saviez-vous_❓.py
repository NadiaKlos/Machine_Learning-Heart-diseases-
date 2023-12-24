import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Heart diseases",
    page_icon="🫀",
)

st.sidebar.image("https://www.visiblebody.com/hubfs/learn/assets/glossary/circulatory/circulatory-system-cardiac-cycle-gif.gif")
st.sidebar.markdown("## **Subject Area** :\n*__Health and Medicine__*")
st.sidebar.markdown("## **Dataset Characteristics** :\n*__Multivariate__*")
st.sidebar.markdown("## **Feature Type** :\n*__Integer__*")


st.title('Les maladies cardiovasculaires en France : Un enjeu de santé majeur\n')

st.write("\nLes maladies cardiovasculaires représentent l'une des principales causes de morbidité et de mortalité en France. Elles englobent un ensemble de pathologies touchant le cœur et les vaisseaux sanguins, telles que les maladies coronariennes, les accidents vasculaires cérébraux (AVC), l'hypertension artérielle, l'insuffisance cardiaque, entre autres.")
st.markdown("<h3 style='color: red;'>Prévalence et Impact :</h3>", unsafe_allow_html=True)
st.write("\nEn France, les maladies cardiovasculaires affectent un nombre significatif de personnes de tous âges et constituent une préoccupation majeure en santé publique. Elles représentent une part considérable des hospitalisations et sont responsables d'un nombre important de décès chaque année. Les facteurs de risque associés, tels que le tabagisme, la sédentarité, une alimentation déséquilibrée, l'hypertension artérielle et le diabète, contribuent à cette prévalence élevée.")

st.markdown("<h3 style='color: red;'>Facteurs de risques :</h3>", unsafe_allow_html=True)
st.write("\nPlusieurs facteurs de risque peuvent influencer le développement des maladies cardiovasculaires. Le mode de vie, incluant les habitudes alimentaires, le niveau d'activité physique, le stress, ainsi que les antécédents familiaux de maladies cardiaques, jouent un rôle crucial dans la survenue de ces pathologies.")

st.markdown("<h3 style='color: red;'>Prévention et Sensibilisation : </h3>", unsafe_allow_html=True)
st.write("\nLa prévention des maladies cardiovasculaires revêt une importance capitale. Les autorités sanitaires françaises mènent des campagnes de sensibilisation visant à informer la population sur les risques associés à ces maladies et à promouvoir des modes de vie plus sains. Cela inclut des programmes d'éducation, des recommandations en matière de régime alimentaire, de pratique d'exercice physique régulier, ainsi que des consultations médicales de suivi pour détecter et contrôler les facteurs de risque.")

st.markdown("<h3 style='color: red;'>Recherche et Innovation :</h3>", unsafe_allow_html=True)
st.write("\nLa recherche scientifique et médicale joue également un rôle crucial dans la lutte contre les maladies cardiovasculaires en France. Des avancées constantes dans le domaine médical, telles que de nouvelles thérapies, des technologies de diagnostic avancées, et des traitements innovants, contribuent à améliorer la prise en charge et la prévention de ces pathologies.")

st.write("\n Les maladies cardiovasculaires demeurent donc un défi de santé publique majeur en France. Bien que des progrès aient été réalisés dans la prévention et la prise en charge de ces maladies, une action continue est nécessaire pour réduire leur prévalence, sensibiliser davantage et encourager des modes de vie sains au sein de la population française.")

Heart_disease=pd.read_csv('Heart_Disease_Data.csv')
Heart_disease.replace('?', np.nan, inplace=True)
Heart_disease=Heart_disease.dropna()
nouveaux_noms = {'cp': 'chest_pain_type', 'trestbps': 'resting_blood_pressure','chol': 'cholesterol','fbs': 'fasting_blood_sugar',
                 'restecg': 'resting electrocardiographic', 'thalach': 'maximum_heart_rate','exsang': 'induced angina',
                 'oldpeak': 'ST depression'}
Heart_disease = Heart_disease.rename(columns=nouveaux_noms)
# Visualisations des données
st.title("Some visualisations")
df = pd.DataFrame(Heart_disease)
#Histogramme d'âge
plt.figure(figsize=(6, 4))
sns.histplot(data=df, x='age', bins=20, kde=True)
plt.title('Répartition des âges')
plt.xlabel('Âge')
plt.ylabel('Nombre de patients')
st.pyplot()


sns.set(style="whitegrid")
plt.figure(figsize=(6, 6))
sns.countplot(data=df, x='sex')
plt.title('Répartition des sexes')
plt.xlabel('Sexe (0: Femme, 1: Homme)')
plt.ylabel('Nombre de patients')
st.pyplot(plt.gcf())


correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matrice de corrélation')
st.pyplot()