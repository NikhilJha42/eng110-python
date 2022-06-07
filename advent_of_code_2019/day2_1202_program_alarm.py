# Intcode = list of integers
# Begins with opcode: 1, 2 or 99.
# 99 means program is finished and should immediately halt.
# 1 add together numbers read from two positions and stores
# the result in a third position.
# The three integers immediately after the opcode tell you these three positions
# The first two indicate the postions for the input values, and the third indicates
# the position the output should be stored at.
# Opcode 2 works the same as 1, except with multiplication.
# Once you've processed an opcode, move forward 4 places.

def process_opcode(intcode: list, start_index: int):
    opcode = intcode[start_index]
    if opcode == 1:
        num1 = intcode[start_index + 1]
        num2 = intcode[start_index + 2]
        total = num1 + num2
        intcode[intcode[start_index + 3]] = total
    elif opcode == 2:
        num1 = intcode[start_index + 1]
        num2 = intcode[start_index + 2]
        total = num1 * num2
        intcode[intcode[start_index + 3]] = total
    elif opcode == 99:
        return False
    return intcode

# # Need to know how to convert .txt to list in Python
# with open("day2_challenge1_input.txt", "r") as intcode:
#     data = list(intcode)
#     data[1] = 12
#     data[2] = 2
#     start = 0
#     processing = process_opcode(data, start)
#     while processing != False:
#         start += 4
#         process_opcode(data, start)
#     print(data[0])
