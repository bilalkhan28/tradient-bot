from indicators import analyze_bnb
import time

while True:
    print("\n📊 Checking BNB/USDT...")
    signal = analyze_bnb()
    print(signal)
    time.sleep(900)  # Wait for 15 minutes before next signal