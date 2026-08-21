class Dog:
    species = "animal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

cody = Dog("cody", 13)
cooper = Dog("cooper", 16)


print("Cody is a {}".format(cody.species))
print("Cooper is also a {}".format(cooper.species))

print("{} is {} years old".format( cody.name, cody.age))
print("{} is {} years old".format( cooper.name, cooper.age))