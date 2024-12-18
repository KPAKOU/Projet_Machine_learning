from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib

# Charger les modèles enregistrés
random_model = joblib.load("random_best_model.pkl")

# Initialiser l'application FastAPI
app = FastAPI(title="API de Prédiction de Consommation d'Énergie")


# Classes pour les données d'entrée
class RandomModelInput(BaseModel):
    BuildingType: str
    Neighborhood: str
    PrimaryProperty: str
    SecondLargest: str
    ThirdLargest: str
    NumberofBuildings: float
    ThirdLargestPropertyUseTypeGFA: float
    PropertyGFAParking: float
    PropertyGFABuilding: float
    NumberPropertyUseType: float
    LargestPropertyUseTypeGFA: float
    SecondLargestPropertyUseTypeGFA: float
    NumberofFloors: float
    harvesine_distance: float
    ENERGYSTARScore: float

# Route pour le modèle random_best_model.pkl
@app.post("/prediction/random_model/")
def predict_random_model(data: RandomModelInput):
    try:
        # Convertir les données en DataFrame
        input_data = pd.DataFrame([data.dict()])
        
        # Prédiction avec le modèle Random Forest
        log_prediction = random_model.predict(input_data)[0]
        prediction = np.exp(log_prediction)  # Appliquer l'exponentielle à la variable cible
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la prédiction : {str(e)}")
   
    return {
        "La prédiction": prediction
        }
