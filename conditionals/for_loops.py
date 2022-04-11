list_data = [1, 2, 3, 4, 5]
# embedded_list = [[1, 2, 3], [4, 5, 6]]
# dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.36"},
# 3: {"name": "Roscoe", "money": "$8.17"}}
#
# for data in embedded_list:
#     for element in data:
#         print(element)
#
# for item in dict_data.values():
#     print(item['money'])

for num in list_data:
    if num == 3:
        print("I've found 3")
    elif num > 3:
        print("I've gone too far")
    else:
        print("Too soon to find 3")