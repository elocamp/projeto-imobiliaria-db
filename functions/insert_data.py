import sqlite3

def add_cliente(database_name: str, numero_ap: int, cliente_nome: str, cliente_sobrenome: str, cliente_cpf: str, cliente_telefone: str):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    
    cursor.execute("""
                   INSERT INTO clientes (numero_ap, nome, sobrenome, cpf, telefone) VALUES (?, ?, ?, ?, ?)
                   """, (numero_ap, cliente_nome, cliente_sobrenome, cliente_cpf, cliente_telefone))
    
    connection.commit()
    connection.close()
    
def add_apartamento(database_name: str, numero_ap: int, apartamento_andar: int, apartamento_bloco: chr, apartamento_valor: float):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    
    cursor.execute("""
                   INSERT INTO apartamentos (numero_ap, andar, bloco, valor) VALUES (?, ?, ?, ?)
                   """, (numero_ap, apartamento_andar, apartamento_bloco, apartamento_valor))
    
    connection.commit()
    connection.close()
    
def add_vaga(database_name: str, numero_ap: int, vaga_placa_carro: str, vaga_marca_carro: str, vaga_modelo_carro: str, vaga_cor_carro: str):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    
    cursor.execute("""
                   INSERT INTO vagas_garagem (numero_ap, placa_carro, marca_carro, modelo_carro, cor_carro) VALUES (?, ?, ?, ?, ?)
                   """, (numero_ap, vaga_placa_carro, vaga_marca_carro, vaga_modelo_carro, vaga_cor_carro))
    
    connection.commit()
    connection.close()