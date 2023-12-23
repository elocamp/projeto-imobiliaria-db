import sqlite3
import pandas as pd

def join_table_clientes_apartamentos(database_nome, numero_ap):
    conn = sqlite3.connect(database_nome)

    conn.execute(f"ATTACH DATABASE clientes AS apartamentos")

    query = f"""
        SELECT * FROM clientes
        LEFT JOIN apartamentos ON clientes.numero_ap = apartamentos.numero_ap
        WHERE clientes.numero_ap = {numero_ap}
    """

    result = pd.read_sql_query(query, conn)

    conn.close()

    return result

def join_table_clientes_vagas_garagem(database_nome, numero_ap):
    conn = sqlite3.connect(database_nome)

    conn.execute(f"ATTACH DATABASE clientes AS vagas_garagem")

    query = f"""
        SELECT * FROM clientes
        LEFT JOIN vagas_garagem ON clientes.numero_ap = vagas_garagem.numero_ap
        WHERE clientes.numero_ap = {numero_ap}
    """

    result = pd.read_sql_query(query, conn)

    conn.close()

    return result

def join_all_tables(database_nome):
    conn = sqlite3.connect(database_nome)

    conn.execute(f"ATTACH DATABASE clientes AS apartamentos")
    conn.execute(f"ATTACH DATABASE clientes AS vagas_garagem")

    query = f"""
        SELECT * FROM clientes
        LEFT JOIN apartamentos ON clientes.numero_ap = apartamentos.numero_ap
        LEFT JOIN vagas_garagem ON clientes.numero_ap = vagas_garagem.numero_ap
    """

    result = pd.read_sql_query(query, conn)

    conn.close()

    return result