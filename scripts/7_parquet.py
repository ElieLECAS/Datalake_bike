import os
import base64
from PIL import Image
import io
import pandas as pd
import os

input_dir = "downloads/product_eval/"

dataframes = {}

for i, file_name in enumerate(os.listdir(input_dir), start=1):
    count = 1
    if file_name.endswith(".parquet"):
        file_path = os.path.join(input_dir, file_name)
        print(f"Chargement du fichier : {file_path}")
        
        df = pd.read_parquet(file_path)

        dataframes[f"df{i}"] = df

df1 = dataframes["df1"]
df2 = dataframes["df2"]
df3 = dataframes["df3"]

df1 = df1
df2 = df2
df3 = df3

output_dir = "images_output/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

csv_file_path = os.path.join(output_dir, "metadata.csv")
df_combined = pd.concat([df1, df2, df3], ignore_index=True)

df_combined = df_combined.head(1000)


for index, row in df_combined.iterrows():
    # Récupérer l'image encodée (Base64 ou bytes)
    image_data = row['image']['bytes']
    
    # Utiliser la valeur de la colonne 'item_ID' pour nommer les fichiers
    item_id = row['item_ID']
    file_name = f"{item_id}.png"
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
        print(f"Erreur pour l'item_ID {item_id} à l'index {index}: {e}")

# Sauvegarde en CSV

df_combined.drop(columns=['image'], inplace=True)

df_combined.to_csv(csv_file_path, index=False, sep=',', encoding='utf-8')