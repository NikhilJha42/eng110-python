def  open_and_print_file(file):
    try:
        opened_file = open(file, "r")
        file_line_list = opened_file.readlines()

        for line in file_line_list:
            print(line.rstrip("\n"))

        opened_file.close()
    
    except FileNameNotFoundError:
        print("File cannot be found or directory is wrong")
        raise

open_and_print_file("order.txt")