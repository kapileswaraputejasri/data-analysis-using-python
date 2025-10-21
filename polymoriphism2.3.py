class Animal:
    def make_sound(self):
        print("some animal sound")
class dog(Animal):
    def make_sound(self):
        print("woof")
class cat(Animal):
    def make_sound(self):
        print("meow")
class bird(Animal):
    def make_sound(self):
        print("tweet")
animals = [dog(),cat(),bird()]
for animal in animals:
    animal.make_sound()
