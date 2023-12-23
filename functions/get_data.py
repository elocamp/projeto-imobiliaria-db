import sqlite3
import pandas as pd

def get_table(database_name, table_name):
    conn = sqlite3.connect(database_name)
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    return df

def get_data_cliente(database_name, numero_ap):
    conn = sqlite3.connect(database_name)
    query = f"SELECT * FROM clientes WHERE numero_ap = {numero_ap}"
    df = pd.read_sql_query(query, conn)
        
    conn.close()
    
    return df

def get_data_apartamento(database_name, numero_ap):
    conn = sqlite3.connect(database_name)
    query = f"SELECT * FROM apartamentos WHERE numero_ap = {numero_ap}"
    df = pd.read_sql_query(query, conn)
        
    conn.close()
    
    return df

def get_data_vaga(database_name, numero_ap):
    conn = sqlite3.connect(database_name)
    query = f"SELECT * FROM vagas_garagem WHERE numero_ap = {numero_ap}"
    df = pd.read_sql_query(query, conn)
        
    conn.close()
    
    return df