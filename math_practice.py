import math

print(abs(-121)) # abs(a) -> 計算 a 的絕對值
print(round(4.2553, 1)) # round(a, p) -> 將 a 四捨五入到小數 p 位。如果 p 沒填，則取到整數。
print(pow(2, 1024)) # 計算 a 的 b 次方
l1 = [1, 3, 5, 6, 9]
print(min(l1)) # 取最小值
print(max(l1)) # 取最大值

print(math.inf*0)
print(math.factorial(50))
print(math.ceil(9.1)) # ceil(a) 找出比 a 大的最小整數
print(math.floor(9.1)) # floor(a) 找出比 a 小的最大整數

print(f'{l1}這是一個串列')
print([n**2 for n in l1])

def clip(lst, min_, max_):
    new_lst = []
    for n in lst:
        if n < min_:
            new_lst.append(min_)
        elif n > max_:
            new_lst.append(max_)
        else:
            new_lst.append(n)
    return new_lst

lst = clip([-24, -17, -5, 0, 2, 4, 7, 9, 44], -3, 20)
print(lst)

def remove_negative2(set1):
    set2 = set1.copy()
    neg = [i for i in set2 if i<0]
    for e in neg:
        set2.remove(e)
    return set2

s1 = {1, 3, 4, -2, -5}
s2 = remove_negative2(s1)

print(s1, s2)

x = 12
def fun():
    global x
    x += 1
    print(x)

fun()

def fact(n):
    if n > 1:
        return n*fact(n-1)
    else:
        return 1

print(fact(4))
