bash scripts/1_pip_venv.sh
bash scripts/2_curl_odbc.sh

/home/elie/Documents/Code/Briefs/Datalake_bike/venv/bin/python scripts/3_db.py
/home/elie/Documents/Code/Briefs/Datalake_bike/venv/bin/python scripts/4_downloads.py
/home/elie/Documents/Code/Briefs/Datalake_bike/venv/bin/python scripts/5_unzip.py
/home/elie/Documents/Code/Briefs/Datalake_bike/venv/bin/python scripts/6_keep_csv.py
/home/elie/Documents/Code/Briefs/Datalake_bike/venv/bin/python scripts/7_parquet.py

rm -r -f downloads/