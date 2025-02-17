# Este é o ponto de entrada do seu programa.
# Contém a função main() e coordena o fluxo geral do programa.

from config import BITCOIN_API_URL
from api_client import get_address_data
from data_processor import process_transactions
from analyzer import analyze_transactions

DEFAULT_ADDRESS = "34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo"  # Endereço da Binance Cold Wallet

def main():
    try:
        address = input(f"Digite o endereço Bitcoin para rastrear (ou pressione Enter para usar o padrão - {DEFAULT_ADDRESS}): ")
        if not address:
            address = DEFAULT_ADDRESS
        
        data = get_address_data(address)
        if data:
            df = process_transactions(data)
            if not df.empty:
                analyze_transactions(df)
                df.to_csv(f"{address}_transactions.csv", index=False)
                print(f"\nDados salvos em {address}_transactions.csv")
            else:
                print("Nenhuma transação encontrada para este endereço.")
        else:
            print("Não foi possível obter dados para o endereço fornecido.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {str(e)}")

if __name__ == "__main__":
    main()