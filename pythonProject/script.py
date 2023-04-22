class Animal(object):
    def __init__(self, age, name):
        self.age = age
        self.name = None


    def get_age(self):
        return self.age

    def get_name(self):
        return self.name
    def set_name(self, name=""):
        self.name = name

    def set_age(self, new_age):
        self.age = new_age

    def __str__(self):
        return f"animal: {self.name}, varsta {self.age}"

a = Coordinate(1, 2)
print(a)
