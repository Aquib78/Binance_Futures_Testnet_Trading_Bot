from binance.client import Client
from dotenv import load_dotenv
import os
import time

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

client = Client(api_key, api_secret)

# Binance Futures Testnet
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

# Synchronize timestamp with Binance server
server_time = client.get_server_time()
client.timestamp_offset = (
    server_time["serverTime"] - int(time.time() * 1000)
)

print("Connected to Binance Futures Testnet")