#!/usr/bin/env python
# coding: utf-8

# In[20]:


# Soldier
import random

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self): 
        return self.strength 

    def receiveDamage(self, damage):
        self.health -= damage 


# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"


# War
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        if not self.vikingArmy or not self.saxonArmy:
            return None
        # Choose random Viking and Saxon
        attacker = random.choice(self.vikingArmy)
        defender = random.choice(self.saxonArmy)

        result = defender.receiveDamage(attacker.attack())

        # Remove dead Saxons
        self.saxonArmy = [s for s in self.saxonArmy if s.health > 0]

        return result

    def saxonAttack(self):
        if not self.vikingArmy or not self.saxonArmy:
            return None
        # Choose random Viking and Saxon
        attacker = random.choice(self.saxonArmy)
        defender = random.choice(self.vikingArmy)

        result = defender.receiveDamage(attacker.attack())

        # Remove dead Vikings
        self.vikingArmy = [v for v in self.vikingArmy if v.health > 0]

        return result

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."



# In[ ]:




