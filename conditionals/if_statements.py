film_rating = "15"

if film_rating.lower() == "universal":
    print("all age groups can watch this file")
elif film_rating.lower() == "pg":
    print("General viewing, but some scenes may be unsuitable for young children")
elif film_rating.lower() == "15":
    print("No one younger than 15 may see a 15 film in the cinema")
elif film_rating.lower() == "18":
    print("No one younger than 18 may see an 18 film in a cinema")
else:
    print("Unknown rating")
