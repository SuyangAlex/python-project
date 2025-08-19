d1 = {}
d2 = dict()
print(d1, d2)

d1 = {"號碼":2, "身高":174}
print(d1)
print(d1['號碼'])
print(d1.get('身高'))

d = {'第一運動定律':'慣性定律',
    '第二運動定律':'加速度定律',
    '第三運動定律':'作用與反作用定律'}
print(d['第一運動定律'])
print(d.get('第二運動定律'))
# print(d['第四運動定律']) # Error


## 新增資料或更新 value
# d[key] = value
# d.update({key:value})

d = {}
d['李白'] = '太白'
print(d['李白'])
d.update({'李白':'青蓮居士'})
print(d['李白'])

## 刪除資料
# del d[key]
d = {'美國獨立':1776, '法國大革命':1789, '武昌起義':1911, '美西戰爭':1898}
del d['美西戰爭']
print(d)

# d.pop(key)：使用 pop method 的好處是他會回傳你要刪掉的那個 value
d = {'美國獨立':1776, '法國大革命':1789, '武昌起義':1911, '美西戰爭':1898}
k = d.pop('美國獨立')
print(k)
print(d)

# 字典的其他用法
capitals = {'台灣':'台北', '美國':'華盛頓', '土耳其':'安卡拉', '日本':'None', '澳洲':'坎培拉'}
print(len(capitals))
print(capitals.keys())

rocks = {'花崗岩':'火成岩', '礫岩':'沈積岩', '板岩':'變質岩', '玄武岩':'火成岩', '砂岩':'沈積岩'}
print(rocks.values())
print(rocks.items())

# 用字典跑迴圈
d = {'name':'Rebel Wilson', 'year':1980}
for key in d:
    print(key, d[key])
for key in d.keys():
    print(key, d[key])

for value in d.values():
    print(value)
for value in d:
    print(d[value], value)
for key, value in d.items():
    print(key, value)


# contacts book practice
contacts = {
    '小明':'0912345678',
    '小美':'0987654321'
}

contacts.update({'阿強':'0905710521'})
contacts.update({'小明':'0909876543'})
del contacts['小美']
print(contacts)
for key, value in contacts.items():
    print(key, value)


# vocab practice
vocab = {
    "apple": "蘋果",
    "book": "書",
    "cat": "貓"
}

if vocab.get('dog') == None:
    print('查無此單字')
else:
    print(vocab.get('dog'))

for key, value in vocab.items():
    print(key, '->', value)


# expenses practice
expenses = {
    "7/1 早餐": 50,
    "7/1 午餐": 100,
    "7/2 咖啡": 60,
    "7/3 晚餐": 200
}

total = 0
for value in expenses.values():
    total += value
print(total)

for key in expenses:
    if expenses[key] > 100:
        print(key)

expenses.update({'7/2 咖啡': 80})
expenses.update({'7/4 車費': 120})
for key, value in expenses.items():
    print(key, value)


# students scores
scores = {
    "Amy": 88,
    "Ben": 76,
    "Chris": 95,
    "Dora": 64
}

total = 0
for value in scores.values():
    total += value
average = total / len(scores)
print(average)

max = 0
min = 100
highest_student = ""
lowest_student = ""

for key in scores.keys():
    if int(scores[key]) > max:
        max = int(scores[key])
        highest_student = key

for key in scores.keys():
    if int(scores[key]) < min:
        min = int(scores[key])
        lowest_student = key

print(highest_student, lowest_student)

student_name = input("請輸入一個名字：")
if student_name in scores.keys():
    print(scores[student_name])
else:
    print('查無此人')

# 給定一段文字，統計每個字元出現幾次（用字典儲存）
text = input('請輸入一段文字：')
stat = {}
for index in text:
    if index in stat.keys():
        stat[index] += 1
    else:
        stat.update({index:1})
print(stat)