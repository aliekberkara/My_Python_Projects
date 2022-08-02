import time
import random
import sys

class Gamer():
    def __init__(self, name, life=5, energy=100):
        self.name = name
        self.life = life
        self.impact = 0
        self.energy = energy
    
    def view_current_status(self):
        print('impact: ', self.impact)
        print('life: ', self.life)
        print('energy: ', self.energy)
    
    def attack(self, opponent):
        print('You Have Made an Attack.')
        print('The Attack Continues. Please wait.')

        for i in range(10):
            time.sleep(.3)
            print('.', end='', flush=True)
        
        result = self.calculate_attack_result()

        if result == 0:
            print('\nRESULT: No Winning Party.')
        
        if result == 1:
            print('\nRESULT: You Hit Your Opponent.')
        
        if result == 2:
            print('\nRESULT: You Take a Hit From Your Opponent.')
    
    def calculate_attack_result(self):
        return random.randint(0, 2)
    
    def escape(self):
        print('Escaping...')
        for i in range(10):
            time.sleep(.3)
            print('\n', flush=True)
        
        print('Your Opponent Caught You')
    
    def bump(self, pounded):
        pounded.impact += 1
        pounded.energy -= 1
        if (pounded.impact % 5) == 0:
            pounded.life -= 1
        if pounded.life < 1:
            pounded.energy = 0
            print(f'{self.name} won the game.')
            self.game_exit()
        
    def game_exit(self):
        print('Exiting...')
        sys.exit()

#############################################


#Gamers

you = Gamer('Ali')
opponent = Gamer('Sena')

#Game Start

while True:
    print('Now you are facing your opponent.',
    'The Move You Want To Make:',
    'Attack: a',
    'Escape: e',
    'Quit: q', sep='\n')

    move = input('\n> ')
    if move == 'a':
        you.attack(opponent)
        print("Your Opponent's Status")
        opponent.view_current_status()

        print('Your Status')
        you.view_current_status()

    if move == 'e':
        you.escape()
    
    if move == 'q':
        you.game_exit()