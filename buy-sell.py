price = int(input("請輸入商品售價："))
budget = int(input("請輸入購買預算："))
willness = input("請輸入購買意願(Y/N)：")
item = budget // price
cash = budget - (item*price)

if willness == "N":
    print("再見")
elif willness == "Y" and price > budget:
    print("預算不夠")
elif willness == "Y" and price <= budget:
    print(item, cash)