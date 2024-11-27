python3 -m venv venv
source venv/bin/activate
pip install -r scripts/requirements.txt

/home/elie/Documents/Code/Briefs/Datalake_bike/venv/bin/python scripts/3_db.py
/home/elie/Documents/Code/Briefs/Datalake_bike/venv/bin/python scripts/4_downloads.py
/home/elie/Documents/Code/Briefs/Datalake_bike/venv/bin/python scripts/5_unzip.py
/home/elie/Documents/Code/Briefs/Datalake_bike/venv/bin/python scripts/6_keep_csv.py
/home/elie/Documents/Code/Briefs/Datalake_bike/venv/bin/python scripts/7_parquet.py

rm -r -f downloads/