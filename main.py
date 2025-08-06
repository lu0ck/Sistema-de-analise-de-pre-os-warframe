# Importando bibliotecas para o projeto
import os  # Para manipular arquivos e diretórios
import requests  # Para chamadas HTTP à API
import time  # Para delays
import json  # Para salvar os dados em JSON

# URL base da API do Warframe Market
BASE_URL = "https://api.warframe.market/v1"

# Dicionário estático de ducats (baseado no Warframe Wiki)
DUCATS_REFERENCE = {
    # Warframes Prime
    'octavia_prime_blueprint': 45,
    'octavia_prime_neuroptics': 15,
    'octavia_prime_chassis': 45,
    'octavia_prime_systems': 100,

    'yareli_prime_blueprint': 45,
    'yareli_prime_neuroptics_blueprint': 15,
    'yareli_prime_chassis_blueprint': 45,
    'yareli_prime_systems_blueprint': 100,

    'limbo_prime_blueprint': 45,
    'limbo_prime_neuroptics': 15,
    'limbo_prime_chassis': 45,
    'limbo_prime_systems': 100,

    'ash_prime_blueprint': 45,
    'ash_prime_neuroptics': 15,
    'ash_prime_chassis': 45,
    'ash_prime_systems': 100,

    'atlas_prime_blueprint': 45,
    'atlas_prime_neuroptics': 15,
    'atlas_prime_chassis': 45,
    'atlas_prime_systems': 100,

    'banshee_prime_blueprint': 45,
    'banshee_prime_neuroptics': 15,
    'banshee_prime_chassis': 45,
    'banshee_prime_systems': 100,

    'baruuk_prime_blueprint': 45,
    'baruuk_prime_neuroptics_blueprint': 15,
    'baruuk_prime_chassis_blueprint': 45,
    'baruuk_prime_systems_blueprint': 100,

    'chroma_prime_blueprint': 45,
    'chroma_prime_neuroptics': 15,
    'chroma_prime_chassis': 45,
    'chroma_prime_systems': 100,

    'ember_prime_blueprint': 45,
    'ember_prime_neuroptics': 15,
    'ember_prime_chassis': 45,
    'ember_prime_systems': 100,

    'equinox_prime_blueprint': 45,
    'equinox_prime_neuroptics': 15,
    'equinox_prime_chassis': 45,
    'equinox_prime_systems': 100,

    'frost_prime_blueprint': 45,
    'frost_prime_neuroptics': 15,
    'frost_prime_chassis': 45,
    'frost_prime_systems': 100,

    'gara_prime_blueprint': 45,
    'gara_prime_neuroptics': 15,
    'gara_prime_chassis': 45,
    'gara_prime_systems': 100,

    'garuda_prime_blueprint': 45,
    'garuda_prime_neuroptics': 15,
    'garuda_prime_chassis': 45,
    'garuda_prime_systems': 100,

    'gauss_prime_blueprint': 45,
    'gauss_prime_neuroptics_blueprint': 15,
    'gauss_prime_chassis_blueprint': 45,
    'gauss_prime_systems_blueprint': 100,

    'grendel_prime_blueprint': 45,
    'grendel_prime_neuroptics_blueprint': 15,
    'grendel_prime_chassis_blueprint': 45,
    'grendel_prime_systems_blueprint': 100,

    'harrow_prime_blueprint': 45,
    'harrow_prime_neuroptics': 15,
    'harrow_prime_chassis': 45,
    'harrow_prime_systems': 100,

    'hildryn_prime_blueprint': 45,
    'hildryn_prime_neuroptics_blueprint': 15,
    'hildryn_prime_chassis_blueprint': 45,
    'hildryn_prime_systems_blueprint': 100,

    'hydroid_prime_blueprint': 45,
    'hydroid_prime_neuroptics': 15,
    'hydroid_prime_chassis': 45,
    'hydroid_prime_systems': 100,

    'inaros_prime_blueprint': 45,
    'inaros_prime_neuroptics': 15,
    'inaros_prime_chassis': 45,
    'inaros_prime_systems': 100,

    'ivara_prime_blueprint': 45,
    'ivara_prime_neuroptics': 15,
    'ivara_prime_chassis': 45,
    'ivara_prime_systems': 100,

    'khora_prime_blueprint': 45,
    'khora_prime_neuroptics_blueprint': 15,
    'khora_prime_chassis_blueprint': 45,
    'khora_prime_systems_blueprint': 100,

    'lavos_prime_blueprint': 45,
    'lavos_prime_neuroptics_blueprint': 15,
    'lavos_prime_chassis_blueprint': 45,
    'lavos_prime_systems_blueprint': 100,

    'loki_prime_blueprint': 45,
    'loki_prime_neuroptics': 15,
    'loki_prime_chassis': 45,
    'loki_prime_systems': 100,

    'mag_prime_blueprint': 45,
    'mag_prime_neuroptics': 15,
    'mag_prime_chassis': 45,
    'mag_prime_systems': 100,

    'mesa_prime_blueprint': 45,
    'mesa_prime_neuroptics': 15,
    'mesa_prime_chassis': 45,
    'mesa_prime_systems': 100,

    'mirage_prime_blueprint': 45,
    'mirage_prime_neuroptics': 15,
    'mirage_prime_chassis': 45,
    'mirage_prime_systems': 100,

    'nekros_prime_blueprint': 45,
    'nekros_prime_neuroptics': 15,
    'nekros_prime_chassis': 45,
    'nekros_prime_systems': 100,

    'nezha_prime_blueprint': 45,
    'nezha_prime_neuroptics': 15,
    'nezha_prime_chassis': 45,
    'nezha_prime_systems': 100,

    'nidus_prime_blueprint': 45,
    'nidus_prime_neuroptics': 15,
    'nidus_prime_chassis': 45,
    'nidus_prime_systems': 100,

    'nova_prime_blueprint': 45,
    'nova_prime_neuroptics': 15,
    'nova_prime_chassis': 45,
    'nova_prime_systems': 100,

    'nyx_prime_blueprint': 45,
    'nyx_prime_neuroptics': 15,
    'nyx_prime_chassis': 45,
    'nyx_prime_systems': 100,

    'oberon_prime_blueprint': 45,
    'oberon_prime_neuroptics': 15,
    'oberon_prime_chassis': 45,
    'oberon_prime_systems': 100,

    'protea_prime_blueprint': 45,
    'protea_prime_neuroptics_blueprint': 15,
    'protea_prime_chassis_blueprint': 45,
    'protea_prime_systems_blueprint': 100,

    'revenant_prime_blueprint': 45,
    'revenant_prime_neuroptics_blueprint': 15,
    'revenant_prime_chassis_blueprint': 45,
    'revenant_prime_systems_blueprint': 100,

    'rhino_prime_blueprint': 45,
    'rhino_prime_neuroptics': 15,
    'rhino_prime_chassis': 45,
    'rhino_prime_systems': 100,

    'saryn_prime_blueprint': 45,
    'saryn_prime_neuroptics': 15,
    'saryn_prime_chassis': 45,
    'saryn_prime_systems': 100,

    'sevagoth_prime_blueprint': 45,
    'sevagoth_prime_neuroptics_blueprint': 15,
    'sevagoth_prime_chassis_blueprint': 45,
    'sevagoth_prime_systems_blueprint': 100,

    'titania_prime_blueprint': 45,
    'titania_prime_neuroptics': 15,
    'titania_prime_chassis': 45,
    'titania_prime_systems': 100,

    'trinity_prime_blueprint': 45,
    'trinity_prime_neuroptics': 15,
    'trinity_prime_chassis': 45,
    'trinity_prime_systems': 100,

    'valkyr_prime_blueprint': 45,
    'valkyr_prime_neuroptics': 15,
    'valkyr_prime_chassis': 45,
    'valkyr_prime_systems': 100,

    'vauban_prime_blueprint': 45,
    'vauban_prime_neuroptics': 15,
    'vauban_prime_chassis': 45,
    'vauban_prime_systems': 100,

    'volt_prime_blueprint': 45,
    'volt_prime_neuroptics': 15,
    'volt_prime_chassis': 45,
    'volt_prime_systems': 100,

    'wukong_prime_blueprint': 45,
    'wukong_prime_neuroptics': 15,
    'wukong_prime_chassis': 45,
    'wukong_prime_systems': 100,

    'xaku_prime_blueprint': 45,
    'xaku_prime_neuroptics_blueprint': 15,
    'xaku_prime_chassis_blueprint': 45,
    'xaku_prime_systems_blueprint': 100,

    'zephyr_prime_blueprint': 45,
    'zephyr_prime_neuroptics': 15,
    'zephyr_prime_chassis': 45,
    'zephyr_prime_systems': 100,

    # Armas Prime (exemplo padrão, geralmente com essas faixas)
    'acceltra_prime_blueprint': 35,
    'acceltra_prime_barrel': 15,
    'acceltra_prime_receiver': 15,
    'acceltra_prime_stock': 15,

    'astilla_prime_blueprint': 35,
    'astilla_prime_barrel': 15,
    'astilla_prime_receiver': 15,
    'astilla_prime_stock': 15,

    'baza_prime_blueprint': 35,
    'baza_prime_barrel': 15,
    'baza_prime_receiver': 15,
    'baza_prime_stock': 15,

    'boar_prime_blueprint': 35,
    'boar_prime_barrel': 15,
    'boar_prime_receiver': 15,
    'boar_prime_stock': 15,

    'boltor_prime_blueprint': 35,
    'boltor_prime_barrel': 15,
    'boltor_prime_receiver': 15,
    'boltor_prime_stock': 15,

    'braton_prime_blueprint': 35,
    'braton_prime_barrel': 15,
    'braton_prime_receiver': 15,
    'braton_prime_stock': 15,

    'burston_prime_blueprint': 35,
    'burston_prime_barrel': 15,
    'burston_prime_receiver': 15,
    'burston_prime_stock': 15,

    'cedo_prime_blueprint': 35,
    'cedo_prime_barrel': 15,
    'cedo_prime_receiver': 15,
    'cedo_prime_stock': 15,

    'cernos_prime_blueprint': 25,
    'cernos_prime_lower_limb': 15,
    'cernos_prime_upper_limb': 15,
    'cernos_prime_grip': 15,
    'cernos_prime_string': 15,
    'rakta_cernos': 35,

    'corinth_prime_blueprint': 35,
    'corinth_prime_barrel': 15,
    'corinth_prime_receiver': 15,
    'corinth_prime_stock': 15,

    'daikyu_prime_blueprint': 35,
    'daikyu_prime_grip': 15,
    'daikyu_prime_lower_limb': 15,
    'daikyu_prime_string': 15,
    'daikyu_prime_upper_limb': 15,

    'fulmin_prime_blueprint': 35,
    'fulmin_prime_barrel': 15,
    'fulmin_prime_receiver': 15,
    'fulmin_prime_stock': 15,

    'gotva_prime': 35,

    'latron_prime_blueprint': 35,
    'latron_prime_barrel': 15,
    'latron_prime_receiver': 15,
    'latron_prime_stock': 15,

    'paris_prime_blueprint': 35,
    'paris_prime_grip': 15,
    'paris_prime_string': 15,
    'paris_prime_upper_limb': 15,

    'rubico_prime_blueprint': 35,
    'rubico_prime_stock': 15,
    'rubico_prime_receiver': 15,
    'rubico_prime_barrel': 15,

    'soma_prime_blueprint': 35,
    'soma_prime_barrel': 15,
    'soma_prime_receiver': 15,
    'soma_prime_stock': 15,

    'stradavar_prime_blueprint': 35,
    'stradavar_prime_barrel': 15,
    'stradavar_prime_receiver': 15,
    'stradavar_prime_stock': 15,

    'strun_prime_blueprint': 35,
    'strun_prime_barrel': 15,
    'strun_prime_receiver': 15,
    'strun_prime_stock': 15,

    'sybaris_prime_blueprint': 35,
    'sybaris_prime_barrel': 15,
    'sybaris_prime_receiver': 15,
    'sybaris_prime_stock': 15,

    'tenora_prime_blueprint': 35,
    'tenora_prime_barrel': 15,
    'tenora_prime_receiver': 15,
    'tenora_prime_stock': 15,

    'tiberon_prime_blueprint': 35,
    'tiberon_prime_barrel': 15,
    'tiberon_prime_receiver': 15,
    'tiberon_prime_stock': 15,

    'tigris_prime_blueprint': 35,
    'tigris_prime_barrel': 15,
    'tigris_prime_receiver': 15,
    'tigris_prime_stock': 15,

    'trumna_prime_blueprint': 35,
    'trumna_prime_barrel': 15,
    'trumna_prime_receiver': 15,
    'trumna_prime_stock': 15,

    'zhuge_prime_blueprint': 35,
    'zhuge_prime_barrel': 15,
    'zhuge_prime_receiver': 15,
    'zhuge_prime_string': 15,

    'afuris_prime_blueprint': 35,
    'afuris_prime_barrel': 15,
    'afuris_prime_receiver': 15,
    'afuris_prime_link': 15,

    'akarius_prime_blueprint': 35,
    'akarius_prime_barrel': 15,
    'akarius_prime_receiver': 15,
    'akarius_prime_link': 15,

    'akbolto_prime_blueprint': 35,
    'akbolto_prime_barrel': 15,
    'akbolto_prime_receiver': 15,
    'akbolto_prime_link': 15,

    'akbronco_prime_blueprint': 35,
    'akbronco_prime_link': 15,

    'akjagara_prime_blueprint': 35,
    'akjagara_prime_barrel': 15,
    'akjagara_prime_receiver': 15,
    'akjagara_prime_link': 15,

    'aklex_prime_blueprint': 35,
    'aklex_prime_link': 15,

    'akmagnus_prime_blueprint': 35,
    'akmagnus_prime_link': 15,

    'aksomati_prime_blueprint': 35,
    'aksomati_prime_barrel': 15,
    'aksomati_prime_receiver': 15,
    'aksomati_prime_link': 15,

    'akstiletto_prime_blueprint': 35,
    'akstiletto_prime_barrel': 15,
    'akstiletto_prime_receiver': 15,

    'akvasto_prime_blueprint': 35,
    'akvasto_prime_link': 15,

    'ballistica_prime_blueprint': 35,
    'ballistica_prime_upper_limb': 15,
    'ballistica_prime_lower_limb': 15,
    'ballistica_prime_string': 15,

    'bronco_prime_blueprint': 35,
    'bronco_prime_barrel': 15,
    'bronco_prime_receiver': 15,

    'measured_burst': 15,
    'entropy_burst': 15,

    'epitaph_prime_blueprint': 35,
    'epitaph_prime_barrel': 15,
    'epitaph_prime_receiver': 15,

    'euphona_prime_blueprint': 35,
    'euphona_prime_barrel': 15,
    'euphona_prime_receiver': 15,

    'hikou_prime_blueprint': 35,
    'hikou_prime_pouch': 15,
    'hikou_prime_stars': 15,

    'hystrix_prime_blueprint': 35,
    'hystrix_prime_receiver': 15,
    'hystrix_prime_barrel': 15,

    'knell_prime_blueprint': 35,
    'knell_prime_barrel': 15,
    'knell_prime_receiver': 15,

    'kompressa_prime_blueprint': 35,
    'kompressa_prime_barrel': 15,
    'kompressa_prime_reciever': 15,

    'lex_prime_blueprint': 35,
    'lex_prime_barrel': 15,
    'lex_prime_receiver': 15,

    'magnus_prime_blueprint': 35,
    'magnus_prime_receiver': 15,
    'magnus_prime_barrel': 15,

    'pandero_prime_blueprint': 35,
    'pandero_prime_barrel': 15,
    'pandero_prime_receiver': 15,

    'pyrana_prime_blueprint': 35,
    'pyrana_prime_receiver': 15,
    'pyrana_prime_barrel': 15,

    'quassus_prime_blueprint': 35,
    'quassus_prime_handle': 15,
    'quassus_prime_blade': 15,

    'sicarus_prime_blueprint': 35,
    'sicarus_prime_barrel': 15,
    'sicarus_prime_receiver': 15,

    'spira_prime_blueprint': 35,
    'spira_prime_blade': 15,
    'spira_prime_pouch': 15,

    'vasto_prime_blueprint': 35,
    'vasto_prime_barrel': 15,
    'vasto_prime_receiver': 15,

    'velox_prime_blueprint': 35,
    'velox_set': 15,
    'velox_receiver': 15,
    'velox_barrel': 15,
    'velox_prime_barrel': 15,
    'velox_prime_receiver': 15,

    'zylok_prime_blueprint': 35,
    'zylok_prime_barrel': 15,
    'zylok_prime_receiver': 15,

    # Componente de armas corpo-a-corpo Prime (geralmente 15-35)
    'ankyros_prime_blueprint': 35,
    'ankyros_prime_gauntlet': 15,
    'ankyros_prime_blade': 15,

    'dakra_prime_blueprint': 35,
    'dakra_prime_handle': 15,
    'dakra_prime_blade': 15,

    'destreza_prime_blueprint': 35,
    'destreza_prime_handle': 15,
    'destreza_prime_blade': 15,

    'dual_kamas_prime_blueprint': 35,
    'dual_kamas_prime_handle': 15,
    'dual_kamas_prime_blade': 15,

    'dual_zoren_prime_blueprint': 35,
    'dual_zoren_prime_handle': 15,
    'dual_zoren_prime_blade': 15,

    'fang_prime_blueprint': 35,
    'fang_prime_handle': 15,
    'fang_prime_blade': 15,

    'fragor_prime_blueprint': 35,
    'fragor_prime_head': 15,
    'fragor_prime_handle': 15,

    'galatine_prime_blueprint': 35,
    'galatine_prime_blade': 15,
    'galatine_prime_handle': 15,

    'glaive_prime_blueprint': 35,
    'glaive_prime_blade': 15,
    'glaive_prime_disc': 15,

    'gram_prime_blueprint': 35,
    'gram_prime_handle': 15,
    'gram_prime_blade': 15,

    'guandao_prime_blueprint': 35,
    'guandao_prime_blade': 15,
    'guandao_prime_handle': 15,

    'gunsen_prime_blueprint': 35,
    'gunsen_prime_handle': 15,
    'gunsen_prime_blade': 15,

    'karyst_prime_blueprint': 35,
    'karyst_prime_handle': 15,
    'karyst_prime_blade': 15,

    'kogake_prime_blueprint': 35,
    'kogake_prime_gauntlet': 15,
    'kogake_prime_boot': 15,

    'kronen_prime_blueprint': 35,
    'kronen_prime_handle': 15,
    'kronen_prime_blade': 15,

    'masseter_prime_blueprint': 35,
    'masseter_prime_blade': 15,
    'masseter_prime_handle': 15,

    'nami_skyla_prime_blueprint': 35,
    'nami_skyla_prime_handle': 15,
    'nami_skyla_prime_blade': 15,

    'nikana_prime_blueprint': 35,
    'nikana_prime_blade': 15,
    'nikana_prime_hilt': 15,

    'ninkondi_prime_blueprint': 35,
    'ninkondi_prime_chain': 15,
    'ninkondi_prime_handle': 15,

    'okina_prime_blueprint': 35,
    'okina_prime_handle': 15,
    'okina_prime_blade': 15,

    'orthos_prime_blueprint': 35,
    'orthos_prime_blade': 15,
    'orthos_prime_handle': 15,

    'pangolin_prime_blueprint': 35,
    'pangolin_prime_blade': 15,
    'pangolin_prime_handle': 15,

    'reaper_prime_blueprint': 35,
    'reaper_prime_blade': 15,
    'reaper_prime_handle': 15,

    'redeemer_prime_blueprint': 35,
    'redeemer_prime_blade': 15,
    'redeemer_prime_handle': 15,

    'scindo_prime_blueprint': 35,
    'scindo_prime_handle': 15,
    'scindo_prime_blade': 15,

    'tatsu_prime_blueprint': 35,
    'tatsu_prime_blade': 15,
    'tatsu_prime_handle': 15,

    'tekko_prime_blueprint': 35,
    'tekko_prime_gauntlet': 15,
    'tekko_prime_blade': 15,

    'tipedo_prime_blueprint': 35,
    'tipedo_prime_handle': 15,
    'tipedo_prime_ornament': 15,

    'venka_prime_blueprint': 35,
    'venka_prime_gauntlet': 15,

    'volnus_prime_blueprint': 35,
    'volnus_prime_head': 15,
    'volnus_prime_handle': 15,

    # Sentinelas Prime
    'carrier_prime_blueprint': 45,
    'carrier_prime_cerebrum': 15,
    'carrier_prime_carapace': 45,
    'carrier_prime_systems': 100,

    'dethcube_prime_blueprint': 45,
    'dethcube_prime_cerebrum': 15,
    'dethcube_prime_carapace': 45,
    'dethcube_prime_systems': 100,

    'helios_prime_blueprint': 45,
    'helios_prime_cerebrum': 15,
    'helios_prime_carapace': 45,
    'helios_prime_systems': 100,

    'nautilus_prime_blueprint': 45,
    'nautilus_prime_cerebrum': 15,
    'nautilus_prime_carapace': 45,
    'nautilus_prime_systems': 100,

    'shade_prime_blueprint': 45,
    'shade_prime_cerebrum': 15,
    'shade_prime_carapace': 45,
    'shade_prime_systems': 100,

    'wyrm_prime_blueprint': 45,
    'wyrm_prime_cerebrum': 15,
    'wyrm_prime_carapace': 45,
    'wyrm_prime_systems': 100,
}


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
    'akmagnus_prime_blueprint','akmagnus_prime_link',
    'aksomati_prime_blueprint', 'aksomati_prime_barrel', 'aksomati_prime_receiver', 'aksomati_prime_link',
    'akstiletto_prime_blueprint', 'akstiletto_prime_barrel', 'akstiletto_prime_receiver',
    'akvasto_prime_blueprint', 'akvasto_prime_link'
    'ballistica_prime_blueprint', 'ballistica_prime_upper_limb', 'ballistica_prime_lower_limb', 'ballistica_prime_string',
    'bronco_prime_barrel', 'bronco_prime_blueprint', 'bronco_prime_receiver',
    'measured_burst', 'entropy_burst',
    'epitaph_prime_blueprint', 'epitaph_prime_barrel', 'epitaph_prime_receiver',
    'euphona_prime_blueprint', 'euphona_prime_barrel', 'euphona_prime_receiver', 
    'hikou_prime_blueprint', 'hikou_prime_pouch', 'hikou_prime_stars',
    'hystrix_prime_blueprint', 'hystrix_prime_receiver', 'hystrix_prime_barrel',
    'knell_prime_barrel', 'knell_prime_blueprint', 'knell_prime_receiver',
    'kompressa_prime_blueprint', 'kompressa_prime_barrel', 'kompressa_prime_reciever',
    'lex_prime_blueprint', 'lex_prime_barrel', 'lex_prime_receiver',
    'magnus_prime_blueprint', 'magnus_prime_receiver', 'magnus_prime_barrel',
    'pandero_prime_barrel', 'pandero_prime_receiver', 'pandero_prime_blueprint'
    'pyrana_prime_blueprint', 'pyrana_prime_receiver', 'pyrana_prime_barrel',
    'quassus_prime_blueprint', 'quassus_prime_handle', 'quassus_prime_blade',
    'sicarus_prime_barrel', 'sicarus_prime_receiver', 'sicarus_prime_blueprint',
    'spira_prime_blueprint', 'spira_prime_blade', 'spira_prime_pouch',
    'vasto_prime_barrel', 'vasto_prime_blueprint', 'vasto_prime_receiver',
    'velox_set', 'velox_receiver', 'velox_barrel', 'velox_prime_blueprint', 'velox_prime_barrel', 'velox_prime_receiver',
    'zylok_prime_blueprint', 'zylok_prime_barrel', 'zylok_prime_receiver',
    'ankyros_prime_blueprint', 'ankyros_prime_gauntlet', 'ankyros_prime_blade',
    'dakra_prime_handle', 'dakra_prime_blade', 'dakra_prime_blueprint',
    'destreza_prime_handle', 'destreza_prime_blade', 'destreza_prime_blueprint',
    'dual_kamas_prime_blueprint', 'dual_kamas_prime_handle', 'dual_kamas_prime_blade',
    'dual_zoren_prime_blueprint', 'dual_zoren_prime_handle', 'dual_zoren_prime_blade',
    'fang_prime_handle', 'fang_prime_blade', 'fang_prime_blueprint',
    'fragor_prime_head', 'fragor_prime_blueprint', 'fragor_prime_handle',
    'galatine_prime_blueprint', 'galatine_prime_blade', 'galatine_prime_handle',
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
    'tatsu_prime_blade', 'tatsu_prime_blueprint', 'tatsu_prime_handle',
    'tekko_prime_gauntlet', 'tekko_prime_blade', 'tekko_prime_blueprint',
    'tipedo_prime_blueprint', 'tipedo_prime_handle', 'tipedo_prime_ornament',
    'venka_prime_blueprint', 'venka_prime_gauntlet',
    'volnus_prime_blueprint', 'volnus_prime_head', 'volnus_prime_handle',
    'carrier_prime_blueprint', 'carrier_prime_cerebrum', 'carrier_prime_carapace', 'carrier_prime_systems',
    'dethcube_prime_blueprint', 'dethcube_prime_cerebrum', 'dethcube_prime_carapace', 'dethcube_prime_systems',
    'helios_prime_blueprint', 'helios_prime_cerebrum', 'helios_prime_carapace', 'helios_prime_systems',
    'nautilus_prime_blueprint', 'nautilus_prime_cerebrum', 'nautilus_prime_carapace', 'nautilus_prime_systems',
    'shade_prime_blueprint', 'shade_prime_cerebrum', 'shade_prime_carapace', 'shade_prime_systems',
    'wyrm_prime_blueprint', 'wyrm_prime_cerebrum', 'wyrm_prime_carapace', 'wyrm_prime_systems',
    
]


""" 
### para busca exata de nome de item
response = requests.get("https://api.warframe.market/v1/items")
items = response.json()['payload']['items']
print([item['url_name'] for item in items if 'cobra_crane' in item['url_name']])
"""


# Lista para armazenar os dados coletados
data = []

# Loop para processar cada item
for url_name in item_list:
    try:
        # Obter informações do item (para ducats)
        item_url = f"{BASE_URL}/items/{url_name}"
        response = requests.get(item_url)
        response.raise_for_status()
        item_data = response.json()

        # Encontrar o item correto em items_in_set
        api_ducats = 0
        for set_item in item_data['payload']['item']['items_in_set']:
            if set_item['url_name'] == url_name:
                api_ducats = set_item.get('ducats', 0)
                break

        # Usar o dicionário estático como referência principal
        ducats = DUCATS_REFERENCE.get(url_name, api_ducats)

        # Log para depuração, comparando API com referência
        if api_ducats != ducats:
            print(f"Discrepância em {url_name}: API={api_ducats}, Referência={ducats}")
        else:
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