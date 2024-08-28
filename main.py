import pandas as pd
import os

# Definir caminho relativo para o arquivo JSON e CSV
json_path = 'mercadolivre/Dashboard/starturls.json'
csv_path = 'mercadolivre/Dashboard/starturls.csv'

# Carregar dados JSON
df = pd.read_json(json_path)

# Salvar dados como CSV
df.to_csv(csv_path, index=False)

print(f'Arquivo CSV criado com sucesso em: {csv_path}')
