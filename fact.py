def f(m):
	if m == 0:
		return 0
	elif m == 1:
		return 1
	else:
		return f(m-1)+f(m-2)
num = int(input())
print(f(num))