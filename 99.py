# for i in range(1, 10):
#     for u in range(1, 10):
#         print(i,"x",u,"=",i*u)

# n = int(input("請輸入一個整數："))
# total = 0

# for i in range(1, n+1):
#     factorial = 1
#     for j in range(1, i+1):
#         factorial *= j
#     total += factorial
# print(total)

for i in range(1, 4):
	for j in range(1, 4):
		if j == 3:
			print(str(j) + '*' + str(i) + '=' + str(j*i))
		else:
			print(str(j) + '*' + str(i) + '=' + str(j*i), end = '\t')