# 判斷溫度是否開冷氣
def temperature(t):
    if t > 28:
        return f'現在溫度為 {t} 度，開冷氣'
    elif t < 15:
        return f'現在溫度為 {t} 度，開暖氣'
    else:
        return f'現在溫度為 {t} 度，不開冷暖氣'
temperature(26)

# 找零錢
def make_change(price):
    change = 100 - price # 計算找零
    result = []          # 用來存結果
    
    fifty = change // 50 # 幾個 50 元硬幣
    change %= 50         # 剩下多少

    ten = change // 10   # 幾個 10 元硬幣
    change %= 10         # 剩下多少

    five = change // 5   # 幾個 5 元硬幣
    change %= 5          # 剩下多少

    one = change         # 剩下的都是 1 元硬幣

    # 把結果存成字串
    result.append(f'50 元硬幣 {fifty} 枚')
    result.append(f'10 元硬幣 {ten} 枚')
    result.append(f'5 元硬幣 {five} 枚')
    result.append(f'1 元硬幣 {one} 枚')

    return "，".join(result)
print(make_change(33))

# 輸入月份，判斷季節
def season(month):
    if month == 1 or month == 2 or month == 12:
        return f'{month} 月為冬季'
    elif month == 3 or month == 4 or month == 5:
        return f'{month} 月為春季'
    elif month == 6 or month == 7 or month == 8:
        return f'{month} 月為夏季'
    elif month == 9 or month == 10 or month == 11:
        return f'{month} 月為秋季'
    else:
        return '請輸入 1~12 其中一個數字'
print(season(8))

# 計算停車費用
def parking_price(h):
    if h > 12:
        price = 12 * 40 + (h - 12) * 30
        return f'停車 {h} 小時，應繳 {price} 元'
    elif 0 <= h <= 12:
        price = h * 40
        return f'停車 {h} 小時，應繳 {price} 元'
    else:
        return '請輸入正整數'
print(parking_price(190))

# 秒數轉換
def times(second):
    # 預設值，避免沒被指定就報錯
    hour = 0
    minutes = 0
    seconds = 0

    # 如果大於等於一小時，先算小時
    if second >= 3600:
        hour = second // 3600
        second = second % 3600 # 剩下秒數
    
    # 如果大於等於一分鐘，再算分鐘
    if second >= 60:
        minutes = second // 60
        second = second % 60 # 剩下秒數
    
    # 剩下的就是秒數
    seconds = second

    return f"{hour*3600 + minutes*60 + seconds} 秒等於 {hour:02d} 小時 {minutes:02d} 分 {seconds:02d} 秒"
print(times(14865))