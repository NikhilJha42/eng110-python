import csv

def transform_user_details(csv_file_name):
    new_user_data = []

    with open("user_details.csv", newline='') as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter=",")

        for user in user_details_csv:
            transformation = []
            transformation.append(user[1])
            transformation.append(user[2])
            transformation.append(user[-1])
            new_user_data.append(transformation)

    return new_user_data

print(transform_user_details("user_details.csv"))
# with open("user_details.csv", newline='') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
#
#     # print(csvreader)
#
#     # iterable_csv = iter(csvreader)
#     # next(iterable_csv) #Skips over column heading
#     # for row in csvreader:
#     #     print(row[-1])
#
#     print(list(csvreader))