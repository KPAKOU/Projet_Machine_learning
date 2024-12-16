#!/usr/bin/env python
# coding: utf-8

# 

# <h1 style="text-align:center;color:yellow;font-size:50px;font-family:ALGERIAN;border:solid">Projet de Machine Learning</h1>

# <h1 style="text-align:center;color:yellow;font-size:50px;font-family:times">Ecole Nationale de la Statistique et de l'Analyse Economique Pierre NDIAYE (ENSAE)</h1><br>

# <div style="display:flex;text-align:justify">
#     
#     
# <ul style="text-align:justify;font-family:times;font-size:15px;list-style-type:circle; width:60%"> 
# <span style="font-weight:bold">Réalisé par : </span> 
#     <ul style="text-align:justify;font-family:times;font-size:15px;list-style-type:circle"> 
#         <li>KPAKOU M'Mounéné</li>                                      
#         <li>SANGARE Gnalen</li>
#         <li>Moussa Mahammadou Oumar Farouk</li>                                      
#         <li>ADAM Alassane</li>
#     </ul>
#     <span style="font-style: italic;font-size:13px">Élèves Ingénieurs Statisticiens Economistes</span>
# </ul>
#  
# <ul style="text-align:justify;font-family:times;font-size:15px;list-style-type:none;width:39%"> 
#  <li style="font-weight:bold">Sous la supervision de :</li> 
#  <li>Mme. Mously DIAW</li>                                     
#    
# </ul>
#     
# </div>   

# ![image.png](data:image/png;base64,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)

# <div style="background-color: blue;" >
# <h1 style="margin: auto; padding: 20px; color:#fff; ">Etape 1 - IMPORTATIONS DES DONNEES</h1>
# </div>

# ## LIBRAIRIES

# In[1]:


from pathlib import Path

import matplotlib.pyplot as plt
import missingno as msno
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import seaborn as sns
from plotly.subplots import make_subplots
from ydata_profiling import ProfileReport
from yellowbrick.regressor import ResidualsPlot
from scipy.stats import chi2_contingency


# In[2]:


# Le répertoire du projet contenant le dossier data
HOME_DIR = Path.cwd().parent
print(f"Home directory: {HOME_DIR}")

# Le répertoire des données
DATA_DIR = Path(HOME_DIR, "Data")
print(f"Data directory: {DATA_DIR}")

# Chargement des données
data = pd.read_csv(Path(DATA_DIR, "2016_Building_Energy_Benchmarking_20241107.csv"), sep =",")


# ### <font color="#2cb7b0" id=""> Description et nettoyage des données</font>

# In[3]:


data.info()


# ## Description des variables

# | Variable                          | Non-Null Count | Data type     | Description |
# |----------------------------------|----------------|-----------|-------------------|
# | OSEBuildingID                    | 3376 non-null  | int64     | Identifiant de la propireté |
# | DataYear                         | 3376 non-null  | int64     | Année d'enrégistrement |
# | BuildingType                     | 3376 non-null  | object    | Type de bâtiment |
# | PrimaryPropertyType              | 3376 non-null  | object    | Utilisation principale d’un bien |
# | PropertyName                     | 3376 non-null  | object    | Nom de la proprieté |
# | Address                          | 3376 non-null  | object    | Adresse postale de la propriété |
# | City                             | 3376 non-null  | object    | Ville de la propriété |
# | State                            | 3376 non-null  | object    | État de la propriété |
# | ZipCode                          | 3360 non-null  | float64   | Code postal |
# | TaxParcelIdentificationNumber    | 3376 non-null  | object    | Numéro d'identification fiscal |
# | CouncilDistrictCode              | 3376 non-null  | int64     | Code du district du conseil municipal |
# | Neighborhood                     | 3376 non-null  | object    | quartier |
# | Latitude                         | 3376 non-null  | float64   | Latitude |
# | Longitude                        | 3376 non-null  | float64   | Longitude |
# | YearBuilt                        | 3376 non-null  | int64     | Année de construction de la propriété |
# | NumberofBuildings                | 3368 non-null  | float64   | Nombre de bâtiments inclus dans le rapport de la propriété |
# | NumberofFloors                   | 3376 non-null  | int64     | Nombre d’étages déclarés dans Portfolio Manager |
# | PropertyGFATotal                 | 3376 non-null  | int64     | Surface de plancher brute totale du bâtiment et du parking |
# | PropertyGFAParking               | 3376 non-null  | int64     | Espace total en pieds carrés de tous les types de stationnement |
# | PropertyGFABuilding(s)           | 3376 non-null  | int64     | Surface totale en pieds carrés entre les surfaces extérieures des murs d’enceinte d’un bâtiment |
# | ListOfAllPropertyUseTypes        | 3367 non-null  | object    | Toutes les utilisations des biens immobiliers déclarées dans Portfolio Manager |
# | LargestPropertyUseType           | 3356 non-null  | object    | La plus grande utilisation d’un bien |
# | LargestPropertyUseTypeGFA        | 3356 non-null  | float64   | La surface de plancher brute (GFA) de la plus grande utilisation de la propriété |
# | SecondLargestPropertyUseType     | 1679 non-null  | object    | La deuxième plus grande utilisation d’une propriété |
# | SecondLargestPropertyUseTypeGFA  | 1679 non-null  | float64   | La surface de plancher brute (SPB) de la deuxième utilisation en importance de la propriété |
# | ThirdLargestPropertyUseType      | 596 non-null   | object    | La troisième plus grande utilisation d’un bien |
# | ThirdLargestPropertyUseTypeGFA   | 596 non-null   | float64   | La surface de plancher brute (SPB) de la troisième plus grande utilisation de la propriété |
# | YearsENERGYSTARCertified         | 119 non-null   | object    | Depuis que la propriété a reçu la certification ENERGY STAR |
# | ENERGYSTARScore                  | 2533 non-null  | float64   | Une cote de 1 à 100 calculée par l’EPA qui évalue la performance énergétique globale d’une propriété |
# | SiteEUI(kBtu/sf)                 | 3369 non-null  | float64   | L’intensité de consommation d’énergie du site (IUE) par surface|
# | SiteEUIWN(kBtu/sf)               | 3370 non-null  | float64   | L’intensité de consommation d’énergie du site normalisée en fonction des conditions météorologiques (WN) |
# | SourceEUI(kBtu/sf)               | 3367 non-null  | float64   | L’intensité de consommation d’énergie à la source (IUE) |
# | SourceEUIWN(kBtu/sf)             | 3367 non-null  | float64   | L’intensité de consommation d’énergie de la source normalisée en fonction des conditions météorologiques (IUE) |
# | SiteEnergyUse(kBtu)              | 3371 non-null  | float64   | La quantité annuelle d’énergie consommée par la propriété à partir de toutes les sources d’énergie |
# | SiteEnergyUseWN(kBtu)            | 3370 non-null  | float64   | La quantité annuelle d’énergie consommée par la propriété à partir de toutes les sources d’énergie ajustée à ce que la propriété aurait consommé pendant les conditions météorologiques moyennes sur 30 ans |
# | SteamUse(kBtu)                   | 3367 non-null  | float64   | La quantité annuelle de vapeur urbaine consommée par la propriété sur le site |
# | Electricity(kWh)                 | 3367 non-null  | float64   | La quantité annuelle d’électricité consommée par la propriété sur place |
# | Electricity(kBtu)                | 3367 non-null  | float64   | La quantité annuelle d’électricité consommée par la propriété sur place |
# | NaturalGas(therms)               | 3367 non-null  | float64   | La quantité annuelle de gaz naturel fournie par les services publics consommée par la propriété |
# | NaturalGas(kBtu)                 | 3367 non-null  | float64   | La quantité annuelle de gaz naturel fournie par les services publics consommée par la propriété |
# | DefaultData                      | 3376 non-null  | bool      | La propriété utilisait des données par défaut pour au moins une caractéristique de propriété |
# | Comments                         | 0 non-null      | float64   | Commentaires |
# | ComplianceStatus                 | 3376 non-null  | object    | Si une propriété a satisfait aux exigences en matière d’analyse comparative énergétique pour l’année de déclaration en cours |
# | Outlier                          | 32 non-null     | object    | Si une propriété est une valeur aberrante élevée ou faible (O/N) |
# | TotalGHGEmissions                | 3367 non-null  | float64   | La quantité totale d’émissions de gaz à effet de serre |
# | GHGEmissionsIntensity            | 3367 non-null  | float64   | Émissions totales de gaz à effet de serre divisées par la surface de plancher brute de la propriété |
# 

# Il est précisié dans le projet que **seuls les bâtiments non destinés à l'habitation seront étudiés**. Nous allons donc supprimer toutes les lignes correspondant à des habitations en nous basant sur la variable `BuildingType`

# In[4]:


data['BuildingType'].unique()


# In[5]:


data = data[~data['BuildingType'].str.contains("Multifamily")]
data['BuildingType'].unique()


# In[6]:


print("Le jeu de données compte à présent {} lignes et {} colonnes.".format(data.shape[0],data.shape[1]))


# ### Traitement de la modalité Campus
# 
# Suppression des campus principalement destinés aux logement multifamiliaux

# In[7]:


df_campus = data[data['BuildingType']== 'Campus']
df_campus['PrimaryPropertyType'].unique() # Nom des propriétés 


# In[8]:


df_campus


# In[9]:


# Suppression les lignes où la colonne 'PrimaryPropertyType' contient 'Low-Rise Multifamily'
data = data[data['PrimaryPropertyType'] != 'Low-Rise Multifamily']
data['PrimaryPropertyType'].unique()


# In[10]:


print(data["City"].unique())
print(data["State"].unique())
print(data["DataYear"].unique())


# Repartition des types de batiments

# In[11]:


building_type = data.groupby(by='BuildingType')['OSEBuildingID'].nunique()

font_title = {'family': 'serif',
              'color':  '#1d479b',
              'weight': 'bold',
              'size': 18,
             }

fig, ax = plt.subplots(figsize=(8,8))
ax.pie(building_type.values, labels=building_type.index, 
       autopct='%1.1f%%', shadow=True, startangle=30,
       textprops=dict(color="black",size=12, weight="bold"))
ax.axis('equal')
ax.set_title("Répartition des types de bâtiments du Dataset", fontdict=font_title)
plt.show()


# La majeur partie des bâtiments sont typés "NonResidential". Nous pouvons visualiser les diverses catégories représentées dans ce type de bâtiments :

# In[12]:


data.loc[(data['BuildingType']=="NonResidential"),'PrimaryPropertyType'].value_counts()


# #### Vocabulaire

# Significations de quelques acronymes
# 
# GHG: greenhouse gas emissions, correspond aux émissions des gazs à effet de serre.
# 
# OSE: Seattle Office of Sustainability and Environment.
# 
# EUI: Energy Use Intensity.
# 
# kBtu: kilo-British thermal unit, 1 kWh = 3.412 kBtu.
# 
# sf: square feet, 1m² = 10,7639sf.
# 
# WN: weather-normalized, normalisé vis à vis des conditions climatiques.
# 
# GFA: Gross floor area, Surface de plancher brute - La surface de plancher couverte (par un toit, même sans mur) 
#     totale contenue dans le bâtiment.
# 
# therm: mesure énergétique 1thm =100000Btu.
# 
# 

# Dans la visualisation, certaines variables apparaissent donc comme redondantes :
# - `Electricity(kWh)` et `Electricity(kBtu)`,
# - `NaturalGas(therms)` et `NaturalGas(kBtu)`
# 
# Nous allons donc commencer par supprimer ces variables :

# In[13]:


#Suppression des variables redondantes
redundant_features = ['NaturalGas(therms)','Electricity(kWh)']
data.drop(redundant_features, axis=1, inplace=True)


# Nous constatons qu'il n'y a pas de données dans les variables Outlier et Comments. La variable Comments renseigne sur les commentaires des propriétaires ou de tout autre agent concernant la consommation d'énergie, tandis que la variable Outlier indique si la propriété présente une valeur élevée ou faible. Nous devrons faire sans la variable Comments.
# 
# Les variables City et State n'ont pas un grand intérêt, car elles n'admettent chacune qu'une seule modalité. Il en est de même pour les variables ZipCode qui désigne ici le code postal.
# 
# De plus, nous avons constaté que, dans la base contenant des bâtiments non résidentiels, la variable cible `SiteEnergyUse (kBtu)` contient deux valeurs manquantes. Or, en modélisation, la variable cible ne peut pas être nulle.
# 
# Nous allons donc procéder aux modifications susmentionnées. Toutefois, bien que notre modèle de référence soit basé sur les jeux de données avant toute transformation, il existe des pistes à explorer en répondant aux questions suivantes :
# 
# Quelles sont les lignes pour lesquelles la variable Outlier n'est pas vide ?
# 

# In[14]:


# Suppression des colonnnes
data = data.drop(["Comments", "State", "City", "ZipCode", "CouncilDistrictCode","YearsENERGYSTARCertified","Outlier"], axis=1)
# 8 variables dropped


# ## Traitement des valeurs manquantes

# ### Affichage des variables ayant des valeurs manquantes

# In[15]:


# # A bar chart visualization of the nullity of the given DataFrame.
msno.bar(data[data.columns[data.isna().any()]], figsize = (25, 5))


# ## Traitement de la variable  **consommation d'énergie du bâtiment** (`SiteEnergyUse(kBtu)`)

# In[16]:


# Afficher les observations pour lesquelles la variable à prédire (SiteEnergyUse(kBtu)) n'est pas renseignée
energy_na = data["SiteEnergyUse(kBtu)"].isnull()
data.loc[energy_na, :]


# Certaines lignes comportent des manquants sur cette variable ainsi que les variables succeptibles de determiner le niveau de consommation de l'energie des bâtiments, nous allons donc les supprimer :

# In[17]:


data = data[~((data['SiteEnergyUse(kBtu)'].isnull()))]


# In[18]:


data.describe()


# Nouvelle visualisation des variables ayant les valeurs manquantes

# In[19]:


# # A bar chart visualization of the nullity of the given DataFrame.
msno.bar(data[data.columns[data.isna().any()]], figsize = (25, 5))


# 

# In[20]:


# Afficher les observations pour lesquelles la variable SiteEUI(kBtu/sf) n'est pas renseignée 
SiteEUI_kBtu_sf_na = data['SiteEUI(kBtu/sf)'].isnull()
data.loc[SiteEUI_kBtu_sf_na, ['PropertyName', 'SiteEUI(kBtu/sf)', 'SiteEnergyUse(kBtu)', 'PropertyGFATotal']]


# L'intensité de consommation d’énergie du site (IUE) peut êtimé par le rapport de la consommation d’énergie du site d’une propriété et sa surface de plancher brute.

# In[21]:


data['SiteEUI(kBtu/sf)'].fillna(data['SiteEnergyUse(kBtu)']/data['PropertyGFATotal'], inplace=True)
data.loc[SiteEUI_kBtu_sf_na, ['PropertyName', 'SiteEUI(kBtu/sf)', 'SiteEnergyUse(kBtu)', 'PropertyGFATotal']]


# In[22]:


# Afficher les observations pour lesquelles la variable SiteEUIWN(kBtu/sf) /SiteEnergyUseWN(kBtu) n'est pas renseignée 
SiteEUIWN_kBtu_sf_na = (data['SiteEUIWN(kBtu/sf)'].isnull() | data['SiteEnergyUseWN(kBtu)'].isnull())
data.loc[SiteEUIWN_kBtu_sf_na, ['PropertyName', 'SiteEUIWN(kBtu/sf)', 'SiteEnergyUseWN(kBtu)', 'PropertyGFATotal']]


# In[23]:


data['SiteEUIWN(kBtu/sf)'].fillna(data['SiteEUI(kBtu/sf)'], inplace = True)
data['SiteEnergyUseWN(kBtu)'].fillna(data['SiteEnergyUse(kBtu)'], inplace = True)
# Afficher les résultats
data.loc[SiteEUIWN_kBtu_sf_na, ['PropertyName', 'SiteEUIWN(kBtu/sf)', 'SiteEnergyUseWN(kBtu)', 'PropertyGFATotal']]


# In[24]:


# A new bar chart visualization of the nullity of the given DataFrame.
msno.bar(data[data.columns[data.isna().any()]], figsize = (25, 5))


# Nous allons traiter le reste des vairable dans la partie suivante

# ## Traitement des variables Utilisation du bien immobilier

# In[25]:


# Afficher les observations pour lesquelles la variable LargestPropertyUseType n'est pas renseignée
df=data
LargeUse_na = df.LargestPropertyUseType.isnull()
df.loc[LargeUse_na ,['OSEBuildingID', 'ListOfAllPropertyUseTypes', 'LargestPropertyUseType']] 


# Nous allons supposer que, pour les bâtiments pour lesquels la variable « LargestPropertyUseType » n’est pas spécifiée, la principale utilisation du bien correspond au premier élément de la liste de toutes les utilisations déclarées de ce bien immobilier. Il est d’ailleurs à noter que, pour la plupart de ces bâtiments, une seule utilisation du bien est enregistrée.

# In[26]:


# Traitement des Na de la variable "LargestPropertyUseType" comme mentionné ci-dessus
df.loc[LargeUse_na, "LargestPropertyUseType"] = [Use.split(",")[0].strip() for Use in df.loc[LargeUse_na, "ListOfAllPropertyUseTypes"]]
#
df.loc[LargeUse_na,['OSEBuildingID', 'ListOfAllPropertyUseTypes', 'LargestPropertyUseType']]


# In[27]:


# Afficher les observations pour lesquelles la variable LargestPropertyUseTypeGFA n'est pas renseignée
LargestPropertyUseTypeGFA_na = df.LargestPropertyUseTypeGFA.isnull()
df.loc[LargestPropertyUseTypeGFA_na ,['ListOfAllPropertyUseTypes', 'LargestPropertyUseType', 'LargestPropertyUseTypeGFA', 'PropertyGFATotal']]


# Pour la plupart de ces observation, une seule utilisation du bien immobilier est entrégistrée.   
# Par conséquent, les valeurs manquantes de la variable « surface de plancher brute (SPB) de la plus grande utilisation de la propriété » peuvent être attribuées à la surface de plancher brute totale associée à cette propriété.

# In[28]:


## Traitement des na comme mentionné ci-dessus
df['LargestPropertyUseTypeGFA'].fillna(df['PropertyGFATotal'], inplace=True)
## Voir le résultat du traitement
df.loc[LargestPropertyUseTypeGFA_na ,['ListOfAllPropertyUseTypes', 'LargestPropertyUseType', 'LargestPropertyUseTypeGFA', 'PropertyGFATotal']]


# Pour une analyse approfondie des variables "Deuxième plus grande utilisation d’une propriété", "Surface de plancher brute (SPB) de la deuxième utilisation en importance de la propriété.", "Troisième plus grande utilisation d’une propriété" et "Surface de plancher brute (SPB) de la troisième plus grande utilisation de la propriété.", nous allons créer une nouvelle variable fournissant le nombre d'utilisations de la propriété et qui sera nommée NumberPropertyUseType

# In[29]:


# Vréation de la variable NumberPropertyUseType
df['NumberPropertyUseType'] = [len(AllPropertyUseTypes.split(",")) for AllPropertyUseTypes in df.ListOfAllPropertyUseTypes]


# In[30]:


# Afficher les observations pour lesquelles la variable SecondLargestPropertyUseType n'est pas renseignée 
SecondLargestPropertyUseType_na = df.SecondLargestPropertyUseType.isnull()
df.loc[SecondLargestPropertyUseType_na, ['ListOfAllPropertyUseTypes', 'LargestPropertyUseType', 'SecondLargestPropertyUseType']]


# In[31]:


# Afficher les observations pour lesquelles la variable SecondLargestPropertyUseType n'est pas renseignée 
# et que plus d'une utilisation a été enrégistrée pour cette proprieté
df.loc[SecondLargestPropertyUseType_na & df.NumberPropertyUseType > 1, ['ListOfAllPropertyUseTypes', 'LargestPropertyUseType', 'SecondLargestPropertyUseType', 'NumberPropertyUseType']]


# Nous notons que la variable "Deuxième plus grande utilisation d’une propriété" est correctement enregistrée pour les propriétés qui enregistrent plus d'une utilisation. Par conséquent, es valeurs manquantes de la variable "SecondLargestPropertyUseType" est parfaitement justifiée.  
# 
# Une telle analyse peut également être effectuée sur les variables : SecondLargestPropertyUseTypeGFA, ThirdLargestPropertyUseType et ThirdLargestPropertyUseTypeGFA.

# In[32]:


# Variable SecondLargestPropertyUseTypeGFA
SecondLargestPropertyUseTypeGFA_na = df.SecondLargestPropertyUseTypeGFA.isnull()
df.loc[SecondLargestPropertyUseTypeGFA_na  & df.NumberPropertyUseType > 1, ['ListOfAllPropertyUseTypes', 'LargestPropertyUseType', 'SecondLargestPropertyUseTypeGFA']]


# In[33]:


# Variable ThirdLargestPropertyUseType
ThirdLargestPropertyUseType_na = df.ThirdLargestPropertyUseType.isnull()
df.loc[ThirdLargestPropertyUseType_na  & df.NumberPropertyUseType > 2, ['ListOfAllPropertyUseTypes', 'LargestPropertyUseType', 'ThirdLargestPropertyUseType']]


# In[34]:


# Variable ThirdLargestPropertyUseTypeGFA
ThirdLargestPropertyUseTypeGFA_na = df.ThirdLargestPropertyUseTypeGFA.isnull()
df.loc[ThirdLargestPropertyUseTypeGFA_na  & df.NumberPropertyUseType > 2, ['ListOfAllPropertyUseTypes', 'LargestPropertyUseType', 'ThirdLargestPropertyUseTypeGFA']]


# ## Les variables contenant encore des valeurs manquantes

# In[35]:


# A new bar chart visualization of the nullity of the given DataFrame.
msno.bar(df[df.columns[df.isna().any()]], figsize = (25, 5))


# Comme nous l'avons expliqué précédemment, l'absence de données pour les variables `SecondLargestPropertyUseType ` et `SecondLargestPropertyUseTypeGFA` `SecondLargestPropertyUseTypeGFA  `(ou respectivement `ThirdLargestPropertyUseType` et `ThirdLargestPropertyUseTypeGFA` ) est justifiée par le fait que les biens immobiliers correspondants sont dédiés à une seule utilisation (ou au plus deux).
# 
# 
# Enfin, s'agissant de la variable ` ENERGYSTARScore`  (score de performance énergétique globale d'une propriété) qui présente également des valeurs manquantes, nous examinerons après son importance pour la prédiction de la consommation d'énergie.</p>

# In[36]:


data=df


# ## <font color="#337da4" id="">Analyse exploratoire & Feature Engineering</font>

# <h3 style="margin: auto; padding: 20px; color: RGB(51,165,182); "> Analyse exploratoire des variables quantitatives</h3>

# ## Résumé descriptif des variables quantitatives

# In[37]:


## Résumé descriptifs des variables quantitatives
var_quanti = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
data[var_quanti[:15]].describe()


# ## Aperçu des boîtes à moustache

# In[38]:


# Nombre de box-plots par ligne
box_plots_per_row = 5

# Nombre total de lignes nécessaires
total_rows = (len(var_quanti) - 1) // box_plots_per_row + 1

# Création des sous-tracés
fig = make_subplots(rows=total_rows, cols=box_plots_per_row, subplot_titles=var_quanti)

# Affichage des box-plots sur les sous-tracés
for i, var in enumerate(var_quanti):
    row = i // box_plots_per_row + 1
    col = i % box_plots_per_row + 1

    box_fig = px.box(df, y=var, title=var)
    box_fig.update_yaxes(title_text=var)

    # Personnalisation des dimensions de la figure
    box_fig.update_layout(
        width=250,  # Largeur de la figure
        height=300,  # Hauteur de la figure
        margin=dict(l=50, r=50, b=50, t=50),  # Marges de la figure
    )

    # Ajout du box-plot au sous-tracé correspondant
    for trace in box_fig.data :
        fig.add_trace(trace, row=row, col=col)

# Mise à jour du layout de la figure principale
fig.update_layout(showlegend=False, height=total_rows * 300, width=box_plots_per_row * 250)

# Affichage de la figure principale
fig.show()


# La plupart des variables contiennent des valeurs extremes

# ### <font color="#2cb7b0" id="">Les corrélations linéaires</font>

# In[39]:


data_numeric = data.select_dtypes(include=[np.number])
corr = data_numeric.corr()
mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
fig, ax = plt.subplots(figsize=(15,15))
ax = sns.heatmap(corr, annot=True, fmt=".2f", annot_kws={'size':8}, 
                 mask=mask, center=0, cmap="coolwarm")
plt.title(f"Heatmap des corrélations linéaires\n", 
          fontdict=font_title)
plt.show()


# Les émissions de gaz à effet de serre présentent généralement une corrélation linéaire significative avec notre variable cible (`SiteEnergyUse(kBtu`)). Toutefois, il est important de noter que ces émissions sont estimées en fonction de la quantité d'énergie consommée. Par conséquent, la création d'un modèle de prédiction pour la quantité d'énergie consommée par un bâtiment ne devrait pas dépendre de la quantité d'émissions de gaz à effet de serre, car ces données ne sont estimées qu'après avoir déterminé la quantité d'énergie consommée par les bâtiments.
# Par contre, les variables `OSEBuildingID`, `DataYear`, `Latitude` et  `Longitude` présentent une très faibles corrélations avec les autres variables. Ce qui n'est sans doûte pas surprenant car ces variables sont censés nous permettre d'identifier les différentes observations et non les expliquer.

# Il semble clairement exister une corrélation parfaite entre la quantité d'électricité consommée et notre variable cible à prédire (`SiteEnergyUse(kBtu`). Ceci est vraisemblablement dû au fait que la variable cible semble être une somme parfaite de la quantité d'énergie consommée en électricité, en gaz naturel et en vapeur urbaine, comme le démontre la figure ci-dessous.

# Ces trois variables ne seront donc pas prises encore dans la formation du modèle prédictif. Cependant pour eviter la fuite des données (data leakage) nous allons calculer les ratio SteamUse, Electricity, NaturalGas

# La variable `PropertyGFATotal` présente une forte corrélation avec les variables `LargestPropertyUseTypeGFA` et `SecondLargestPropertyUseTypeGFA`. Ce que l'on pouvait s'y atttendre car cette première est déduite des autres. Dans la formation de notre modèle nous prendrons pas en compte la variable ` PropertyGFATotal`.

# Etant donné que les variables `SiteEUI(kBtu/sf)`, `SiteEUIWN(kBtu/sf)`, `SourceEUI(kBtu/sf)` et `SourceEUIWN(kBtu/sf)` sont calculées à partir de notre variable à prédire, elles ne seront donc pas prise en compte dans la formation de notre modèle.

# ### *Analyse de la variable SiteEnergyUse(kBtu)*

# In[40]:


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 4))

sns.histplot(data["SiteEnergyUse(kBtu)"], color='r', kde=True, ax=axes[0])
axes[0].set_title('Distribution - SiteEnergyUse(kBtu)')

sns.histplot(np.log(data["SiteEnergyUse(kBtu)"]), color='b', kde=True, ax=axes[1])
axes[1].set_title('Distribution - SiteEnergyUse(kBtu)$log$')
axes[1].set_xscale('log'); 


# Nous remarquons que la représentation en log est beaucoup plus intéressante, en ce sens que sa distrubution ressemble beaucoup plus à celle de la loi normale. Cependant, même le log de la variable n'est pas symétriquement distribué

# In[41]:


# statistiques descriptives
statistiques_ener = data['SiteEnergyUse(kBtu)'].describe()

# Calcul du coefficient de variation
#Il s'obtient en divisant l'écart-type de la variable par sa moyenne. C'est un indicateur de dipersion. On le 
# compare souvent à 0.3. S'il est supérieur à ce dernier, on dira que la variable est dispersée. Inversément
# on aboutit à la conclusion opposée.
cv_ener = data['SiteEnergyUse(kBtu)'].std() / data['SiteEnergyUse(kBtu)'].mean()  # Coefficient de variation

# Afficher un joli tableau avec les statistiques
print("Statistiques descriptives de la variable 'SiteEnergyUse(kBtu)':")
print(statistiques_ener)
print(f"Coefficient de variation : {cv_ener}")


# Faire la distribution du log(varcible)

# #### **Interprétations**

# La moyenne est de 7.373224e+06(kBtu), le minimum est de 0 et le max de 2.930908e+08. Il est à noter que 25% des bâtiments non résidentiels les moins énergivores de notre jeu de données consomment  1.215744e+06 d'énergie. Aussi, le quart des bâtiments le plus énergivores consomment 6.785911e+06. Il faut noter la consommation d'énergie est très dispersée.

# On remarque que la consommation minimale est nulle. Nous allons traiter ce cas

# In[42]:


data.loc[data['SiteEnergyUse(kBtu)'] == 0.0, ['Electricity(kBtu)', 'NaturalGas(kBtu)', 'SteamUse(kBtu)']]


# In[43]:


# Mise à jour de 'SiteEnergyUse(kBtu)' pour les lignes qui satisfont la condition
data.loc[data['SiteEnergyUse(kBtu)'] == 0.0, 'SiteEnergyUse(kBtu)'] = data.loc[data['SiteEnergyUse(kBtu)'] == 0.0, ['Electricity(kBtu)', 'NaturalGas(kBtu)', 'SteamUse(kBtu)']].sum(axis=1)


# In[44]:


data.loc[data['SiteEnergyUse(kBtu)'] == 0.0, ['Electricity(kBtu)', 'NaturalGas(kBtu)', 'SteamUse(kBtu)']]


# In[45]:


print("Nous avons a présent ", data.loc[data['SiteEnergyUse(kBtu)'] == 0.0, ['Electricity(kBtu)', 'NaturalGas(kBtu)', 'SteamUse(kBtu)']].shape[0], "batiments dont SiteEnergyUse est nulle")


# Pour ces 5 batiments, on remarque bien que la consommation d'énergie pour chaque source d'énergie est nulle. Ce type d'observation (ne présentant pas de consommation d'énergie) ne nous servirait à rien pour l'objectif de prédiction de la consommation d'énergie des batiments. Il s'agit peut-être de batiments non exploités. On choisit donc de supprimer les observations concernés

# In[46]:


data = data[data['SiteEnergyUse(kBtu)']!=0.0]


# In[47]:


# Calculer le 3e quartile (Q3) et le 1er quartile (Q1)
Q3 = data['SiteEnergyUse(kBtu)'].quantile(0.75)

# Trouver les lignes avec des valeurs dépassant le 3e quartile
valeurs_excedent_Q3 = data[data['SiteEnergyUse(kBtu)'] > Q3]

# Afficher les lignes dépassant le 3e quartile
# Obtenir un résumé statistique des valeurs dépassant le 3e quartile
print(valeurs_excedent_Q3['SiteEnergyUse(kBtu)'].describe())
print(valeurs_excedent_Q3.info())


# Le nombre de 411 valeurs est loin d'être négligeable, d'autant plus que cela représente environ le quart de notre jeu de données. La bonne nouvelle est qu'il n'y a pas de quantité d'énergie négative

# ## Observation des autres variables

# In[48]:


import matplotlib.pyplot as plt
import seaborn as sns

# Configuration des sous-graphiques
df_num = data.select_dtypes(exclude=['object'])
num_vars = len(df_num.columns)
cols_per_row = 3  # Nombre de colonnes par ligne
rows = (num_vars // cols_per_row) + (num_vars % cols_per_row > 0)

# Taille de la figure globale
fig, axes = plt.subplots(rows, cols_per_row, figsize=(15, 4 * rows))
axes = axes.flatten()  # Aplatir pour un accès facile

# Création des histogrammes et des courbes de densité
for i, col in enumerate(df_num.columns):
    sns.histplot(df_num[col], kde=True, ax=axes[i], color="royalblue")
    axes[i].set_title(f'Distribution de {col}', fontsize=12)
    axes[i].set_ylabel('Fréquence')
    axes[i].set_xlabel(col)

# Supprime les sous-graphiques vides
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

# Ajustements finaux
fig.tight_layout()
plt.show()


# 

# #### Normalisation des variables puis visualisation des distributions après application du logarithmique

# In[49]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler

# Sélectionner les variables numériques
df_num = data.select_dtypes(exclude=['object'])

# Normalisation des variables
scaler = StandardScaler()
df_num_normalized = pd.DataFrame(scaler.fit_transform(df_num), columns=df_num.columns)

# Application de la transformation logarithmique
df_num_log = df_num_normalized.apply(lambda x: np.log1p(x))  # log1p pour éviter log(0)

# Configuration des sous-graphiques
num_vars = len(df_num_log.columns)
cols_per_row = 3  # Nombre de colonnes par ligne
rows = (num_vars // cols_per_row) + (num_vars % cols_per_row > 0)

# Taille de la figure globale
fig, axes = plt.subplots(rows, cols_per_row, figsize=(15, 4 * rows))
axes = axes.flatten()  # Aplatir pour un accès facile

# Création des histogrammes et des courbes de densité
for i, col in enumerate(df_num_log.columns):
    sns.histplot(df_num_log[col], kde=True, ax=axes[i], color="royalblue")
    axes[i].set_title(f'Distribution de {col}', fontsize=12)
    axes[i].set_ylabel('Fréquence')
    axes[i].set_xlabel(col)

# Supprime les sous-graphiques vides
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

# Ajustements finaux
fig.tight_layout()
plt.show()


# ### Traitement des variables longitude et latitude

# Regardons à présent si les coordonnées géographiques ont un impact sur les  consommations. Pour cela, afin d'éviter les corrélations fortes entre Latitude et Longitude, nous allons calculer la distance Harversine entre chaque point de coordonnées et le centre de Seattle :

# In[50]:


from math import radians, cos, sin, asin, sqrt

#Coordonnées du centre de Seattle
seattle_lat = 47.6062
seattle_lon = -122.3321

def haversine_distance(lat1, lng1, lat2, lng2, degrees=True):
    r = 3956 # rayon de la Terre en miles
    
    if degrees:
        lat1, lng1, lat2, lng2 = map(radians, [lat1, lng1, lat2, lng2])
    
    # Formule Haversine
    dlng = lng2 - lng1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlng/2)**2
    d = 2 * r * asin(sqrt(a))  

    return d


# In[51]:


#Calcul des distance au centre de Seattle pour chaque point
data['harvesine_distance'] = [haversine_distance(seattle_lat, seattle_lon, x, y) 
                              for x, y in zip(data.Latitude.astype(float), data.Longitude.astype(float))]


# In[52]:


fig, axes = plt.subplots(nrows=1, ncols=2, sharex=False, sharey=False, figsize=(20,8))
sns.scatterplot(data=data, y="SiteEnergyUse(kBtu)", x="harvesine_distance", color="#6D9C0E", ax=axes[0])
axes[0].set_title("Données globales", color='#2cb7b0')
sns.histplot(data=data[(data['SiteEnergyUse(kBtu)'] < 2*10**8)], y="SiteEnergyUse(kBtu)", 
                x="harvesine_distance", color="#6D9C0E", ax=axes[1])
axes[1].set_title("Données zoomées", color='#2cb7b0')
font_title = {'fontsize': 22, 'fontweight': 'bold'} 
plt.suptitle("Répartition de la consommation d'energies en fonction des coordonnées géographiques", 
             fontdict=font_title)
plt.show()


# En regardant ces projections, il semble que les coordonnées géographiques (donc les adresses des bâtiments) puissent avoir un impact sur les consommations d'énergie.
# nous allons supprimer ces 2 colonnes pour conserver uniquement ce point de coordonnée unique Harvesine

# <h3 style="margin: auto; padding: 20px; color: RGB(51,165,182); "> Analyse exploratoire des variables qualitatives</h3>

# Sortons le nombre de modalités par variables catégorlelles.

# In[53]:


obj_columns = list(data.select_dtypes(include=['object', 'bool']).columns)
data[obj_columns].apply(lambda col: col.nunique())


# ## Recodage des variables catégorielles

# In[54]:


data["BuildingType"]=data["BuildingType"].replace(['Nonresidential WA','Nonresidential COS'],"NonResidential")


# In[55]:


data["BuildingType"].unique()


# In[56]:


# Transformons les modalités des variables catégorielles en majuscule pour éviter un double compte
for cat in data[obj_columns]:
    data[cat] = data[cat].apply(lambda x: str(x).upper())
data[obj_columns]


# In[57]:


# Redeterminons le nombre de modalités par variables
data[obj_columns].apply(lambda col: col.nunique())


# On remarque que le nombre de modalités de la variable Neighborhood a diminué. Faisons un focus sur ses modalités pour voir si elles ne nécessitent pas un recodage.

# In[58]:


data['Neighborhood'].unique()


# On peut remarquer que DELRIDGE NEIGHBORHOODS et DELRIDGE correspondent à la même modalité. Dans la suite, on remplace tous les DELRIDGE NEIGHBORHOODS par DELRIDGE.

# In[59]:


data['Neighborhood'] = data['Neighborhood'].replace('DELRIDGE NEIGHBORHOODS', 'DELRIDGE')
data['Neighborhood'].unique()


# In[60]:


# Nouvelles classes en anglais et en majuscules
new_classes = {
    'EDUCATION': ['K-12 SCHOOL', 'UNIVERSITY'],
    'HEALTH AND MEDICAL': ['SENIOR CARE COMMUNITY', 'HOSPITAL', 'MEDICAL OFFICE', 'LABORATORY'],
    'OFFICE AND BUSINESS': ['OFFICE', 'LARGE OFFICE', 'SMALL- AND MID-SIZED OFFICE'],
    'STORAGE': ['SELF-STORAGE FACILITY', 'WAREHOUSE', 'REFRIGERATED WAREHOUSE', 'DISTRIBUTION CENTER'],
    'RETAIL AND PERSONAL SERVICES': ['RETAIL STORE'],
    'HOTEL': ['HOTEL'],
    'RESIDENTIAL AND HOUSING': ['LOW-RISE MULTIFAMILY', 'RESIDENCE HALL'],
    'FOOD AND BEVERAGE': ['RESTAURANT', 'SUPERMARKET / GROCERY STORE'],
    'MIXED USE': ['MIXED USE PROPERTY'],
    'OTHER SERVICES AND FACILITIES': ['OTHER', 'WORSHIP FACILITY']
}

# Fonction pour mapper les classes
def map_class(category):
    for key, values in new_classes.items():
        if category in values:
            return key
    return 'UNDEFINED'

# Création de la PrimaryProperty en fonction de la PrimaryPropertyType
data['PrimaryProperty'] = data['PrimaryPropertyType'].apply(map_class)


# In[61]:


data['PrimaryProperty'].unique()


# In[62]:


data['SecondLargestPropertyUseType'].unique()


# In[63]:


new_classes = {
    'EDUCATION': ['K-12 SCHOOL', 'VOCATIONAL SCHOOL', 'COLLEGE/UNIVERSITY', 'ADULT EDUCATION', 'OTHER - EDUCATION', 'PRE-SCHOOL/DAYCARE'],
    'RETAIL AND PERSONAL SERVICES': ['RETAIL STORE', 'PERSONAL SERVICES (HEALTH/BEAUTY, DRY CLEANING, ETC)', 'CONVENIENCE STORE WITHOUT GAS STATION'],
    'ENTERTAINMENT AND LEISURE': ['OTHER - ENTERTAINMENT/PUBLIC ASSEMBLY', 'MOVIE THEATER', 'SWIMMING POOL', 'PERFORMING ARTS', 'BAR/NIGHTCLUB', 'SOCIAL/MEETING HALL'],
    'FOOD AND BEVERAGE': ['RESTAURANT', 'SUPERMARKET/GROCERY STORE', 'FOOD SALES', 'FOOD SERVICE', 'OTHER - RESTAURANT/BAR'],
    'HEALTH AND MEDICAL': ['MEDICAL OFFICE', 'LABORATORY', 'FITNESS CENTER/HEALTH CLUB/GYM'],
    'OFFICE AND BUSINESS': ['OFFICE', 'DATA CENTER', 'MANUFACTURING/INDUSTRIAL PLANT', 'BANK BRANCH', 'REPAIR SERVICES (VEHICLE, SHOE, LOCKSMITH, ETC)'],
    'RESIDENTIAL AND HOUSING': ['RESIDENCE HALL/DORMITORY', 'MULTIFAMILY HOUSING', 'OTHER - LODGING/RESIDENTIAL'],
    'STORAGE': ['SELF-STORAGE FACILITY', 'REFRIGERATED WAREHOUSE', 'NON-REFRIGERATED WAREHOUSE', 'DISTRIBUTION CENTER'],
    'OTHER SERVICES AND FACILITIES': ['OTHER', 'OTHER - SERVICES', 'OTHER - RECREATION', 'OTHER - PUBLIC SERVICES', 'ENCLOSED MALL', 'AUTOMOBILE DEALERSHIP', 'WORSHIP FACILITY'],
    'NOT CONCERNED': ['NOT CONCERNED'],
    'HOTEL': ['HOTEL'],
    'PARKING': ['PARKING']
}

# Fonction pour mapper les classes
def map_class(category):
    for key, values in new_classes.items():
        if category in values:
            return key
    return 'UNDEFINED'

# Création de la SecondLargest en fonction de la SecondLargestPropertyUseType
data['SecondLargest'] = data['SecondLargestPropertyUseType'].apply(map_class)


# In[64]:


data['SecondLargest'].unique()


# In[65]:


data['ThirdLargestPropertyUseType'].unique()


# In[66]:


# Nouvelles classes en anglais et en majuscules
new_classes = {
    'EDUCATION': ['K-12 SCHOOL', 'VOCATIONAL SCHOOL', 'COLLEGE/UNIVERSITY', 'ADULT EDUCATION', 'OTHER - EDUCATION', 'PRE-SCHOOL/DAYCARE'],
    'RETAIL AND PERSONAL SERVICES': ['RETAIL STORE', 'PERSONAL SERVICES (HEALTH/BEAUTY, DRY CLEANING, ETC)', 'CONVENIENCE STORE WITHOUT GAS STATION'],
    'ENTERTAINMENT AND LEISURE': ['SWIMMING POOL', 'OTHER - ENTERTAINMENT/PUBLIC ASSEMBLY', 'SOCIAL/MEETING HALL', 'BAR/NIGHTCLUB'],
    'FOOD AND BEVERAGE': ['RESTAURANT', 'FAST FOOD RESTAURANT', 'FOOD SERVICE', 'SUPERMARKET/GROCERY STORE'],
    'HEALTH AND MEDICAL': ['MEDICAL OFFICE', 'OTHER/SPECIALTY HOSPITAL', 'LABORATORY', 'FITNESS CENTER/HEALTH CLUB/GYM'],
    'OFFICE AND BUSINESS': ['OFFICE', 'DATA CENTER', 'FINANCIAL OFFICE', 'BANK BRANCH', 'MANUFACTURING/INDUSTRIAL PLANT'],
    'RESIDENTIAL AND HOUSING': ['MULTIFAMILY HOUSING'],
    'STORAGE': ['REFRIGERATED WAREHOUSE', 'NON-REFRIGERATED WAREHOUSE', 'DISTRIBUTION CENTER', 'SELF-STORAGE FACILITY'],
    'OTHER SERVICES AND FACILITIES': ['OTHER - SERVICES', 'OTHER - UTILITY', 'WORSHIP FACILITY', 'OTHER - RECREATION', 'OTHER - TECHNOLOGY/SCIENCE', 'OTHER', 'OTHER - RESTAURANT/BAR'],
    'HOTEL': ['HOTEL'],
    'PARKING': ['PARKING'],
    'NOT CONCERNED': ['NOT CONCERNED']
}

# Fonction pour mapper les classes
def map_class(category):
    for key, values in new_classes.items():
        if category in values:
            return key
    return 'UNDEFINED'

# Création de la ThirdLargest en fonction de la ThirdLargestPropertyUseType
data['ThirdLargest'] = data['ThirdLargestPropertyUseType'].apply(map_class)


# In[67]:


data['ThirdLargest'].unique()


# Correlation entre les variables qualitatives

# In[68]:


# Sélectionnez uniquement les colonnes catégorielles
data_cat = data.select_dtypes(include=['object', 'category'])

# Créez une fonction pour calculer le V de Cramer
def cramers_v(x, y):
    confusion_matrix = pd.crosstab(x, y)
    chi2, _, _, _ = chi2_contingency(confusion_matrix)
    n = confusion_matrix.sum().sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k - 1) * (r - 1)) / (n - 1))
    rcorr = r - ((r - 1)  * 2) / (n - 1)
    kcorr = k - ((k - 1) * 2) / (n - 1)
    return np.sqrt(phi2corr / min((kcorr - 1), (rcorr - 1)))

# Créez un DataFrame pour stocker les résultats du V de Cramer
cramers_v_results = pd.DataFrame(index=data_cat.columns, columns=data_cat.columns)

# Calculer le V de Cramer pour chaque paire de variables catégorielles
for col1 in data_cat.columns:
    for col2 in data_cat.columns:
        if col1 != col2:
            v_cramer = cramers_v(data_cat[col1], data_cat[col2])
            cramers_v_results.loc[col1, col2] = v_cramer

# Convertir les valeurs de V de Cramer en nombres flottants
cramers_v_results = cramers_v_results.astype(float)

# Créer un heatmap des valeurs de V de Cramer
plt.figure(figsize=(10, 8))
sns.heatmap(cramers_v_results, annot=True, cmap="YlGnBu")
plt.title("Heatmap des valeurs de V de Cramer entre les variables catégorielles")
plt.show()


# <h2 style="margin: auto; padding: 20px; font-size: 40px;color: RGB(51,165,182); "> Feature Engineering</h2>

# ### Transformation de la variable yearBuilt en nombre d'années

# Representation de la distribution de la variable

# In[69]:


font_title = {'family': 'serif',
              'color':  '#1d479b',
              'weight': 'bold',
              'size': 18,
             }

fig = plt.figure(figsize=(12,8))
ax = sns.histplot(data=data, x='YearBuilt', bins=int((data.YearBuilt.max() - data.YearBuilt.min())/5))
ax.set_xlabel("Année de construction")
ax.set_ylabel("Nombre de bâtiments")
plt.title(f"Distribution des années de construction des bâtiments\n", fontdict=font_title)
plt.show()


# Il serait intéressant de traiter l'**age des bâtiments** pour réduire la dispersion des données et lier l'année des relevés(consommation d'electricité, de gaz et autres). Nous allons donc créer cette nouvelle variable et supprimer l'année de construction :

# In[70]:


data['BuildingAge'] = 2016 - data['YearBuilt']
data.drop('YearBuilt', axis=1, inplace=True)

fig = plt.figure(figsize=(12,8))
ax = sns.histplot(data=data, x='BuildingAge', bins=int((data.BuildingAge.max() - data.BuildingAge.min())/5))
ax.set_xlabel("Age du bâtiment")
ax.set_ylabel("Nombre de bâtiments")
plt.title(f"Distribution de l'âge des bâtiments\n", fontdict=font_title)
plt.show()


# <h3 style="margin: auto; padding: 20px; color: RGB(51,165,182); "> Selection des variables </h3>

# In[71]:


print(data.columns)


# In[72]:


var_model = ['OSEBuildingID', 'BuildingType', 'Neighborhood', 'BuildingAge', 'NumberofBuildings', 
        'NumberofFloors', 'PropertyGFAParking', 'PropertyGFABuilding(s)',
       'PrimaryProperty', 'LargestPropertyUseTypeGFA',
       'SecondLargest', 'SecondLargestPropertyUseTypeGFA',
       'ThirdLargest', 'ThirdLargestPropertyUseTypeGFA','NumberPropertyUseType', 'harvesine_distance', 'BuildingAge',
        'ENERGYSTARScore','SiteEnergyUse(kBtu)'
       ]


# In[73]:


data_final = data.filter(var_model)


# In[75]:


data_final.to_csv(Path(DATA_DIR, "data_clean.csv"), index=False)


# ## <font color="#337da4" id="section_4">Projection des établissements sur la carte de Seattle</font>

# In[ ]:


##pip install folium


# In[76]:


import folium
import folium.plugins

seattle_map = folium.Map(location=[seattle_lat, seattle_lon], zoom_start=11)

#Clusters
marker_cluster = folium.plugins.MarkerCluster().add_to(seattle_map)
for lat, lng, in zip(data.Latitude, data.Longitude):
    folium.Marker(location=[lat, lng]).add_to(marker_cluster)

seattle_map


# In[ ]:




