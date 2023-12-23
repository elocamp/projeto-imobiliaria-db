import sqlite3

def create_table_clientes(database_name: str):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS clientes (
                       numero_ap INTEGER PRIMARY KEY,
                       nome TEXT NOT NULL,
                       sobrenome TEXT NOT NULL,
                       cpf TEXT NOT NULL,
                       telefone TEXT
                   )"""
                   )
    connection.close()

def create_table_apartamentos(database_name: str):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS apartamentos (
                       numero_ap INTEGER PRIMARY KEY,
                       andar INTEGER NOT NULL,
                       bloco CHARACTER,
                       valor FLOAT NOT NULL
                   )"""
                   )
    connection.close()

def create_table_vagas_garagem(database_name: str):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS vagas_garagem (
                       numero_ap INTEGER PRIMARY KEY,
                       placa_carro TEXT NOT NULL,
                       marca_carro TEXT,
                       modelo_carro TEXT,
                       cor_carro TEXT NOT NULL
                   )"""
                   )
    connection.close()

create_table_clientes('dados_imobiliaria.db')
create_table_apartamentos('dados_imobiliaria.db')
create_table_vagas_garagem('dados_imobiliaria.db')