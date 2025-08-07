# Importações necessárias
import cv2
import pytesseract
import json
import mss
from datetime import datetime
import time
import requests
from zoneinfo import ZoneInfo as timezone

# Configura o caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Ajuste o caminho conforme sua instalação

# Define a região para capturar a tela inteira
sct = mss.mss()
monitor = sct.monitors[1]  # Captura o monitor principal

# Função para atualizar os dados do Warframe Market
def update_warframe_data():
    # Verifica se é meio-dia (12:00) no horário de Brasília
    current_time = datetime.now().astimezone(timezone('America/Sao_Paulo'))
    if current_time.hour == 12 and current_time.minute == 0:
        print(f"Atualizando dados do Warframe Market às {current_time.strftime('%H:%M')}...")
        # URL base da API
        BASE_URL = "https://api.warframe.market/v1"
        # Lista de itens (ajuste com sua lista completa)
        item_list = [
            'akbolto_prime_barrel', 'lex_prime_receiver', 'burston_prime_stock', 'shade_prime_systems'
            # Adicione os outros itens da sua lista original aqui
        ]
        data = []

        for url_name in item_list:
            try:
                item_url = f"{BASE_URL}/items/{url_name}"
                response = requests.get(item_url)
                response.raise_for_status()
                item_data = response.json()
                for set_item in item_data['payload']['item']['items_in_set']:
                    if set_item['url_name'] == url_name:
                        ducats = set_item.get('ducats', 0)
                        break
                else:
                    ducats = 0
                time.sleep(0.333)

                orders_url = f"{BASE_URL}/items/{url_name}/orders"
                response = requests.get(orders_url)
                response.raise_for_status()
                orders_data = response.json()
                sell_orders = [
                    order for order in orders_data['payload']['orders']
                    if order['order_type'] == 'sell' and order['user']['status'] == 'ingame'
                ]
                lowest_price = min(order['platinum'] for order in sell_orders) if sell_orders else None
                time.sleep(0.333)

                data.append({
                    'url_name': url_name,
                    'ducats': ducats,
                    'lowest_sell_price': lowest_price
                })
            except Exception as e:
                print(f"Erro ao processar {url_name}: {e}")
                continue

        with open('warframe_data.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Dados atualizados com sucesso!")
    else:
        print(f"Não é meio-dia (horário atual: {current_time.hour}:{current_time.minute}). Nenhuma atualização realizada.")

# Função para monitorar a tela
def monitor_screen():
    while True:
        # Captura a tela inteira
        screenshot = sct.grab(monitor)
        img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Extrai o texto da tela inteira
        text = pytesseract.image_to_string(img)
        print("Texto extraído:", text)

        # Limpa o texto e busca no banco de dados
        lines = text.split('\n')
        items_found = []
        with open('warframe_data.json', 'r') as f:
            data = json.load(f)
        for line in lines:
            line = line.strip().lower()
            if line:
                for item in data:
                    if item['url_name'].lower() in line:
                        items_found.append(item['url_name'])
                        break

        # Exibe os resultados
        print("Itens identificados:", items_found)
        for item in items_found:
            plat = next((d['lowest_sell_price'] for d in data if d['url_name'] == item), "N/A")
            ducats = next((d['ducats'] for d in data if d['url_name'] == item), 0)
            print(f"Item: {item}, Platina: {plat}, Ducats: {ducats}")

        # Aguarda 24 horas para a próxima verificação
        time.sleep(86400)  # 86400 segundos = 24 horas
        update_warframe_data()

# Inicia o monitoramento
if __name__ == "__main__":
    update_warframe_data()  # Atualiza imediatamente na primeira execução
    monitor_screen()