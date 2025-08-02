# Importando bibliotecas para o projeto
import os  # Para manipular arquivos e diretórios
import requests  # Para chamadas HTTP à API
import time  # Para delays
import json  # Para salvar os dados em JSON

# URL base da API do Warframe Market
BASE_URL = "https://api.warframe.market/v1"

# Lista de itens
item_list = [
    'octavia_prime_blueprint', 'octavia_prime_neuroptics', 'octavia_prime_chassis', 'octavia_prime_systems',
    'yareli_prime_blueprint', 'yareli_prime_neuroptics', 'yareli_prime_chassis', 'yareli_prime_systems'
]

# Lista para armazenar os dados coletados
data = []

# Loop para processar cada item
for url_name in item_list:
    try:
        # Obtem informações do item para ducats
        item_url = f"{BASE_URL}/items/{url_name}"
        response = requests.get(item_url)
        response.raise_for_status()  # Levanta erro para códigos HTTP 4xx/5xx
        item_data = response.json()
        ducats = item_data['payload']['item']['items_in_set'][0].get('ducats', 0)

        # Atraso para respeitar o limite de taxa da API (3 chamadas por segundo)
        time.sleep(0.333)

        # Obter ordens do item
        orders_url = f"{BASE_URL}/items/{url_name}/orders"
        response = requests.get(orders_url)
        response.raise_for_status()
        orders_data = response.json()
        
        # Filtrar ordens de venda de jogadores online
        sell_orders = [
            order for order in orders_data['payload']['orders']
            if order['order_type'] == 'sell' and order['user']['status'] == 'ingame'
        ]

        # Encontrar o preço mais baixo em platina
        lowest_price = min(order['platinum'] for order in sell_orders) if sell_orders else None

        # Armazenar os dados do item
        data.append({
            'url_name': url_name,
            'ducats': ducats,
            'lowest_sell_price': lowest_price
        })

        # Atraso adicional para respeitar o limite de taxa
        time.sleep(0.333)

    except Exception as e:
        print(f"Erro ao processar o item {url_name}: {e}")
        continue

# Salvar os dados em um arquivo JSON
with open('warframe_data.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Dados coletados e salvos com sucesso!")