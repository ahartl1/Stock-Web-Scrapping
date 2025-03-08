def scrape_stock(ticker_symbol: Any) -> Dict[str, Any]:
    print('Getting stock data of', ticker_symbol)
    headers = {
    'User-Agent': useragent,
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/',
    }
    url = f'https://finance.yahoo.com/quote/{ticker_symbol}'

    session = requests.Session()
    session.headers.update(headers)
    
    r = session.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    if r.status_code != 200:
        print("Cannot reach",ticker_symbol)
    else:
        stock = {
        'stock_name': soup.find('h1', {'class': 'yf-xxbei9'}).text.strip(),
        'regularMarketPrice': soup.find('span', {'data-testid': 'qsp-price'}).text.strip(),
        'regularMarketChange': soup.find('span', {'data-testid': 'qsp-price-change'}).text.strip(),
        'regularMarketChangePercent': soup.find('span', {'data-testid': 'qsp-price-change-percent'}).text.strip(),
        
        'previous_close': soup.find('span', {'title': 'Previous Close'}).find_next_sibling('span').text.strip(),
        'open_value': soup.find('span', {'title': 'Open'}).find_next_sibling('span').text.strip(),
        'bid': soup.find('span', {'title': 'Bid'}).find_next_sibling('span').text.strip(),
        'ask': soup.find('span', {'title': 'Ask'}).find_next_sibling('span').text.strip(),
        'days_range': soup.find('span', {'title': 'Day\'s Range'}).find_next_sibling('span').text.strip(),
        'week_range': soup.find('span', {'title': '52 Week Range'}).find_next_sibling('span').text.strip(),
        'volume': soup.find('span', {'title': 'Volume'}).find_next_sibling('span').text.strip(),
        'avg_volume': soup.find('span', {'title': 'Avg. Volume'}).find_next_sibling('span').text.strip(),
        'market_cap': soup.find('span', {'title': 'Market Cap (intraday)'}).find_next_sibling('span').text.strip(),
        'beta': soup.find('span', {'title': 'Beta (5Y Monthly)'}).find_next_sibling('span').text.strip(),
        'pe_ratio': soup.find('span', {'title': 'PE Ratio (TTM)'}).find_next_sibling('span').text.strip(),
        'eps': soup.find('span', {'title': 'EPS (TTM)'}).find_next_sibling('span').text.strip(),
        'earnings_date': soup.find('span', {'title': 'Earnings Date'}).find_next_sibling('span').text.strip(),
        'dividend_yield': soup.find('span', {'title': 'Forward Dividend & Yield'}).find_next_sibling('span').text.strip(),
        'ex_dividend_date': soup.find('span', {'title': 'Ex-Dividend Date'}).find_next_sibling('span').text.strip(),
        'year_target_est': soup.find('span', {'title': '1y Target Est'}).find_next_sibling('span').text.strip()}
    return stock

useragent = input("Enter user agent:")
ticker_symbols = input("Enter ticker symbols seperated by a space (e.g. \"TSLA AMZN AAPL\"):").split()
stockdata = [scrape_stock(symbol) for symbol in ticker_symbols]

with open('stock_holder_data.json', 'w', encoding='utf-8') as f:
    json.dump(stockdata, f)

with open('stock_holder_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = stockdata[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(stockdata)

df = pd.DataFrame(stockdata)
df.to_excel('stock_holder_data.xlsx', index=False)

print('Done!')
