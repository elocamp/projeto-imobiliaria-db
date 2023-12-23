import sqlite3

def create_db(database_name: str):
    sqlite3.connect(database_name)

# create_db('dados_imobiliaria.db')