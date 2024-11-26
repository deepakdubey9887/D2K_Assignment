import os
import sqlite3
import pandas as pd

def load_to_sqlite(db_file, inputdata):
    db_dir = os.path.dirname(db_file)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)

    # Connect to the SQLite database (file will be created if it doesn't exist)
    conn = sqlite3.connect(db_file)
    # Load the processed data
    df = inputdata.copy()
    df.to_sql('trips', conn, if_exists='append', index=False)
    conn.commit()
    conn.close()
    print(f"Data successfully loaded into {db_file}")