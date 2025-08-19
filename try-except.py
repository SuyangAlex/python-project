# 數字除法小工具
num1 = int(input("請輸入被除數："))
num2 = int(input("請輸入除數："))
try:
    result = num1 / num2
    print('結果是：', result)
except ZeroDivisionError:
    print('除數不能為0！')


# 轉換數入成整數
user_input = input("請輸入一個數字：")
try:
    num = int(user_input)
    print("平方是：", num ** 2)
except ValueError:
    print('請輸入正確的數字')


# 簡易加法器（重複輸入直到正確）
while True:
    num1 = input('請輸入第一個值：')
    num2 = input('請輸入第二個值：')
    try:
        result = int(num1) + int(num2)
        print(result)
        break # 輸入正確，跳出 while 迴圈
    except ValueError:
        print('請輸入正確的值')


# 發票兌獎（結合字典 + try）
awards = {
    "特別獎": "12345678",
    "特獎": "87654321",
}
user_input = input("請輸入你的發票號碼：")

try:
    if len(user_input) != 8:
        raise ValueError('長度錯誤')

    num = int(user_input)
    is_winner = False
    for value in awards.values():
        if num == int(value):
            is_winner = True
            break
    
    if is_winner:
        print('恭喜中獎！獎項是'+awards[user_input])
    else:
        print('可惜沒有中獎')

except ValueError:
    print('請輸入正確的 8 碼數字')