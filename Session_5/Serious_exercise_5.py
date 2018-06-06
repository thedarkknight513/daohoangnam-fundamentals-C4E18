prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {

}

fruit_list = []

total = 0

stock["banana"] = 6
stock["apple"] = 0
stock["orange"] = 32
stock["pear"] = 15

for k in prices:
    added_item = prices[k]
    fruit_list.append(k)
print("Updated")

for i in range(len(fruit_list)):
    fruit_price = prices[fruit_list[i]]
    fruit_stock = stock[fruit_list[i]]
    print(fruit_list[i])
    print("Prices: ", fruit_price)
    print("Stock: ",fruit_stock)
    print("*"* 20)

for j in range(len(fruit_list)):
    total_prices = prices[fruit_list[j]] * stock[fruit_list[j]]
    print(fruit_list[j]," gives", total_prices)
    total += total_prices

print("The total you get is", total)


