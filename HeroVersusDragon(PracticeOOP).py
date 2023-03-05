class ColorsForPrint:
    WHITE = '\033[00m'
    GREEN = '\033[0;92m'
    RED = '\033[1;31m'

class Character(ColorsForPrint):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def Attack(self, opponent):
        print(f'{Character.GREEN} Hero HP: {self.health} \nDragon HP: {opponent.health}{Character.WHITE}')
        opponent.health -= self.strength
        print(f'{Character.RED}The {self.name} attacks the {opponent.name} and deals them {self.strength} damage.{Character.WHITE}')
        


def main(): 

    hero = Character('Hero', 200, 50) 

    dragon = Character('Dragon', 500, 15) 

    while hero.health > 0 and dragon.health > 0:

        hero.Attack(dragon)

        dragon.Attack(hero)



    if hero.health > 0:
        print(f'{hero.name} has won!')
    else:
        print(f'{dragon.name} has won!')


if __name__ == '__main__': 
    main()    
    