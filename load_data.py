import pandas as pd
import numpy as np
import os
import warnings

def load_data():
    file_path = "/home/shosh/Desktop/NTI projects /Mall_Customers/Mall_Customers.csv"
    
    if os.path.exists(file_path):
        data = pd.read_csv(file_path)
    else:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    
    warnings.simplefilter(action='ignore', category=FutureWarning)
    warnings.simplefilter(action='ignore', category=UserWarning)

    data.replace([np.inf, -np.inf], np.nan, inplace=True)

    return data

def preprocess_data(data):
    data['Genre'].fillna(data['Genre'].mode()[0], inplace=True)
    data.drop('CustomerID', axis=1, inplace=True)
    return data
