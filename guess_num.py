ans = 72
num = int(input('請猜一個數字'))
while True:
	if ans > num:
		print('猜太低囉！')
		num = int(input('請猜一個數字'))
	elif ans < num:
		print('猜太高囉！')
		num = int(input('請猜一個數字'))
	else:
		print('恭喜答對！')
		break
	
lst = [1, 2, 6, 3, 5, 7, 9, 4, 8, 10]
new = []
for n in lst:
	if n == 4:
		continue
	else:
		new.append(n)
print(new)