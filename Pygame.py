#creating our class
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

#Inheriting our parent class - Subclasses Hero and Vilain
class Hero(Character):
    def __init__(self, name, health): 
        super().__init__(name,health)


class Vilain(Character):
    def __init__(self, name, health): 
        super().__init__(name,health)

#create our Heroes + Vilains List

Heroes = ["Hulk", "Batman", "Spiderman"]
Vilains = ["Goblin","Zombie","Monster"]

#creating instances of our subclasses Hero and Vilain

Hulk = Hero("hulk", 10)
Batman = Hero("batman", 8)
Superman = Hero("Superman", 9)


Goblin = Vilain("goblin",9)
Zombie =  Vilain("zombie",10)
Monster = Vilain("monster",12)
 