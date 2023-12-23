import sqlite3

def delete_cliente(database_name: str, numero_ap: int):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM clientes WHERE numero_ap = {numero_ap}")

    conn.commit()
    conn.close()
    
def delete_apartamento(database_name: str, numero_ap: int):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM apartamentos WHERE numero_ap = {numero_ap}")

    conn.commit()
    conn.close()

def delete_vaga_garagem(database_name: str, numero_ap: int):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM vagas_garagem WHERE numero_ap = {numero_ap}")

    conn.commit()
    conn.close()