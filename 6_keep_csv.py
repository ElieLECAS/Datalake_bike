import os
import shutil

# Dossier source (où se trouvent les fichiers et sous-dossiers)
source_folder = "./downloads/nlp_data"

# Dossier cible pour la copie du contenu
target_folder = "./nlp_data_csv"
os.makedirs(target_folder, exist_ok=True)

# Parcourir récursivement le dossier source
for root, dirs, files in os.walk(source_folder):
    # Calculer le chemin relatif du dossier actuel par rapport au dossier source
    relative_path = os.path.relpath(root, source_folder)
    
    # Créer les sous-dossiers correspondants dans le dossier cible
    target_subfolder = os.path.join(target_folder, relative_path)
    os.makedirs(target_subfolder, exist_ok=True)
    
    for file in files:
        source_file_path = os.path.join(root, file)  # Chemin complet du fichier source
        target_file_path = os.path.join(target_subfolder, file)  # Chemin cible
        
        if file.endswith(".xlsx") or file.endswith(".xls"):
            # Supprimer les fichiers Excel
            os.remove(source_file_path)
            print(f"Supprimé : {source_file_path}")
        elif file.endswith(".csv"):
            # Copier les fichiers CSV dans le dossier cible
            shutil.copy2(source_file_path, target_file_path)
            print(f"Copié : {source_file_path} → {target_file_path}")

print("Processus terminé : fichiers Excel supprimés et fichiers CSV copiés.")
