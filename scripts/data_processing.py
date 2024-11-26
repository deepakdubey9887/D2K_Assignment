import os
import pandas as pd


def clean_and_transform(inputdata):
    """Clean and transform raw data."""
    df = inputdata.copy()
    
    # Remove invalid data
    df = df.dropna(subset=['VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime', 'fare_amount', 'trip_distance'])
    df = df[df['fare_amount'] > 0]
    df = df[df['trip_distance'] > 0]
    df = df[df['passenger_count'] > 0]
    # Convert datetime
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
    df['date'] = df['tpep_pickup_datetime'].dt.date
    # pickupdate date >=2019 as found some few data points are backdated and less then 2025 to inculde data till 2024
    df = df[(df['tpep_pickup_datetime'].dt.year >= 2019) & (df['tpep_pickup_datetime'].dt.year < 2025)]
    # Derive new columns
    df['trip_duration'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60
    df = df[df['trip_duration'] > 0]
    df['average_speed'] = df['trip_distance'] / (df['trip_duration'] / 60)
    # Reset index and rename ID
    df = df.reset_index()   
    df = df.rename(columns={"index": "ID"})

    return df  


def process_all_files(RAW_DATA_DIR,PROCESSED_DATA_DIR):
    """Process all raw data files."""
    print(RAW_DATA_DIR,"procesed")
    data = pd.read_parquet(RAW_DATA_DIR)
    df = clean_and_transform(data)
    return df


