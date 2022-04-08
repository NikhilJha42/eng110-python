# Dictionaries

# Key-value pairs

# me = {
#     "name": "Jha, Nikhil",
#     "job": "Trainee Spartan",
#     "age": 22
# }
#
# print(me["job"])
#
# # DICTIONARY NAME [ KEY ]
#
# me["favourite_food"] = "pizza"
#
# print(me)
#
# print(me.get("name"))
# me.update({"name": "Jha, Nikhil Jha", "favourite_food": "chocolate mousse"})
#
# print(me)
#
# print(me.get(height))

film = {
    "title": "Doctor Who: The TV Movie",
    "screenwriter": "Mathew Jacobs",
    "director": "Geoffrey Sax",
    "executive_producers": ["Alex Beaton", "Philip Segal", "Jo Wright"],
    "release_year": 1996,
    "age_certificate": 12,
    "language": "English",
    "run_time": 85,
    "main_actors": ["Paul McGann", "Daphne Ashbrook", "Yee Jee Tso", "Eric Roberts"],
    "villain": {
        "name": "The Master",
        "species": "Time Lord (inhabiting human body)"
    }
}

print(film.keys()) # Keys
print(film.values()) # Values
print(film.items()) # List of tuples of key-value pairs