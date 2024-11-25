import os
import pandas as pd
from sqlalchemy import create_engine
import pyodbc
from dotenv import load_dotenv

load_dotenv()

# Récupérer les informations d'identification
server = os.getenv('DB_SERVER')
database = os.getenv('DB_NAME')
username = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
driver = os.getenv('DRIVER')

# Connexion à la base de données
conn = pyodbc.connect(
    f'DRIVER={{{driver}}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
)

# Requête pour récupérer les noms des tables
query_tables = """
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE'
"""

# Exécuter la requête et charger les résultats dans un DataFrame
df_tables = pd.read_sql(query_tables, conn)

# Nom de la table à charger
nom_table = "Person.PhoneNumberType"

query = f"SELECT * FROM {nom_table}"
df = pd.read_sql(query, conn)

output_dir = 'csv'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Récupérer la liste des tables
query_tables = """
SELECT TABLE_SCHEMA + '.' + TABLE_NAME AS FullTableName
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE'
"""
df_tables = pd.read_sql(query_tables, conn)

# Boucle sur les tables pour sauvegarder en CSV
for index, row in df_tables.iterrows():
    table_name = row['FullTableName']
    try:
        # Charger les données de la table dans un DataFrame
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, conn)
        
        # Nom du fichier CSV
        file_name = f"{table_name.replace('.', '_')}.csv"
        file_path = os.path.join(output_dir, file_name)
        
        # Sauvegarder en CSV
        df.to_csv(file_path, index=False, sep=';', encoding='utf-8')
        print(f"Table {table_name} exportée avec succès dans {file_path}")
    except Exception as e:
        print(f"Erreur lors de l'exportation de la table {table_name} : {e}")

# Fermer la connexion
conn.close()