from ability import Ability
from armor import Armor
import random


class Hero:
  def __init__(self, name, starting_health=100):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health
    self.abilities = list()
    self.armors = list()

  def fight(self, opponent):
    if random.randint(0,1) == 1:
      print(f"{self.name} destroys {opponent.name}!")
    else:
      print(f"{opponent.name} destroys {self.name}!")      

  def add_ability(self, ability):
    self.abilities.append(ability)

if __name__ == "__main__":
  ability = Ability("Great Debugging", 50)
  hero = Hero("Grace Hopper", 200)
  hero.add_ability(ability)
  print(hero.abilities)
  hero1 = Hero("Wonder Woman")
  hero2 = Hero("Dumbledore")

  hero1.fight(hero2)

  ability = Ability("Debugging Ability", 20)
  print(ability.name)
  print(ability.attack())
  
  armor = Armor("Debugging Shield", 10)
  print(armor.name)
  print(armor.block())
  