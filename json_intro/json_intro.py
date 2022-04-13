import json
# DON'T NAME ANY MODULES / DIRECTIORIES "JSON"

# JSON
# JavaScript Object Notation

car = {"make": "tesla",
       "engine": "electric",
       "faults": "lots",
       "is_expensive": True,
       "driver": None
       }

# json_dumps = json.dumps(car)
# print(json_dumps, type(json_dumps))

# dumps (pronounced dump-s) ==> take a dictionary and "dump" it as a string

# with open("car_json_file.json", "w") as jsonfile:
#     # print(jsonfile, type(jsonfile))
#     json.dump(car, jsonfile)

# with open("new_car_json_file.json", "r") as jsonfile:
#     new_car = json.load(jsonfile)
#
# print(new_car, type(new_car))

# Create a dictionary and write to a json file.
# Create a json file and read it in as a dictionary.

doom_coalition = {"Doctor": {"name": "Paul McGann", "number": 8},
                  "Companions": ["Liv Chenka", "Helen Sinclair"],
                  "Allies": ["River Song"],
                  "Enemies": ["The Eleven", "Calira", "The Clocksmith"],
                  "Episodes": 16
                  }

with open("doom_coalition_json_file.json", "w") as jsonfile:
    json.dump(doom_coalition, jsonfile)

with open("city_of_death.json", "r") as jsonfile:
    city_of_death = json.load(jsonfile)

print(city_of_death, type(city_of_death))