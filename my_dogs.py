import dog

class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
    print("dog initialized!")

  def bark(self):
    print("Woof!")



my_dog = dog.Dog("Rex", "SuperDog")
my_dog.bark()

my_other_dog = dog.Dog("Annie", "SuperDog")
print(my_other_dog.name) 