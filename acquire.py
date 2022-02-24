from env import host, user, password, get_db_url
import pandas as pd 
import numpy as np
import os

# 1.

def get_titanic_data():
    filename = 'titanic.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        print('Retrieving data from mySQL server...')
        df = pd.read_sql('SELECT * FROM passengers;', get_db_url('titanic_db'))
        print('Caching data as csv file for future use...')
        df.to_csv(filename)
        return df

# 2. 

def get_iris_data():
    filename = 'iris.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        print('Retrieving data from mySQL server...')
        df = pd.read_sql('''
        SELECT * FROM measurements 
        JOIN species USING(species_id);''' , get_db_url('iris_db'))
        print('Caching data as csv file for future use...')
        df.to_csv(filename)
        return df

# 3.

def get_telco_data():
    filename = 'telco.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        print('Retrieving data from mySQL server...')
        df = pd.read_sql('''
        SELECT * FROM customers
        JOIN contract_types USING (contract_type_id)
        JOIN payment_types USING (payment_type_id)
        JOIN internet_service_types USING (internet_service_type_id);''' , get_db_url('telco_churn'))
        print('Caching data as csv file for future use...')
        df.to_csv(filename)
        return df

# 4. All work for this exercise already included in previous exercises

