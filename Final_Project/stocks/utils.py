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
    try:
        prompt = f"Describe in 3 words what this company does: {stock.company_name}. Description: {stock.description}"
        response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
        return response.text.strip()
    except Exception as e:
        error_msg = str(e)
        print(f"DEBUG: AI summary failed: {error_msg}")

        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg or "quota" in error_msg.lower():
            return f"🤖 AI quota exceeded. {stock.company_name} is in the {stock.description[:50]}... sector. Try again in a few minutes!"
        else:
            return f"AI analysis temporarily unavailable. {stock.company_name} operates in: {stock.description[:100]}..."


def get_stock_news_fast(stock_symbol):
    """
    Get latest news for a specific stock - ALWAYS WORKS version
    """
    # Always return fallback first for testing
    fallback = get_fallback_news(stock_symbol)

    # Try Alpha Vantage API if available
    try:
        params = {
            "function": "NEWS_SENTIMENT",
            "tickers": stock_symbol,
            "apikey": API_KEY_STOCKS,
            "limit": 3
        }

        response = requests.get(BASE_URL, params=params, timeout=5)

        if response.status_code == 200:
            data = response.json()

            # Check for API errors or limits
            if "Error Message" in data:
                return fallback

            if "Note" in data:
                return fallback

            # Try to extract news
            if "feed" in data and data["feed"]:
                news_articles = []
                for article in data["feed"][:3]:
                    news_articles.append({
                        "title": article.get("title", "No title"),
                        "summary": article.get("summary", "No summary available")[:200] + "...",
                        "url": article.get("url", "#"),
                        "time_published": article.get("time_published", ""),
                        "source": article.get("source", "Unknown"),
                        "sentiment_score": article.get("overall_sentiment_score", 0)
                    })

                if news_articles:
                    return news_articles

        return fallback

    except Exception as e:
        return fallback


def get_fallback_news(stock_symbol):
    """
    Fallback: Real financial links when API is unavailable
    """
    return [
        {
            "title": f"📊 View {stock_symbol} Live Financial Data",
            "summary": f"Get real-time stock price, charts, financial statements, and analyst ratings for {stock_symbol}. Comprehensive market data and trading information available.",
            "url": f"https://finance.yahoo.com/quote/{stock_symbol}",
            "time_published": "Live Data",
            "source": "Yahoo Finance",
            "sentiment_score": 0.0
        },
        {
            "title": f"📈 {stock_symbol} Market Analysis & News",
            "summary": f"Latest market analysis, financial news, and expert opinions about {stock_symbol}. Includes recent earnings reports, analyst recommendations, and market trends.",
            "url": f"https://www.marketwatch.com/investing/stock/{stock_symbol.lower()}",
            "time_published": "Real-time",
            "source": "MarketWatch",
            "sentiment_score": 0.0
        }
    ]


# Keep old function for compatibility
def get_stock_news(stock_symbol):
    return get_stock_news_fast(stock_symbol)


def generate_news_summary_fast(news_articles):
    """
    Generate FAST AI summary of recent news using Gemini
    """
    if not news_articles:
        return "No recent news available."

    try:
        # Create comprehensive news summary for AI analysis
        news_content = ""
        for i, article in enumerate(news_articles[:3], 1):
            news_content += f"\nNews {i}:\n"
            news_content += f"Title: {article['title']}\n"
            news_content += f"Summary: {article['summary'][:150]}...\n"
            if article.get('sentiment_score'):
                sentiment = "Positive" if article['sentiment_score'] > 0 else "Negative" if article['sentiment_score'] < 0 else "Neutral"
                news_content += f"Sentiment: {sentiment}\n"
        
        prompt = f"""Based on these recent financial news, provide a single sentence investment insight:
        {news_content}
        
        Respond in one clear sentence that summarizes the overall market sentiment and potential stock impact."""

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )

        result = response.text.strip()
        return result

    except Exception as e:
        error_msg = str(e)

        # Check if it's a quota error
        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg or "quota" in error_msg.lower():
            return f"🤖 AI Summary temporarily unavailable (quota exceeded). The news analysis shows recent market activity - check the links above for detailed financial information and real-time data."
        elif "quota" in error_msg.lower():
            return f"🤖 AI quota exceeded for this hour. Try again later, or check the news links above for real-time analysis."
        else:
            return f"📊 AI analysis temporarily unavailable. For comprehensive market analysis, check the financial data links above which provide recent news, analyst ratings, and trading activity."


# Keep old function for compatibility
def generate_news_summary(news_articles):
    return generate_news_summary_fast(news_articles)