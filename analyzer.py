def analyze_transactions(df):
    print(f"Total de transações: {len(df)}")
    print(f"Total recebido: {df[df['type'] == 'entrada']['amount'].sum():.8f} BTC")
    print(f"Total enviado: {df[df['type'] == 'saída']['amount'].sum():.8f} BTC")
    print("\nMaiores transações:")
    print(df.nlargest(5, 'amount'))