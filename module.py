import math
import random

# 使用 math 模組計算圓面積
radius = int(input('請輸入圓的半徑：'))
result = math.pi * (radius**2)
print(result)


# 使用 random 模組寫猜數字遊戲
num = random.randint(1, 10)

while True:
    try:
        a = int(input('請從 1~10 猜一個數字：'))

        if a < 1 or a > 10:
            print('請輸入 1 到 10 之間的整數')
            continue

        if num == a:
            print('恭喜中獎！')
            break
        elif num < a:
            print('猜低一點試試')
        else:
            print('猜高一點試試')
    except ValueError:
        print('請輸入數字')

import BMI
result = BMI.bmi(1.75, 90)
print(result)