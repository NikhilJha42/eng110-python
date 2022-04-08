# # slicing: inclusive of first index and exculsive of last index;
# s = "Hello world!"
#
# slice = s[0:4]
# print(slice)
#
# # Grabbing every second character
# print(s[1:10:2])
#
# # reversing a string
# print(s[::-1])

# # String methods
#
# s0 = "EnGineering team 110"
# s1 = "#############Engineering team 110############"
#
# print(s0.capitalize())
# print(s1.strip('#'))
# print(s0.replace('e', 'ooo').upper().replace('E', 'OOOOO'))


# # F-strings = Formatted Strings
#
# a = "here is"
# b = " a string"
# c = " in parts"
#
# print(a + b + c)
# d = f"F-string: {a} {b} {c}."
# print(d)
#
# number = 10
# fruit = "apples"
#
# to_print = "There are " + str(number) + " " + fruit + "."
# print("str:", to_print)
#
# f_to_print = f"There are {number} {fruit}."
# print("F-string:", f_to_print)

# Input

name = input("What is your name?\n")
favourite_food = input("What is your favourite food?\n")
frequency = input(f"How many times a year do you eat (a) {favourite_food}?\n")
location = input(f"Where do you usually eat your {favourite_food}?\n")
answer = input(f"What is the answer?\n")
print(f"Hello, {name}. You eat your favourite food {favourite_food} {frequency} times a year, usually at {location}.\n"
      f"Your answer was \"{answer}\". How close was it to 42?")