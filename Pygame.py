#creating our class
class Character:
    def __init__(self, name, attack, health):
        self.attack = attack
        self.name = name
        self.health = health

#creating our methods for actions + user interactivity w/game
    def damageH(self, enemy):
        self.health -= enemy.attack
        print(f"{self.name} is hit for {enemy.attack} your new health is {self.health}")

    
#Inheriting our parent class - Subclasses Hero and Vilain
class Hero(Character):
    def __init__(self, name, attack, health): 
        super().__init__(name,attack,health)
    
    def printStats(self):
        print(f"""
        name: {self.name}
        Attack: {self.attack}
        Health: {self.health}""")

class Vilain(Character):
    def __init__(self, name, attack, health): 
        super().__init__(name,attack,health)


#creating instances of our subclasses Hero and Vilain

Hulk = Hero("hulk", 10, 50)
Batman = Hero("batman", 8, 40)
Superman = Hero("superman", 9, 300)


Goblin = Vilain("goblin",9,15)
Zombie =  Vilain("zombie",10,25)
Monster = Vilain("monster",12, 30)
 

#create our Heroes + Vilains object List

Heroes = [Hulk,Batman,Superman]
Vilains = [Goblin, Zombie, Monster]



def GameStart():
    print(" Welcome to SuperHeroes Smackdown!!")
    print("This is the list of playable characters")
    for hero in Heroes:
        print(hero.name)
    heroChoice = input("""who do you want to play as?
    -->""" )
    if heroChoice.lower() == 'hulk':
        heroChoice = Hulk
    elif heroChoice.lower() == "batman":
        heroChoice = Batman
    elif heroChoice.lower() == "superman":
        heroChoice = Superman
    else:
        print('Only type in a playable character')

    print(f"you are now playing as {heroChoice.name}")

    print(f"watch Out {heroChoice.name}, you are now in a war zone")
    print("This is a list of all the ennemies on this land")
    for vilain in Vilains:
        print(vilain.name)
    vilainChoice = input("""who do you want to fight with ?
    -->""")
    if vilainChoice.lower() == "goblin":
        vilainChoice = Goblin
    elif vilainChoice.lower() == "zombie":
        vilainChoice = Zombie   
    elif vilainChoice.lower() == "monster":
        vilainChoice = Monster 
    else:
        print(" the vilain entered doesnt exist please choose from the one on this land"   ) 

    print(f"you choose to fight with {vilainChoice.name}")  
    print(f"Let the battle between {heroChoice.name} and {vilainChoice.name} begins")  







GameStart()
#create vilian select copy and paste hero select logic
#create fight function mennu called fightMenu
#have methods to attack/damage
#death logic if hero or enemy.health <0 what happens??
#quit logic/play again logic