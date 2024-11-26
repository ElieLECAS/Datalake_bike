from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta
import os

# Informations de base
account_name = "datalakedeviavals"
account_key = "Di7GZT/MHmRkRD6UTcIZmjnuWWhye/yvN2nFUTrgP380meAg4ggupT8RBGmL3IFnoI6aTqam3WFe+AStF56q9g=="
container_name = "datalakedeviavals"
blob_name = "data"

# Durée de validité du SAS
expiry_time = datetime.utcnow() + timedelta(hours=1)  # Expire dans 1 heure

# Permissions SAS
permissions = BlobSasPermissions(read=True, write=True, delete=True, list=True)

# Génération du SAS
sas_token = generate_blob_sas(
    account_name=account_name,
    container_name=container_name,
    blob_name=blob_name,  # Supprimez cette ligne si vous générez un SAS pour un conteneur
    account_key=account_key,
    permission=permissions,
    expiry=expiry_time
)

# URL avec SAS
blob_url_with_sas = f"https://{account_name}.blob.core.windows.net/{container_name}/{blob_name}?{sas_token}"

# Résultat
print("SAS Token:", sas_token)
print("Blob URL with SAS:", blob_url_with_sas)


# Remplacez par vos informations
account_name = "datalakedeviavals"
container_name = "data"

# Créer une connexion BlobServiceClient
blob_service_client = BlobServiceClient(
    f"https://{account_name}.blob.core.windows.net",
    credential=account_key
)

# Accéder à un conteneur
container_client = blob_service_client.get_container_client(container_name)

print(f"Connexion réussie au conteneur {container_name}.")

# Liste des blobs (fichiers) dans le conteneur
print("Blobs disponibles :")
for blob in container_client.list_blobs():
    print(blob.name)

# Créer une connexion BlobServiceClient
connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Accéder à un conteneur
container_client = blob_service_client.get_container_client(container_name)

print(f"Connexion réussie au conteneur {container_name}.")

# Chemin du dossier local où les fichiers seront sauvegardés
local_folder = "./downloads"
os.makedirs(local_folder, exist_ok=True)

# Liste et téléchargement des blobs
print("Téléchargement des blobs disponibles :")
for blob in container_client.list_blobs():
    blob_name = blob.name
    local_file_path = os.path.join(local_folder, blob_name)

    # Vérifiez si un fichier ou un répertoire existe déjà
    parent_dir = os.path.dirname(local_file_path)
    if os.path.exists(parent_dir):
        if os.path.isfile(parent_dir):
            # Si un fichier existe avec le même nom, le supprimer
            os.remove(parent_dir)

    # Créez les répertoires nécessaires
    os.makedirs(parent_dir, exist_ok=True)

    # Télécharger le blob
    with open(local_file_path, "wb") as file:
        blob_data = container_client.download_blob(blob_name)
        file.write(blob_data.readall())

    print(f"Blob '{blob_name}' téléchargé dans '{local_file_path}'.")

print("Tous les blobs ont été téléchargés avec succès.")