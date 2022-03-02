import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# 1. Prep Iris Data

def prep_iris(iris):
    iris = iris.drop(['species_id', 'measurement_id'], axis = 1)
    iris = iris.rename(columns={'species_name': 'species'})
    dummy_iris = pd.get_dummies(iris[['species']], dummy_na = False, drop_first=True)
    iris = pd.concat([iris, dummy_iris], axis = 1)
    return iris

# 2. Prep Titanic Data

def prep_titanic(titanic):
    titanic.drop_duplicates(inplace= True)
    columns_to_drop = ['deck', 'age', 'embarked', 'class', 'passenger_id']
    titanic = titanic.drop(columns = columns_to_drop)
    titanic['embark_town'] = titanic.embark_town.fillna('Southampton')
    dummy_titanic = pd.get_dummies(titanic[['sex', 'embark_town']], 
                         dummy_na = False, 
                         drop_first = [True, True])
    titanic = pd.concat([titanic, dummy_titanic], axis = 1)
    return titanic.drop(columns=['sex', 'embark_town'])

# 3. Prep Telco Data

# Extra step: Create function that splits the data

def split_telco_data(telco):
    train_validate, test = train_test_split(telco, test_size=.2,
                                       random_state=123,
                                       stratify=telco.churn)
    train, validate = train_test_split(train_validate, test_size=.3,
                                  random_state=123,
                                  stratify=train_validate.churn)
    return train, validate, test


def prep_telco(telco):
    telco.drop_duplicates(inplace = True)
    telco['total_charges'] = telco['total_charges'].str.strip()
    telco = telco[telco.total_charges != '']
    telco['total_charges'] = telco.total_charges.astype(float)
    columns_to_drop = ['customer_id', 'streaming_tv', 'streaming_movies', 'online_security', 'online_backup', 
                       'device_protection', 'tech_support', 'contract_type_id', 'payment_type_id', 
                       'internet_service_type_id']
    telco = telco.drop(columns = columns_to_drop)
    telco['partner'] = telco.partner.map({'Yes': 1, 'No': 0})
    telco['dependents'] = telco.dependents.map({'Yes': 1, 'No': 0})
    telco['phone_service'] = telco.phone_service.map({'Yes': 1, 'No': 0})
    telco['paperless_billing'] = telco.paperless_billing.map({'Yes': 1, 'No': 0})
    telco['churn'] = telco.churn.map({'Yes': 1, 'No': 0})
    dummy_telco = pd.get_dummies(telco[['gender','contract_type', 'payment_type', 'internet_service_type']], 
                         dummy_na = False, 
                         drop_first = [True, True])
    telco = pd.concat([telco, dummy_telco], axis = 1)
    telco = telco.drop(columns= ['gender', 'contract_type', 'payment_type', 'internet_service_type'])
    
    #Split the data using other function
    train, validate, test = split_telco_data(telco)
    
    return train, validate, test

# Stand alone data splitting function

def train_validate_test_split(df, target, seed=123):
    train_validate, test = train_test_split(df, test_size=0.2, random_state=seed, stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, random_state=seed, stratify=train_validate[target])
    return train, validate, test
