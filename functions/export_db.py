import functions.join_tables
import pandas as pd

def export_all_data():
    data = functions.join_tables.join_all_tables('dados_imobiliaria.db')
    data = pd.DataFrame(data)
    data.to_excel('dados_imobiliaria.xlsx')