class Dog:
    animal_kind = "canine"

    def bark(self):
        return "woof"

fido = Dog()
lassie = Dog()

# Use multiple classes to define new instances, i.e., don't use the class
# Dog to create a dolphin.
print(type(fido))
print(type(lassie))
print(fido.animal_kind)
print(lassie.animal_kind)
print(fido.bark())
print(lassie.bark())
