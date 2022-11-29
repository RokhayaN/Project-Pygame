#creating our class
class Character:
    def __init__(self, name, attack, health):
        self.attack = attack
        self.name = name
        self.health = health

#creating our methods for actions + user interactivity w/game
    def damageH(self, enemy):
    
        enemy.health -= self.attack
        print(f"{enemy.name} is hit for {self.attack} their new health is {enemy.health}")

    
#Inheriting our parent class - Subclasses Hero and Vilain
class Hero(Character):
    def __init__(self, name, attack, health): 
        super().__init__(name,attack,health)
    
    def printStats(self):
        print(f"""
        name:   {self.name}
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



def displayFightMenu(heroChoice,vilainChoice):
    while (vilainChoice.health > 0):
        fightChoice = ''
        while fightChoice != 1 or fightChoice != 2 or fightChoice !=3 or fightChoice != 4:
            fightChoice = input(""" 
                    Press 1 to attack vilain
                    Press 2 to view character stats
                    Press 3 to reset game
                    Press 4 to quit game       
            -->""")


            if fightChoice == "1": 
                heroChoice.damageH(vilainChoice)
                #enemy attacks
            elif fightChoice == "2":
                heroChoice.printStats()
            elif heroChoice == "3":
                GameStart()  
            elif heroChoice == "4":
                quit()
            else:
                print('Please only choose from the options below!')
        print(f"{heroChoice.name} has won the battle!!")
        #
        playAgain = input("""Want to play again?  Y/N
        -->""")
        if playAgain.upper() == "Y":
            GameStart()
        elif playAgain.upper() == "N":
            print("Good Bye")
            quit()
        else:
            print('Please only choose from the options above')
    


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

    print("Here is our fight menu press any number below to choose an option")
    displayFightMenu(heroChoice, vilainChoice)







GameStart()

##add user control 
##whenever hero attacks have enemy automatically attack hero back
#have print hero health