# Load dependencies
import json
import pandas as pd
import numpy as np

def loadJson(filename):
    #Declare the path of the data file
    file_to_load = f"Data/{filename}"
    #Read the data file
    with open(file_to_load, mode='r') as file:
        result = json.load(file)
    
    #Return result
    return result

def loadCsv(filename):
    #Declare the path of the data file
    file_to_load = f"Data/{filename}"
    
    # Load kaggle data files    
    result = pd.read_csv(file_to_load, low_memory=False)
        
    #Return result
    return result

def loadDataFile(filename):
    # Determine data type
    if '.csv' in  filename:
        result = loadCsv(filename)
        return result
    elif '.json' in filename:
        result = loadJson(filename)
        return result
    else: 
        print("Data type not supported/found!")
    