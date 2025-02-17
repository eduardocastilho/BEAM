import requests
from config import BITCOIN_API_URL

def get_address_data(address):
    full_url = f"{BITCOIN_API_URL}{address}"
    print(f"Fazendo requisição para: {full_url}")
    response = requests.get(full_url)
    if response.status_code == 200:
        data = response.json()
        print(f"Dados recebidos. Número de transações: {len(data.get('txs', []))}")
        return data
    else:
        print(f"Erro ao obter dados: {response.status_code}")
        print(f"Resposta: {response.text}")
        return None