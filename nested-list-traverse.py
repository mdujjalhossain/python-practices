
# market_item = [
#     ['potato', 'tomato', 'garlic'], [10, 20, 30], ['green-chilli', 50.50, 40]
# ]
# for item in market_item:
#     for nested_item in item:
#         print(nested_item, end =' ')
         
market_item = [
    ['potato', 'tomato', 'garlic'], [10, 20, 30], ['green-chilli', 50.50, 40]
]

row = 0
while row < len(market_item):
    col = 0
    while col < len(market_item[row]):
        print(market_item[row][col], end = ' ')
        col = col+1
    print()
    row += 1 