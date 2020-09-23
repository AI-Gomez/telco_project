### Make a new python module, acquire.py to hold the following 
#data aquisition functions:

import pandas as pd
import os
from env import host, password, user 

def get_connection(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

# 1. get_titanic_data: returns the titanic data from the codeup data science database as a pandas data frame.
def get_titanic_data():
    filename = 'titanic.csv'
    if os.path.isfile(filename):
        df = pd.read_csv(filename, index_col=0)
        return df
    else:
        df = pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))
        df.to_csv(filename)
        return df
    
# 2. get_iris_data: returns the data from the iris_db on the codeup data science database as a pandas data frame. 
# The returned data frame should include the actual name of the species in addition to the species_ids.
def get_iris_data():
    filename = 'iris.csv'
    if os.path.isfile(filename):
        df = pd.read_csv(filename, index_col=0)
        return df
    else:
        df = pd.read_sql('select * from measurements join species using (species_id);', get_connection('iris_db'))
        df.to_csv(filename)
        return df

def telco_cust():
    sql_query = '''
    select * from customers as c
join internet_service_types as ist on ist.internet_service_type_id = c.internet_service_type_id
join contract_types as cs on cs.contract_type_id = c.contract_type_id
join payment_types as pt on pt.payment_type_id = c.payment_type_id
    '''
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    return df 

def telco_cust1():
    df1 = pd.read_sql(get_connection('telco_churn'))
    return df1 