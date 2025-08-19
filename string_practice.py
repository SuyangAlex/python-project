print(type('python'))

# 換行：\n
# TAB：\t
# 雙引號：\"
# 單引號：\'
# 反斜線：\\

print('I love ' + 'programming')
print('啊 ' + '好像棋盤似的')

str = '很重要所以說3遍！'
print(str * 3) # 重複字串的倍數必須是 Int

# 計算字串長度：len(字串)
# a = input()
# b = input()
# print(len(a))
# print(len(b))
# print(len(a+b))

# 字串－索引值


# 字串切割 - Slicing：字鑽[起始位置:結束位置:間隔值]
# 切割出的內容會包含起始位置、不包含結束位置
s = 'python'
print(s[1:5:2])
print(s[0:-1])