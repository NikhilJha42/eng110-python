list_of_nums = [i for i in range(1, 101)]

x_userinput = input("Pick a number between 1 and 100:")
y_userinput = input("Pick a second number between 1 and 100:")

valid_inputs = False

while valid_inputs == False:
    if x_userinput.isdigit() and y_userinput.isdigit():
        valid_inputs = True
    else:
        print("Please pick valid numbers:")
        x_userinput = input("Pick a number between 1 and 100:")
        y_userinput = input("Pick a second number between 1 and 100:")

x = int(x_userinput)
y = int(y_userinput)
xy_product = x*y
for num in list_of_nums:
    if num % xy_product == 0:
        print(num, "Fizzbuzz!")
    elif num % x == 0:
        print(num, "Fizz")
    elif num % y == 0:
        print(num, "Buzz")
    else:
        print(num)
