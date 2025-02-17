import pandas as pd
from datetime import datetime

def process_transactions(data):
    transactions = []
    for tx in data.get('txs', []):
        time = tx.get('time', 0)
        
        # Process inputs
        for input in tx.get('inputs', []):
            prev_out = input.get('prev_out', {})
            if prev_out.get('addr') == data.get('address'):
                transactions.append({
                    'timestamp': datetime.fromtimestamp(time),
                    'type': 'saída',
                    'amount': prev_out.get('value', 0) / 100000000,  # Convertendo satoshis para BTC
                    'to_address': tx.get('out', [{}])[0].get('addr', 'Unknown')
                })
        
        # Process outputs
        for output in tx.get('out', []):
            if output.get('addr') == data.get('address'):
                transactions.append({
                    'timestamp': datetime.fromtimestamp(time),
                    'type': 'entrada',
                    'amount': output.get('value', 0) / 100000000,
                    'from_address': tx.get('inputs', [{}])[0].get('prev_out', {}).get('addr', 'Unknown')
                })
    
    return pd.DataFrame(transactions)