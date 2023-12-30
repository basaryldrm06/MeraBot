def fetch_price(client, symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    if ticker:
        price = float(ticker['price'])
        return price
    return 0.0