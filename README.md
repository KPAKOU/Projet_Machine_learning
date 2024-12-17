# Projet de machine learning
# Prediction de la consommation d'energie des batiments non residentiels de la ville de seattle.

## Description du projet

La ville de Seattle s’intéresse de près aux émissions des bâtiments non destinés à l’habitation: Prédiction de la
 consommation d’énergie
 Vous travaillez pour la ville de Seattle. Pour atteindre son objectif de ville neutre en émissions de carbone en 2050,
 votre équipe s’intéresse de près à la consommation totale d’énergie des bâtiments non destinés à l’habitation.
 Votre prédiction se basera sur les données déclaratives du permis d'exploitation commerciale (taille et usage des
 bâtiments, mention de travaux récents, date de construction..)
 Vous cherchez également à évaluer l’intérêt de l’
 ENERGY STAR Score pour la prédiction de consommation d’énergie,
 qui est fastidieux à calculer avec l’approche utilisée actuellement par votre équipe
##  Votre mission
 Voici un récapitulatif de votre mission :
 1.Réaliser une analyse exploratoire.
 2.Tester différents modèles de prédiction afin de répondre au mieux à la problématique.
 3.API ou dashboard pour prédire la consommation d'un bâtiment
 4.Réaliser les tâches MLOps pour ce projet

## Dataset

L'ensemble de données utilisé dans ce projet comprend des informations détaillées sur les bâtiments de Seattle, englobant les types résidentiels et non résidentiels. Les principales caractéristiques comprennent la taille du bâtiment, l'emplacement (latitude et longitude) et les statistiques de consommation d'énergie. La variable cible est: `SiteEnergyUse(Kbtu)`

## Analyse exploratoire des données 
confère le notebook exploration pour: 
1. **Traitement des valeurs manquantes**: 
2. **Analyse des distributions des variables**: 
3. **Analyse des correlation entre les variables**

## Feature Engineering

1. **Traitement des valeurs manquantes**: Nous avons traiter les valeurs mannquantes en fonction des types des variables et avec utilisation des technique specifique à chaque cas.
2. **Detection des valeurs aberrantes**: Used Interquartile Range (IQR) method to identify and handle outliers.
3. **Categorical Encoding**: Utilisation de onehot encoding qui a été appliqué à travers les pipelines dans la partie modelisation.
4. **Creation des nouvelles variables**: Nous avons creer une variable Age pour prendre en compte l'âge des batiments au lieu de l'année de construction et la variable harvesine_distance qui nous permet de prendre en compte la distance du batiment au centre de la ville de Seattle.

## Modelisation

1. **Selection des modèles**: test de plusieurs modèles linéaires et non linéaires : `Regression linéaire`,`Lasso`,`ridge`,`XGBOOST`,`RandomForest`,`SVR`
2. **Optimisatio des hyperparamètres et evaluation**: Nous avons créer une fonction qui optimise les hyperparamètres avec le cross-validation et evalue chaque chaque modèle. Les metriques utilisés pour evaluer les modèles sont R²,RMSE,MAE.


### Selection du  performant:
Chaque modèle est evalué avec la presence ou non de la variable `ENERGYSTARSCore` afin de voir l'influence de cette dernière.
Globalement il a été constaté qu'en presence de la variable `ENERGYSTARScore` les modèles étaient plus performants.
- **Resultats**: Sans la variable `ENERGYSTARScore` on a 2 modèles qui sont les plus performants notamment le modèle `SVR` et `XGBOOST`. L'importances des variables étaient relativement le même pour les deux modèles. 
Avec `ENERYSTARScore` le modèle le plus performant est le `RandomForest` 
- **Importances des variables**: Pour les modèles performants nous avons determiner les variables importantes. Il est à noter que la variable `ENERGYSTARScore` ameliore considerablement le score des modèles


## Execution du projet

1. **Cloner le repositoire**: `git clone <repo_url>`
2. **Installer les dependences**: `pip install -r requirements.txt`
3. **Exectuer les notebooks**: `jupyter notebook`


## Remerciements 
- Ce projet a été réalisé dans le cadre du cours de Machine learning.


## Auteurs
KPAKOU M’Mounéné , ISE2 ENSAE
Oumar Farouk, ISE2 ENSAE
Gnalen Sangaré, ISE2 ENSAE
ADAM ALASSANE Ibrahim, ISE2 ENSAE
## Sous la supervision 
Mme Mously Diaw ,ML Engineer


