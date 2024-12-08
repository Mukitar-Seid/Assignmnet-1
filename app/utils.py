import pandas as pd

def load_data():
    df1 = pd.read_csv('../data/benin-malanville.csv')
    df2 = pd.read_csv('../data/sierraleone-bumbuna.csv')
    df3 = pd.read_csv('../data/togo-dapaong_qc.csv')
    
    # Combine data if necessary.
    data = pd.concat([df1, df2, df3], ignore_index=True)
    
    # Convert Timestamp to datetime format if not already done.
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    
    return data
