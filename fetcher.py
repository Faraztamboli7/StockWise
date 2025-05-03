import yfinance as yf

def get_stock_info(symbol):
    stock = yf.Ticker(symbol)
    info = stock.info

    print(f"\n📊 Stock: {info.get('longName', symbol)}")
    print(f"➡️ Current Price: ₹{info.get('currentPrice')}")
    print(f"🏢 Market Cap: {info.get('marketCap')}")
    print(f"📈 P/E Ratio: {info.get('trailingPE')}")
    print(f"🗓️ 52-Week High: ₹{info.get('fiftyTwoWeekHigh')}")
    print(f"🗓️ 52-Week Low: ₹{info.get('fiftyTwoWeekLow')}")
    print()
