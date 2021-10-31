import random

class Hero:
  def __init__(self, name, starting_health=100):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

  def fight(self, opponent):
    if random.randint(0,1) == 1:
      print(f"{self.name} destroys {opponent.name}!")
    else:
      print(f"{opponent.name} destroys {self.name}!")      

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)