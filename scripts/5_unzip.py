import os
import zipfile
import tarfile
import gzip
import shutil

# Dossier contenant les fichiers ZIP téléchargés
downloads_folder = "downloads/machine_learning"

# Dossier de sortie contenant les fichiers dézippés
unzipped_folder = "./machine_learning_unzipped"

# Créez le dossier pour les fichiers extraits si nécessaire
os.makedirs(unzipped_folder, exist_ok=True)

# Fonction pour extraire les fichiers TAR, TGZ et GZ
def extract_tar_gz(file_path, extract_to):
    try:
        # Extraction des fichiers TAR et TGZ
        with tarfile.open(file_path, 'r:*') as tar_ref:
            tar_ref.extractall(extract_to)
            print(f"Fichier TAR/TGZ '{file_path}' extrait dans '{extract_to}'.")
        # Supprimer l'archive une fois extraite
        os.remove(file_path)
        print(f"Fichier '{file_path}' supprimé après extraction.")
    except tarfile.TarError as e:
        print(f"Erreur lors de l'extraction de '{file_path}': {e}")

def extract_gz(file_path, extract_to):
    try:
        # Extraction des fichiers GZ
        with gzip.open(file_path, 'rb') as f_in:
            with open(extract_to, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
            print(f"Fichier GZ '{file_path}' extrait dans '{extract_to}'.")
        # Supprimer le fichier GZ une fois extrait
        os.remove(file_path)
        print(f"Fichier '{file_path}' supprimé après extraction.")
    except Exception as e:
        print(f"Erreur lors de l'extraction de '{file_path}': {e}")

# Parcourir tous les fichiers dans le dossier des téléchargements
print("Extraction des fichiers ZIP et autres archives :")
for root, dirs, files in os.walk(downloads_folder):
    for file in files:
        if file.endswith(".zip"):
            zip_file_path = os.path.join(root, file)
            extract_path = os.path.join(unzipped_folder, os.path.splitext(file)[0])
            os.makedirs(extract_path, exist_ok=True)

            try:
                # Extraire le fichier ZIP
                with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_path)
                    print(f"Fichier ZIP '{file}' extrait dans '{extract_path}'.")

                    
                    for zip_file in zip_ref.namelist():
                        if zip_file.endswith(('.tgz', '.tar', '.gz')):
                            inner_file_path = os.path.join(extract_path, zip_file)
                            # Si c'est un fichier .tar ou .tgz
                            if zip_file.endswith(('.tgz', '.tar')):
                                extract_tar_gz(inner_file_path, extract_path)
                            # Si c'est un fichier .gz
                            elif zip_file.endswith('.gz'):
                                extract_gz(inner_file_path, os.path.join(extract_path, zip_file[:-3]))
            except zipfile.BadZipFile:
                print(f"Le fichier '{file}' n'est pas un fichier ZIP valide.")

print("Extraction terminée.")
