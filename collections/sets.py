# Sets

utensils = {"fork", "knife", "spoon", "spatula"}
print(utensils, type(utensils))

utensils.add("garlic press")
print(utensils)
utensils.add("spoon")
print(utensils)
utensils.discard("fork")
print(utensils)

rep_list = [2, 5, 2, 4, 5, 2, 2, 4, 5, 4, 4, 4, 5, 5, 2, 3]
print(list(set(rep_list)))

x = frozenset([1, 2, 3, 4, 5])
print(type(x))