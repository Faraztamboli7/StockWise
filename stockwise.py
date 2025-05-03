import argparse
from fetcher import get_stock_info
from plotter import plot_stock_history

def main():
    parser = argparse.ArgumentParser(description="StockWise - Get stock info and price charts.")
    parser.add_argument("symbol", help="Stock symbol (e.g., AAPL, TSLA, INFY.NS)")
    parser.add_argument("--history", action="store_true", help="Show historical price chart")

    args = parser.parse_args()

    get_stock_info(args.symbol)

    if args.history:
        plot_stock_history(args.symbol)

if __name__ == "__main__":
    main()
