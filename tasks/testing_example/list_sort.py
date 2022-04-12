def list_sort(list_of_nums, type):
    if type == "asc":
        return sorted(list_of_nums)
    elif type == "desc":
        return sorted(list_of_nums, reverse=True)
    elif type == "none":
        return list_of_nums
    else:
        return "Unknown keyword"