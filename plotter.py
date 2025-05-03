import yfinance as yf
import matplotlib.pyplot as plt

def plot_stock_history(symbol):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="6mo")

    hist['Close'].plot(title=f"{symbol} - 6 Month Closing Price")
    plt.xlabel("Date")
    plt.ylabel("Close Price (₹)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
