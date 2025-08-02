#importando bibliotecas para o projeto
import os #para manipular arquivos e diretórios
import pywmapi #API do Warframe Market
import time #dalays
import json #json para salvar os dados

#Inicializar o cliente da API
wm = pywmapi.WarframeMarket()

# Lista de itens
item_list = ['octavia_prime_blueprint', 'octavia_prime_neuroptics', 'octavia_prime_chassis', 'octavia_prime_systems', 'yareli_prime_blueprint',
'yareli_prime_neuroptics', 'yareli_prime_chassis', 'yareli_prime_systems',
]

#Lista para armazenar os itens que já foram verificados
data= []

#Loop para verificar os itens
for url_name in item_list:
    try:
        #Obter infromaçao do item
        item_info = wm.items.get_item(url_name)
        # Extrair o valor em ducats (pode ser None se não existir)
        ducats = item_info['payload']['item'].get('ducats', 0)

        # Atraso para respeitar o limite de taxa da API
        time.sleep(0.4)

        # Obter ordens do item
        orders = wm.items.get_orders(url_name)

        # Filtrar ordens de venda
        sell_orders = [order for order in orders['payload']['orders'] if order['order_type'] == 'sell']

        # Encontrar o preço mais baixo em platina
        if sell_orders:
            lowest_price = min(order['platinum'] for order in sell_orders)
        else:
            lowest_price = None

        # Armazenar os dados do item
        data.append({
            'url_name': url_name,
            'ducats': ducats,
            'lowest_sell_price': lowest_price
        })

        # Atraso adicional para garantir que não excederei o limite de chamadas
        time.sleep(0.4)

    #exceção para erros de requisição
    except Exception as e:
        print(f"Erro ao processar o item {url_name}: {e}")
        continue

# Agora 'data' contém todos os dados coletados
# Salvar em um arquivo JSON
with open('warframe_data.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Dados coletados e salvos com sucesso!")
