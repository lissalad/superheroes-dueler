from os import name
from ability import Ability
from armor import Armor
from weapon import Weapon
import random


class Hero:
  def __init__(self, name, starting_health=100):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health
    self.abilities = list()
    self.armors = list()

# ---------- CUSTOMIZE HERO ----------------------- #
  def add_ability(self, ability):
    self.abilities.append(ability)

  def add_armor(self, armor):
    self.armors.append(armor)

  def add_weapon(self, weapon):
    self.abilities.append(weapon)


# ----------------------------------------------- #
  def is_alive(self):
    if self.current_health <= 0:
      return False
    return True

  # ---------- ACTIONS ----------------------- #

  def fight(self, opponent):
    if random.randint(0,1) == 1:
      winner=self.name  
    else:
      winner=opponent.name  
    print(f"{winner} destroys {self.name}!")      
   
  def attack(self):
    total_damage = 0
    for ability in self.abilities:
      total_damage += ability.attack()
    return total_damage

  def defend(self):
    total_block = 0
    for armor in self.armors:
      total_block += armor.block() # HELP 
      print("help")
    return total_block

  def take_damage(self, damage):
    hurt = damage - self.defend()
    # print(damage)
    # print(hurt)
    self.current_health = self.current_health - hurt

# ----------  FIGHT ----------------------- #
  def fight(self, opponent):
    if len(self.abilities)==0 and len(opponent.abilities)==0:
      print("Draw!")
    else:
      won = False
      while not won:
        opponent.take_damage(self.attack())
        # print(opponent.current_health)
        if not opponent.is_alive():
          print(f"{self.name} won!")
          won = True;
          break
        self.take_damage(opponent.attack())
        if not self.is_alive():
          print(f"{opponent.name} won!")
          won = True;
          break

# ---------- RUN ----------------------- #
if __name__ == "__main__":

    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())

  # ability = Ability("Great Debugging", 50)
  # another_ability = Ability("Smarty Pants", 90)
  # hero = Hero("Grace Hopper", 200)
  # hero.add_ability(ability)
  # hero.add_ability(another_ability)
  # print(hero.attack())

  # hero = Hero("Grace Hopper", 200)
  # shield = Armor("Shield", 50)
  # hero.add_armor(shield)
  # hero.take_damage(50)
  # print(hero.current_health)

  # hero = Hero("Grace Hopper", 200)
  # hero.take_damage(150)
  # print(hero.is_alive())
  # hero.take_damage(15000)
  # print(hero.is_alive())

  # hero1 = Hero("Wonder Woman")
  # hero2 = Hero("Dumbledore")
  # ability1 = Ability("Super Speed", 30)
  # ability2 = Ability("Super Eyes", 60)
  # ability3 = Ability("Wizard Wand", 80)
  # ability4 = Ability("Wizard Beard", 20)
  # hero1.add_ability(ability1)
  # hero1.add_ability(ability2)
  # hero2.add_ability(ability3)
  # hero2.add_ability(ability4)
  # hero1.fight(hero2)  

  # ability = Ability("Great Debugging", 50)
  # hero = Hero("Grace Hopper", 200)
  # hero.add_ability(ability)
  # print(hero.abilities)

  # ability2 = Ability("Kindness", 3000)
  # hero.add_ability(ability2)
  # print(hero.abilities)

  # hero1 = Hero("Wonder Woman")
  # hero2 = Hero("Dumbledore")

  # hero1.fight(hero2)

  # ability = Ability("Debugging Ability", 20)
  # print(ability.name)
  # print(ability.attack())
  
  # armor = Armor("Debugging Shield", 10)
  # print(armor.name)
  # print(armor.block())
  