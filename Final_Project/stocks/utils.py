import os
import requests
from decouple import config
from .models import Stock

from google import genai
import os
from decouple import config

API_KEY_GEMINI = config("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY_GEMINI)

API_KEY_STOCKS = config("ALPHA_VANTAGE_API_KEY")
BASE_URL = "https://www.alphavantage.co/query"

def update_stock_data(stock):
    """
    Updates the current price and market cap of a Stock instance using Alpha Vantage.
    """
    # 1. Get current price using Global Quote
    params_price = {
        "function": "GLOBAL_QUOTE",
        "symbol": stock.symbol,
        "apikey": API_KEY_STOCKS
    }
    response_price = requests.get(BASE_URL, params=params_price)
    data_price = response_price.json().get("Global Quote", {})

    price = data_price.get("05. price")
    if price:
        stock.current_price = float(price)

    # 2. Get market capitalization using Overview
    params_overview = {
        "function": "OVERVIEW",
        "symbol": stock.symbol,
        "apikey": API_KEY_STOCKS
    }
    response_overview = requests.get(BASE_URL, params=params_overview)
    data_overview = response_overview.json()

    market_cap = data_overview.get("MarketCapitalization")
    if market_cap:
        stock.market_cap = float(market_cap)

    # Save updated data
    stock.save()


def generate_ai_summary(stock):
    prompt = f"Describe in 3 words what this company does: {stock.company_name}. Description: {stock.description}"
    response = client.models.generate_content(model='gemini-2.5-flash',contents=prompt)
    return response.text.strip()
