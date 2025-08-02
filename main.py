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
    'yareli_prime_blueprint', 'yareli_prime_neuroptics_blueprint', 'yareli_prime_chassis_blueprint', 'yareli_prime_systems_blueprint',
    'limbo_prime_blueprint', 'limbo_prime_neuroptics','limbo_prime_chassis', 'limbo_prime_systems', 
    'ash_prime_blueprint', 'ash_prime_neuroptics', 'ash_prime_chassis', 'ash_prime_systems',
    'atlas_prime_blueprint', 'atlas_prime_neuroptics', 'atlas_prime_chassis', 'atlas_prime_systems', 
    'banshee_prime_blueprint','banshee_prime_neuroptics', 'banshee_prime_chassis', 'banshee_prime_systems',
    'baruuk_prime_blueprint','baruuk_prime_neuroptics_blueprint', 'baruuk_prime_chassis_blueprint', 'baruuk_prime_systems_blueprint', 
    'chroma_prime_blueprint', 'chroma_prime_neuroptics','chroma_prime_chassis', 'chroma_prime_systems', 
    'ember_prime_blueprint', 'ember_prime_neuroptics', 'ember_prime_chassis','ember_prime_systems', 
    'equinox_prime_blueprint', 'equinox_prime_neuroptics', 'equinox_prime_chassis', 'equinox_prime_systems',
    'frost_prime_blueprint','frost_prime_neuroptics', 'frost_prime_chassis', 'frost_prime_systems', 
    'gara_prime_blueprint', 'gara_prime_neuroptics','gara_prime_chassis', 'gara_prime_systems', 
    'garuda_prime_blueprint', 'garuda_prime_neuroptics', 'garuda_prime_chassis','garuda_prime_systems', 
    'gauss_prime_blueprint', 'gauss_prime_neuroptics_blueprint', 'gauss_prime_chassis_blueprint', 'gauss_prime_systems_blueprint',
    'grendel_prime_blueprint', 'grendel_prime_neuroptics_blueprint', 'grendel_prime_chassis_blueprint', 'grendel_prime_systems_blueprint', 
    'harrow_prime_blueprint','harrow_prime_neuroptics', 'harrow_prime_chassis', 'harrow_prime_systems', 
    'hildryn_prime_blueprint', 'hildryn_prime_neuroptics_blueprint','hildryn_prime_chassis_blueprint', 'hildryn_prime_systems_blueprint', 
    'hydroid_prime_blueprint', 'hydroid_prime_neuroptics', 'hydroid_prime_chassis','hydroid_prime_systems', 
    'inaros_prime_blueprint', 'inaros_prime_neuroptics', 'inaros_prime_chassis', 'inaros_prime_systems',
    'ivara_prime_blueprint', 'ivara_prime_neuroptics', 'ivara_prime_chassis', 'ivara_prime_systems', 
    'khora_prime_blueprint','khora_prime_neuroptics_blueprint', 'khora_prime_chassis_blueprint', 'khora_prime_systems_blueprint', 
    'lavos_prime_blueprint', 'lavos_prime_neuroptics_blueprint','lavos_prime_chassis_blueprint', 'lavos_prime_systems_blueprint', 
    'loki_prime_blueprint', 'loki_prime_neuroptics', 'loki_prime_chassis','loki_prime_systems', 
    'mag_prime_blueprint', 'mag_prime_neuroptics', 'mag_prime_chassis', 'mag_prime_systems',
    'mesa_prime_blueprint', 'mesa_prime_neuroptics', 'mesa_prime_chassis', 'mesa_prime_systems', 
    'mirage_prime_blueprint','mirage_prime_neuroptics', 'mirage_prime_chassis', 'mirage_prime_systems', 
    'nekros_prime_blueprint', 'nekros_prime_neuroptics','nekros_prime_chassis', 'nekros_prime_systems', 
    'nezha_prime_blueprint', 'nezha_prime_neuroptics', 'nezha_prime_chassis','nezha_prime_systems', 
    'nidus_prime_blueprint', 'nidus_prime_neuroptics', 'nidus_prime_chassis', 'nidus_prime_systems',
    'nova_prime_blueprint', 'nova_prime_neuroptics', 'nova_prime_chassis', 'nova_prime_systems', 
    'nyx_prime_blueprint','nyx_prime_neuroptics', 'nyx_prime_chassis', 'nyx_prime_systems', 
    'oberon_prime_blueprint', 'oberon_prime_neuroptics','oberon_prime_chassis', 'oberon_prime_systems', 
    'protea_prime_blueprint', 'protea_prime_neuroptics_blueprint', 'protea_prime_chassis_blueprint','protea_prime_systems_blueprint', 
    'revenant_prime_blueprint', 'revenant_prime_neuroptics_blueprint', 'revenant_prime_chassis_blueprint','revenant_prime_systems_blueprint', 
    'rhino_prime_blueprint', 'rhino_prime_neuroptics', 'rhino_prime_chassis', 'rhino_prime_systems',
    'saryn_prime_blueprint', 'saryn_prime_neuroptics', 'saryn_prime_chassis', 'saryn_prime_systems', 
    'sevagoth_prime_blueprint','sevagoth_prime_neuroptics_blueprint', 'sevagoth_prime_chassis_blueprint', 'sevagoth_prime_systems_blueprint', 
    'titania_prime_blueprint','titania_prime_neuroptics', 'titania_prime_chassis', 'titania_prime_systems', 
    'trinity_prime_blueprint','trinity_prime_neuroptics', 'trinity_prime_chassis', 'trinity_prime_systems', 
    'valkyr_prime_blueprint','valkyr_prime_neuroptics', 'valkyr_prime_chassis', 'valkyr_prime_systems', 
    'vauban_prime_blueprint','vauban_prime_neuroptics', 'vauban_prime_chassis', 'vauban_prime_systems', 
    'volt_prime_blueprint','volt_prime_neuroptics', 'volt_prime_chassis', 'volt_prime_systems', 
    'wukong_prime_blueprint','wukong_prime_neuroptics', 'wukong_prime_chassis', 'wukong_prime_systems', 
    'xaku_prime_blueprint','xaku_prime_neuroptics_blueprint', 'xaku_prime_chassis_blueprint', 'xaku_prime_systems_blueprint', 
    'zephyr_prime_blueprint','zephyr_prime_neuroptics', 'zephyr_prime_chassis', 'zephyr_prime_systems',
    'acceltra_prime_blueprint', 'acceltra_prime_barrel', 'acceltra_prime_receiver', 'acceltra_prime_stock', 'astilla_prime_blueprint',
    'astilla_prime_barrel', 'astilla_prime_receiver', 'astilla_prime_stock', 'baza_prime_blueprint',
    'baza_prime_barrel', 'baza_prime_receiver', 'baza_prime_stock', 
    'boar_prime_blueprint', 'boar_prime_barrel','boar_prime_receiver', 'boar_prime_stock', 
    'boltor_prime_blueprint', 'boltor_prime_barrel','boltor_prime_receiver', 'boltor_prime_stock', 
    'braton_prime_blueprint', 'braton_prime_barrel','braton_prime_receiver', 'braton_prime_stock', 
    'burston_prime_blueprint', 'burston_prime_barrel','burston_prime_receiver', 'burston_prime_stock',
    'cedo_prime_blueprint', 'cedo_prime_barrel','cedo_prime_receiver', 'cedo_prime_stock', 
    'cernos_prime_blueprint', 'cernos_prime_lower_limb','cernos_prime_upper_limb','cernos_prime_grip','cernos_prime_string','rakta_cernos',
    'corinth_prime_blueprint','corinth_prime_barrel', 'corinth_prime_receiver', 'corinth_prime_stock', 
    'daikyu_prime_blueprint','daikyu_prime_grip', 'daikyu_prime_lower_limb', 'daikyu_prime_string', 'daikyu_prime_upper_limb',
    'fulmin_prime_blueprint', 'fulmin_prime_barrel', 'fulmin_prime_receiver', 'fulmin_prime_stock',
    'gotva_prime',
    'latron_prime_blueprint', 'latron_prime_barrel', 'latron_prime_receiver', 'latron_prime_stock',
    'paris_prime_blueprint', 'paris_prime_grip', 'paris_prime_string', 'paris_prime_upper_limb', 
    'rubico_prime_blueprint', 'rubico_prime_stock', 'rubico_prime_receiver', 'rubico_prime_barrel',
    'soma_prime_blueprint', 'soma_prime_barrel', 'soma_prime_receiver', 'soma_prime_stock',
    'stradavar_prime_blueprint', 'stradavar_prime_barrel', 'stradavar_prime_receiver',
    'stradavar_prime_stock', 'strun_prime_blueprint', 'strun_prime_barrel', 'strun_prime_receiver',
    'strun_prime_stock', 'sybaris_prime_blueprint', 'sybaris_prime_barrel', 'sybaris_prime_receiver',
    'sybaris_prime_stock', 'tenora_prime_blueprint', 'tenora_prime_barrel', 'tenora_prime_receiver',
    'tenora_prime_stock', 'tiberon_prime_blueprint', 'tiberon_prime_barrel', 'tiberon_prime_receiver',
    'tiberon_prime_stock', 'tigris_prime_blueprint', 'tigris_prime_barrel', 'tigris_prime_receiver',
    'tigris_prime_stock', 'trumna_prime_blueprint', 'trumna_prime_barrel', 'trumna_prime_receiver',
    'trumna_prime_stock', 'zhuge_prime_blueprint', 'zhuge_prime_barrel', 'zhuge_prime_receiver','zhuge_prime_string',
    'afuris_prime_blueprint', 'afuris_prime_barrel', 'afuris_prime_receiver', 'afuris_prime_link',
    'akarius_prime_blueprint', 'akarius_prime_barrel', 'akarius_prime_receiver', 'akarius_prime_link',
    'akbolto_prime_blueprint', 'akbolto_prime_barrel', 'akbolto_prime_receiver', 'akbolto_prime_link',
    'akbronco_prime_link', 'akbronco_prime_blueprint',
    'akjagara_prime_blueprint', 'akjagara_prime_barrel', 'akjagara_prime_receiver', 'akjagara_prime_link',
    'aklex_prime_blueprint', 'aklex_prime_link',
    'akmagnus_prime_blueprint', 'akmagnus_prime_link'
    'aksomati_prime_blueprint', 'aksomati_prime_barrel', 'aksomati_prime_receiver', 'aksomati_prime_link',
    'akstiletto_prime_blueprint', 'akstiletto_prime_barrel', 'akstiletto_prime_receiver', 'akstiletto_prime_link',
    'akvasto_prime_blueprint', 'akvasto_prime_link'
    'ballistica_prime_blueprint', 'ballistica_prime_upper_limb', 'ballistica_prime_lower_limb', 'ballistica_prime_string',
    'bronco_prime_barrel', 'bronco_prime_blueprint', 'bronco_prime_receiver',
    'measured_burst', 'entropy_burst',
    'epitaph_prime_blueprint', 'epitaph_prime_barrel', 'epitaph_prime_receiver', 'epitaph_prime_stock',
    'euphona_prime_blueprint', 'euphona_prime_barrel', 'euphona_prime_receiver', 'euphona_prime_stock',
    'hikou_prime_blueprint', 'hikou_prime_pouch', 'hikou_prime_stars',
    'hystrix_prime_blueprint', 'hystrix_prime_receiver', 'hystrix_prime_barrel',
    'knell_prime_barrel', 'knell_prime_blueprint', 'knell_prime_receiver',
    'kompressa_prime_blueprint', 'kompressa_prime_barrel', 'kompressa_prime_reciever',
    'lex_prime_blueprint', 'lex_prime_barrel', 'lex_prime_receiver', 'lex_prime_stock',
    'magnus_prime_blueprint', 'magnus_prime_receiver', 'magnus_prime_barrel',
    'pandero_prime_barrel', 'pandero_prime_receiver', 'pandero_prime_blueprint'
    'pyrana_prime_blueprint', 'pyrana_prime_receiver', 'pyrana_prime_barrel',
    'quassus_prime_blueprint', 'quassus_prime_handle', 'quassus_prime_blade',
    'sicarus_prime_barrel', 'sicarus_prime_receiver', 'sicarus_prime_blueprint',
    'spira_prime_blueprint', 'spira_prime_blade', 'spira_prime_pouch',
    'vasto_prime_barrel', 'vasto_prime_blueprint', 'vasto_prime_receiver',
    'velox_set', 'velox_receiver', 'velox_barrel', 'velox_prime_blueprint', 'velox_prime_barrel', 'velox_prime_receiver',
    'zylok_prime_blueprint', 'zylok_prime_barrel', 'zylok_prime_receiver',
    'ankyros_prime_blueprint', 'ankyros_prime_gauntlet', 'ankyros_prime_blade', 'ankyros_prime_handle',
    'cobra_crane_prime_blueprint', 'cobra_crane_prime_blade', 'cobra_crane_prime_handle', 'cobra_crane_prime_ornament',
    'dakra_prime_handle', 'dakra_prime_blade', 'dakra_prime_blueprint',
    'destreza_prime_handle', 'destreza_prime_blade', 'destreza_prime_blueprint',
    'dual_kamas_prime_blueprint', 'dual_kamas_prime_handle', 'dual_kamas_prime_blade',
    'dual_zoren_prime_blueprint', 'dual_zoren_prime_handle', 'dual_zoren_prime_blade',
    'fang_prime_handle', 'fang_prime_blade', 'fang_prime_blueprint',
    'fragor_prime_head', 'fragor_prime_blueprint', 'fragor_prime_handle',
    'galatine_prime_blueprint', 'galatine_prime_blade', 'galatine_prime_handle', 'galatine_prime_guard',
    'glaive_prime_blade', 'glaive_prime_disc', 'glaive_prime_blueprint',
    'gram_prime_handle', 'gram_prime_blueprint', 'gram_prime_blade',
    'guandao_prime_blueprint', 'guandao_prime_blade', 'guandao_prime_handle',
    'gunsen_prime_blueprint', 'gunsen_prime_handle', 'gunsen_prime_blade',
    'karyst_prime_handle', 'karyst_prime_blueprint', 'karyst_prime_blade',
    'kogake_prime_gauntlet', 'kogake_prime_boot', 'kogake_prime_blueprint',
    'kronen_prime_handle', 'kronen_prime_blueprint', 'kronen_prime_blade',
    'masseter_prime_blueprint', 'masseter_prime_blade', 'masseter_prime_handle',
    'nami_skyla_prime_handle', 'nami_skyla_prime_blade', 'nami_skyla_prime_blueprint',
    'nikana_prime_hilt', 'nikana_prime_blueprint', 'nikana_prime_blade',
    'ninkondi_prime_chain', 'ninkondi_prime_blueprint', 'ninkondi_prime_handle',
    'okina_prime_blueprint', 'okina_prime_handle', 'okina_prime_blade',
    'orthos_prime_blade', 'orthos_prime_blueprint', 'orthos_prime_handle',
    'pangolin_prime_blade', 'pangolin_prime_handle', 'pangolin_prime_blueprint',
    'reaper_prime_blueprint', 'reaper_prime_blade', 'reaper_prime_handle',
    'redeemer_prime_blade', 'redeemer_prime_blueprint', 'redeemer_prime_handle',
    'scindo_prime_handle', 'scindo_prime_blueprint', 'scindo_prime_blade',
    'silva_aegis_prime_blueprint', 'silva_aegis_prime_blade', 'silva_aegis_prime_hilt', 'silva_aegis_prime_shield',
    'tatsu_prime_blade', 'tatsu_prime_blueprint', 'tatsu_prime_handle'
    'tekko_prime_gauntlet', 'tekko_prime_blade', 'tekko_prime_blueprint'
    'tipedo_prime_blueprint', 'tipedo_prime_handle', 'tipedo_prime_ornament', 'tipedo_prime_blade',
    'venka_prime_blueprint', 'venka_prime_gauntlet', 'venka_prime_claws', 'venka_prime_link',
    'volnus_prime_blueprint', 'volnus_prime_head', 'volnus_prime_handle', 'volnus_prime_grip',
    'carrier_prime_blueprint', 'carrier_prime_cerebrum', 'carrier_prime_carapace', 'carrier_prime_systems',
    'dethcube_prime_blueprint', 'dethcube_prime_cerebrum', 'dethcube_prime_carapace', 'dethcube_prime_systems',
    'helios_prime_blueprint', 'helios_prime_cerebrum', 'helios_prime_carapace', 'helios_prime_systems',
    'nautilus_prime_blueprint', 'nautilus_prime_cerebrum', 'nautilus_prime_carapace', 'nautilus_prime_systems',
    'shade_prime_blueprint', 'shade_prime_cerebrum', 'shade_prime_carapace', 'shade_prime_systems',
    'wyrm_prime_blueprint', 'wyrm_prime_cerebrum', 'wyrm_prime_carapace', 'wyrm_prime_systems',
    
]

response = requests.get("https://api.warframe.market/v1/items")
items = response.json()['payload']['items']
print([item['url_name'] for item in items if 'cobra_crane' in item['url_name']])
print([item['url_name'] for item in items if 'dakra' in item['url_name']])
print([item['url_name'] for item in items if 'destreza' in item['url_name']])
print([item['url_name'] for item in items if 'dual_kamas' in item['url_name']])
print([item['url_name'] for item in items if 'dual_zoren' in item['url_name']])
print([item['url_name'] for item in items if 'fang' in item['url_name']])
print([item['url_name'] for item in items if 'fragor' in item['url_name']])
print([item['url_name'] for item in items if 'galantine' in item['url_name']])
print([item['url_name'] for item in items if 'glaive' in item['url_name']])
print([item['url_name'] for item in items if 'gram' in item['url_name']])
print([item['url_name'] for item in items if 'guandao' in item['url_name']])
print([item['url_name'] for item in items if 'gunsen' in item['url_name']])
print([item['url_name'] for item in items if 'karyst' in item['url_name']])
print([item['url_name'] for item in items if 'kogake' in item['url_name']])
print([item['url_name'] for item in items if 'kronen' in item['url_name']])
print([item['url_name'] for item in items if 'masseter' in item['url_name']])
print([item['url_name'] for item in items if 'nami_skyla' in item['url_name']])
print([item['url_name'] for item in items if 'nikana' in item['url_name']])
print([item['url_name'] for item in items if 'ninkondi' in item['url_name']])
print([item['url_name'] for item in items if 'okina' in item['url_name']])
print([item['url_name'] for item in items if 'orthos' in item['url_name']])
print([item['url_name'] for item in items if 'pangolin' in item['url_name']])
print([item['url_name'] for item in items if 'reaper' in item['url_name']])
print([item['url_name'] for item in items if 'redeemer' in item['url_name']])
print([item['url_name'] for item in items if 'scindo' in item['url_name']])
print([item['url_name'] for item in items if 'silva_aegis' in item['url_name']])
print([item['url_name'] for item in items if 'tatsu' in item['url_name']])
print([item['url_name'] for item in items if 'tekko' in item['url_name']])


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

        # Verifica se o item tem informações de ducats
        # Encontrar o item correto em items_in_set
        for set_item in item_data['payload']['item']['items_in_set']:
            if set_item['url_name'] == url_name:
                ducats = set_item.get('ducats', 0)
                break
        else:
            ducats = 0  # Se não encontrar o item, define ducats como 0
        # Log para depuração
        print(f"Item: {url_name}, Ducats: {ducats}")

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