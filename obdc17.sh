source venv/bin/activate
# Ajouter le dépôt Microsoft
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list

# Mettre à jour et installer le pilote ODBC
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y unixodbc unixodbc-dev
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17
