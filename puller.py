import requests
from datetime import datetime

def from_unix_to_date(time):
    return datetime.fromtimestamp(time / 1000).replace(microsecond=(time % 1000) * 1000)

symbol = 'BTCUSDT'
interval = '1s'

limit = 1000

url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"

response = requests.get(url)
data = response.json()

candlesticks = []
for d in data:
    candlestick = {
        'open_time': str(from_unix_to_date(d[0])),
        'open': float(d[1]),
        'high': float(d[2]),
        'low': float(d[3]),
        'close': float(d[4]),
        'close_time': str(from_unix_to_date(d[6]))
        #'open': from_unix_to_date(d[0]),
        #'close': from_unix_to_date(d[6])
    }
    candlesticks.append(candlestick)

for c in candlesticks:
    print(c)
print(from_unix_to_date(1718667745000))

#print(data)