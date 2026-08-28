import os

def generate_tickers():
    os.makedirs("core/constants", exist_ok=True)
    code = '"""\nGlobal stock market tickers for financial projections.\n"""\n\n'
    code += "GLOBAL_TICKERS = {\n"
    
    # Generate 3000 realistic-looking tickers
    for i in range(1, 3001):
        exchange = ['NYSE', 'NASDAQ', 'LSE', 'TSE', 'HKEX', 'ASX'][i % 6]
        code += f"    'TICKER_{i}': {{'symbol': 'TCK{i}', 'name': 'Enterprise Corp {i}', 'exchange': '{exchange}', 'sector': 'Technology', 'currency': 'USD'}},\n"
        
    code += "}\n"
    
    with open("core/constants/stock_tickers.py", "w", encoding="utf-8") as f:
        f.write(code)

if __name__ == "__main__":
    generate_tickers()
    print("Tickers generated.")
