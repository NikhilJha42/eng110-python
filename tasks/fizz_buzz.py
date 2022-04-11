import random

random.seed()

list_of_nums = [random.randint(1, 1001) for i in range(1, 11)]
print(list_of_nums)

num_factor_1 = 3
num_factor_2 = 5
num_factor_product = num_factor_1*num_factor_2
for num in list_of_nums:
    if num % num_factor_product == 0:
        print(num, "Fizzbuzz!")
    elif num % num_factor_1 == 0:
        print(num, "Fizz")
    elif num % num_factor_2 == 0:
        print(num, "Buzz")
    else:
        print(num)
