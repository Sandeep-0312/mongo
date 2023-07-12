import requests
from pymongo import MongoClient
api_url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h"
response = requests.get(api_url)
data = response.json()
formatted_data = []
for item in data:
    document = {
        "open_time": item[0],
        "open": item[1],
        "high": item[2],
        "low": item[3],
        "close": item[4],
        "volume": item[5],
        "close_time": item[6],
        "quote_asset_volume": item[7],
        "number_of_trades": item[8],
        "taker_buy_base_asset_volume": item[9],
        "taker_buy_quote_asset_volume": item[10],
        "ignore": item[11]
    }
    formatted_data.append(document)
client = MongoClient("mongodb+srv://sandyvicky0312:d4wl5UeYbc1nxKMZ@cluster0.23helxv.mongodb.net/") 
db = client["test"]  
collection = db["test"] 
collection.insert_many(formatted_data)
for document in collection.find():
    print(document)
