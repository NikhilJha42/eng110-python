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

    except FileNameNotFoundError:
        print("File cannot be found or directory is wrong")
        raise
    finally:
        print("\n--Execution complete")

open_and_print_file("orders.txt")