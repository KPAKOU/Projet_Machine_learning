import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import requests
from PIL import Image

# Configuration de l'application
st.set_page_config(page_title="Prédiction de consommation d'énergie",page_icon="🌆",layout="wide"
)

image=Image.open('Seattle.png')

# Barre latérale pour la navigation
with st.sidebar:
    st.image(image, width=200)
    pages = ["🏠Accueil", "🗂️Présentation des données", "📉Prédiction"]
    page = st.sidebar.radio("", pages)
    file = st.sidebar.file_uploader("Importer un fichier (CSV ou Excel)", type=["csv", "xlsx"])

# Chargement les données
if file:
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        elif file.name.endswith(".xlsx"):
            df = pd.read_excel(file)
        st.sidebar.success("Fichier chargé avec succès !")

else:
    st.sidebar.warning("Veuillez importer un fichier pour commencer.")


if page == "🏠Accueil":
    st.title("🌆 Prédiction de la consommation d'énergie des bâtiments à Seattle")
    st.markdown("""
            ### 🎯Objectif de l'application
            Cette application vise à prédire la consommation énergétique des bâtiments non résidentiels à Seattle, afin de contribuer à l'objectif de neutralité carbone de la ville d'ici 2050.

            ### 📶Étapes de l'application
            1. Importez et visualisez les données dans la section **Présentation des données**.
            2. Explorez les relations entre les variables grâce à des visualisations interactives.
            3. Passez à la section **Prédiction** pour effectuer une prédiction basée sur les caractéristiques du bâtiment.
            
            ### 📚Pages de l'application
            - **Accueil** : Présentation de l'application.
            - **Présentation des données** : Exploration des données.
            - **Prédiction** : Estimation de la consommation énergétique.
        """)        
elif page == "🗂️Présentation des données":
    st.title("📊 Présentation des données")
    if st.checkbox("Aperçu des données"):
                    num_rows = st.slider("Nombre de lignes à afficher", min_value=5, max_value=25, value=10)
                    st.dataframe(df.head(num_rows))
                    # Dimensions des données
                    st.write(f"**Nombre total de lignes** : {df.shape[0]} | **Nombre total de colonnes** : {df.shape[1]}")
                    # Variables catégorielles et numériques
                    st.subheader("Types de Variables")
                    col1, col2 = st.columns(2)
                    num_cols = df.select_dtypes(include=['number']).columns
                    cat_cols = df.select_dtypes(include=['object']).columns
                    with col1:
                            st.write("**Variables numériques**")
                            st.table(num_cols[:st.slider("Nombre à afficher", 1, len(num_cols), 5)])
                    with col2:
                            st.write("**Variables catégorielles**")
                            st.table(cat_cols[:st.slider("Nombre à afficher", 1, len(cat_cols), 5)])

    # Statistiques descriptives globales
    st.write("##### 🧾Statistiques descriptives des variables numériques")
    num_cols = df.select_dtypes(include=["number"])
    if not num_cols.empty:
                    st.write(num_cols.describe())
    else:
                    st.write("Aucune variable numérique disponible.")



    # Initialisation de l'état
    if 'active_analysis' not in st.session_state:
        st.session_state.active_analysis = None

    col1, col2, col3 = st.columns(3)

    # Boutons pour sélectionner le type d'analyse
    with col1:
        if st.button("Analyse univariée"):
            st.session_state.active_analysis = "unib"
    with col2:
        if st.button("Analyse bivariée"):
            st.session_state.active_analysis = "bib"
    with col3:
        if st.button("Analyse multivariée"):
            st.session_state.active_analysis = "multib"

    # Affichage en fonction du type d'analyse activé
    if st.session_state.active_analysis == "unib":
        st.write("---")
        st.subheader("🔍Analyse univariée")
        st.write("---")
        st.write("##### Variables numériques")
        num_col = st.selectbox("Sélectionnez une variable numérique", num_cols.columns)

        if num_col:
            fig = px.box(df, y=num_col, color_discrete_sequence=["green"])
            fig.update_layout(title=f"Boxplot - {num_col}")
            st.plotly_chart(fig)

        st.write("---")
        st.write("##### Variables catégorielles")
        cat_cols = df.select_dtypes(include=["object", "category"])
        cat_var = st.selectbox("Sélectionnez une variable catégorielle", cat_cols.columns)
        if cat_var:
            fig = px.pie(df, names=cat_var, hole=0.4)
            st.plotly_chart(fig)

    elif st.session_state.active_analysis == "bib":
        st.write("---")
        st.subheader("🔗📈Analyse bivariée")
        st.write("---")
        st.write("##### 🔗Relations entre deux variables numériques")
        num_col1 = st.selectbox("Variable numérique 1", num_cols.columns, key="num1")
        num_col2 = st.selectbox("Variable numérique 2", num_cols.columns, key="num2")

        if num_col1 and num_col2:
            fig, ax = plt.subplots()
            sns.scatterplot(x=df[num_col1], y=df[num_col2], ax=ax)
            ax.set_title(f"Nuage de points - {num_col1} vs {num_col2}")
            st.pyplot(fig)

        st.write("##### 🔗Relations entre une variable numérique et une catégorielle")
        cat_cols = df.select_dtypes(include=["object", "category"])
        num_col = st.selectbox("Variable numérique", num_cols.columns, key="num_cat")
        cat_col = st.selectbox("Variable catégorielle", cat_cols.columns, key="cat_num")
        if num_col and cat_col:
            fig, ax = plt.subplots()
            sns.boxplot(x=df[cat_col], y=df[num_col], ax=ax)
            ax.set_title(f"Boxplot - {num_col} par {cat_col}")
            ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
            st.pyplot(fig)

    elif st.session_state.active_analysis == "multib":
        st.write("---")
        st.subheader("📊🔢Analyse multivariée")
        st.write("---")
        st.write("##### 🌡️🗺️Heatmap de corrélation")
        heatmap_cols = st.multiselect("Sélectionnez les colonnes à inclure dans la heatmap", num_cols.columns)

        if heatmap_cols:
            corr = df[heatmap_cols].corr()
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
            ax.set_title("Matrice de corrélation")
            st.pyplot(fig)
        else:
            st.write("Veuillez sélectionner au moins une colonne pour afficher la heatmap.")

        st.write("##### 🔄📊Pairplot")
        pairplot_cols = st.multiselect("Sélectionnez les colonnes à inclure dans le pairplot", num_cols.columns)
        if pairplot_cols:
            fig = sns.pairplot(df[pairplot_cols], diag_kind="kde", corner=True)
            st.pyplot(fig)



elif page == "📉Prédiction":
    st.title("🔮Prédiction de consommation d'énergie")

        # Définition les options des variables catégorielles
    building_types = ["CAMPUS", "NONRESIDENTIAL", "SPS-DISTRICT K-12"]
    neighborhoods = [
            "SOUTHEAST", "NORTHEAST", "DOWNTOWN", "EAST", "NORTH", "MAGNOLIA / QUEEN",
            "ANNE", "LAKE UNION", "GREATER DUWAMISH", "BALLARD", "NORTHWEST", "CENTRAL", "SOUTHWEST", "DELRIDGE"
        ]
    primary_properties = [
            "HOTEL", "OTHER SERVICES AND FACILITIES", "MIXED USE", "EDUCATION", "STORAGE", "HEALTH AND MEDICAL",
            "OFFICE AND BUSINESS", "RETAIL AND PERSONAL SERVICES", "RESIDENTIAL AND HOUSING", "FOOD AND BEVERAGE"
        ]
    second_largest_options = [
            "UNDEFINED", "PARKING", "EDUCATION", "HEALTH AND MEDICAL", "STORAGE", "RETAIL AND PERSONAL SERVICES",
            "FOOD AND BEVERAGE", "ENTERTAINMENT AND LEISURE", "OFFICE AND BUSINESS", "OTHER SERVICES AND FACILITIES",
            "RESIDENTIAL AND HOUSING", "HOTEL"
        ]
    third_largest_options = second_largest_options

        # Choix du modèle à utiliser
    st.info("Dans cette partie, il est question de procéder à la prédiction de la consommation d'énergie. Remplissez les caractéristiques de votre bâtiment pour prédir sa consommation.")
    with st.form("prediction_form"):
            BuildingType = st.selectbox("Type de bâtiment", building_types)
            Neighborhood = st.selectbox("Quartier", neighborhoods)
            PrimaryProperty = st.selectbox("Propriété principale", primary_properties)
            SecondLargest = st.selectbox("Deuxième usage principal", second_largest_options)
            ThirdLargest = st.selectbox("Troisième usage principal", third_largest_options)
            NumberofBuildings = st.number_input("Nombre de bâtiments", min_value=0, step=1)
            NumberofFloors = st.number_input("Nombre d'étages", min_value=0, step=1)
            PropertyGFABuilding= st.number_input("Surface brute des bâtiments (GFA)", min_value=1000, step=1)
            PropertyGFAParking = st.number_input("Surface brute du parking (GFA)", min_value=0, step=1)
            NumberPropertyUseType = st.number_input("Nombre d'usages de la propriété", min_value=0, step=1)
            LargestPropertyUseTypeGFA = st.number_input("Surface brute du plus grand usage principal (GFA)", min_value=0, step=1)
            SecondLargestPropertyUseTypeGFA = st.number_input("Surface brute du deuxième usage principal (GFA)", min_value=0, step=1)
            ThirdLargestPropertyUseTypeGFA = st.number_input("Surface brute du troisième usage principal (GFA)", min_value=0, step=1)
            harvesine_distance = st.number_input("Distance Harvesine", min_value=0.0, step=0.1)
            ENERGYSTARScore = st.number_input("Score ENERGYSTAR", min_value=0, step=1)

            # Bouton de soumission
            submitted = st.form_submit_button("Prédire")

        # Prédiction lorsque le formulaire est soumis
    if submitted:
            # Création des données pour la requête
            input_data = {
                "BuildingType": BuildingType,
                "Neighborhood": Neighborhood,
                "PrimaryProperty": PrimaryProperty,
                "SecondLargest": SecondLargest,
                "ThirdLargest": ThirdLargest,
                "NumberofBuildings": NumberofBuildings,
                "ThirdLargestPropertyUseTypeGFA": ThirdLargestPropertyUseTypeGFA,
                "PropertyGFAParking": PropertyGFAParking,
                "PropertyGFABuilding": PropertyGFABuilding,
                "NumberPropertyUseType": NumberPropertyUseType,
                "LargestPropertyUseTypeGFA": LargestPropertyUseTypeGFA,
                "SecondLargestPropertyUseTypeGFA": SecondLargestPropertyUseTypeGFA,
                "NumberofFloors": NumberofFloors,
                "harvesine_distance": harvesine_distance,
                "ENERGYSTARScore": ENERGYSTARScore,
            }
            api_url = "http://127.0.0.1:8000/prediction/random_model/" 
            try:
                # Envoi des données à l'API
                response = requests.post(api_url, json=input_data)
                response.raise_for_status()  # Vérifier les erreurs HTTP
                # Affichage des résultats
                result = response.json()
                st.success(f"Prédiction : {result['La prédiction']:.2f} kBtu")
            except requests.exceptions.RequestException as e:
                st.error(f"Erreur lors de la requête : {e}")
