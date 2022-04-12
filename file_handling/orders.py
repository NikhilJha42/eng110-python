def  open_and_print_file(file):
    try:
        with open(file, "r") as file:
            for line in file.readlines():
                print(line.rstrip('\n'))

        # opened_file = open(file, "r")
        # file_line_list = opened_file.readlines()
        #
        # print(file_line_list)
        #
        # for line in file_line_list:
        #     print(line.rstrip("\n"))
        #
        # opened_file.close()

    except FileNotFoundError:
        print("File cannot be found or directory is wrong")
        raise
    finally:
        print("\n--Execution complete\n")

def write_to_file(file, order_item):
    try:
        with open(file, "a") as file:
            file.write(order_item + '\n')
    except FileNotFoundError:
        print("File not found")
        raise
    finally:
        print("\n--Execution complete\n")

write_to_file("orders.txt", "This works?")

open_and_print_file("orders.txt")