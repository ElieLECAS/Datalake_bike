import os
import base64
from PIL import Image
import io
import pandas as pd
import os

# Chemin du dossier contenant les fichiers Parquet
input_dir = "downloads/product_eval/"

# Dictionnaire pour stocker les DataFrames
dataframes = {}

# Parcourir tous les fichiers dans le dossier
for i, file_name in enumerate(os.listdir(input_dir), start=1):
    count = 1
    if file_name.endswith(".parquet"):
        file_path = os.path.join(input_dir, file_name)
        print(f"Chargement du fichier : {file_path}")
        
        # Charger le fichier Parquet
        df = pd.read_parquet(file_path)

        # Ajouter le DataFrame au dictionnaire avec un nom dynamique
        dataframes[f"df{i}"] = df

# Chemin de sortie pour enregistrer les images
output_dir = "images_output/1/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)



df1 = dataframes["df1"]
df2 = dataframes["df2"]
df3 = dataframes["df3"]

    
for index, row in df1.iterrows():
    # Récupérer l'image encodée (Base64 ou bytes)
    image_data = row['image']['bytes']
    
    # Créer un nom de fichier basé sur l'index ou une autre colonne
    file_name = f"image_{index}.png"
    file_path = os.path.join(output_dir, file_name)

    try:
        # Si l'image est encodée en Base64, la décoder
        if isinstance(image_data, str):  # Vérifie si l'image est encodée en base64
            image_data = base64.b64decode(image_data)
        
        # Ouvrir l'image et la sauvegarder
        image = Image.open(io.BytesIO(image_data))
        image.save(file_path, format="PNG")
        print(f"Image sauvegardée : {file_path}")
    except Exception as e:
        print(f"Erreur pour l'index {index}: {e}")

output_dir = "images_output/2/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
for index, row in df2.iterrows():
    # Récupérer l'image encodée (Base64 ou bytes)
    image_data = row['image']['bytes']
    
    # Créer un nom de fichier basé sur l'index ou une autre colonne
    file_name = f"image_{index}.png"
    file_path = os.path.join(output_dir, file_name)

    try:
        # Si l'image est encodée en Base64, la décoder
        if isinstance(image_data, str):  # Vérifie si l'image est encodée en base64
            image_data = base64.b64decode(image_data)
        
        # Ouvrir l'image et la sauvegarder
        image = Image.open(io.BytesIO(image_data))
        image.save(file_path, format="PNG")
        print(f"Image sauvegardée : {file_path}")
    except Exception as e:
        print(f"Erreur pour l'index {index}: {e}")

output_dir = "images_output/3/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
for index, row in df3.iterrows():
    # Récupérer l'image encodée (Base64 ou bytes)
    image_data = row['image']['bytes']
    
    # Créer un nom de fichier basé sur l'index ou une autre colonne
    file_name = f"image_{index}.png"
    file_path = os.path.join(output_dir, file_name)

    try:
        # Si l'image est encodée en Base64, la décoder
        if isinstance(image_data, str):  # Vérifie si l'image est encodée en base64
            image_data = base64.b64decode(image_data)
        
        # Ouvrir l'image et la sauvegarder
        image = Image.open(io.BytesIO(image_data))
        image.save(file_path, format="PNG")
        print(f"Image sauvegardée : {file_path}")
    except Exception as e:
        print(f"Erreur pour l'index {index}: {e}")