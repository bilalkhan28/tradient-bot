import requests
import ta
import pandas as pd

def fetch_binance_data(symbol="BNBUSDT", interval="15m", limit=100):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    data = requests.get(url).json()
    df = pd.DataFrame(data, columns=[
        "time", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base", "taker_buy_quote", "ignore"
    ])
    df["close"] = pd.to_numeric(df["close"])
    df["volume"] = pd.to_numeric(df["volume"])
    return df

def analyze_bnb():
    df = fetch_binance_data()

    # MACD
    macd = ta.trend.MACD(df["close"])
    macd_signal = macd.macd_diff().iloc[-1]

    # StochRSI
    stoch = ta.momentum.StochRSIIndicator(df["close"])
    k = stoch.stochrsi_k().iloc[-1]
    d = stoch.stochrsi_d().iloc[-1]

    advice = []

    # MACD Logic
    if macd_signal > 0:
        advice.append("📈 MACD: Bullish")
    else:
        advice.append("📉 MACD: Bearish")

    # StochRSI Logic
    if k < 20 and d < 20:
        advice.append("🟢 StochRSI: Oversold – Potential Buy Zone")
    elif k > 80 and d > 80:
        advice.append("🔴 StochRSI: Overbought – Potential Sell Zone")
    else:
        advice.append("⚖️ StochRSI: Neutral")

    return "\n".join(advice)