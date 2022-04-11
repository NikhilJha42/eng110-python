# x = 0
#
# while x < 10:
#     print(f"It's working -> {x}")
#     if x == 4:
#         break
#     x += 1

user_prompt = True

while user_prompt:
    age = input("What is your age?")
    if age.isdigit():
        if int(age) >= 13 and int(age) < 117:
            print(f"Your age is {age}. You may watch this video.")
        else:
            print(f"Your age is {age}. You must be over 13 to watch this video.")
        user_prompt = False
    else:
        print("Please enter a valid age below:")