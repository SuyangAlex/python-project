import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# 下載 AAPL 股票資料
stock = yf.download("NVDA", start="2025-01-01", end="2025-06-30")

# 找出最高點和最低點
high_day = stock[stock['High'] == stock['High'].max()]
low_day = stock[stock['Low'] == stock['Low'].min()]

# 印出資訊
print("最高點資料：\n", high_day)
print("最低點資料：\n", low_day)

# 畫圖並標記最高 / 最低點
plt.figure(figsize=(10, 5))
stock['Close'].plot(label='收盤價', color='blue')

plt.scatter(high_day.index, high_day['Close'], color='red', label='最高點')
plt.text(high_day.index[0], high_day['Close'][0], '最高點', color='red')

plt.scatter(low_day.index, low_day['Close'], color='green', label='最低點')
plt.text(low_day.index[0], low_day['Close'][0], '最低點', color='green')

plt.title("AAPL 收盤價趨勢（含最高與最低點）")
plt.xlabel("日期")
plt.ylabel("收盤價")
plt.legend()
plt.grid(True)
plt.show()
