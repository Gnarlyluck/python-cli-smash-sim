import random
import time 

class Character:
    def __init__(self, character):
        self.name = character['name']
        self.attacks = character['attacks']
        self.health = 100

    def smash(self, enemy):
        attack = random.choice(self.attacks)
        print(f'{self.name} used {attack["name"]} for {attack["damage"]} damage \n')
        hit_points = int(attack['damage'])
        enemy.minus_health(hit_points)
        if enemy.health <= 0:
            print(f'{enemy.name} has been knocked out!!\n')
        else:
            print(f'{enemy.name} has {enemy.health} HP left to fight with! \n')  
        return
        
    def minus_health(self, amount):
        self.health -= amount
       
class Battle:
    def __init__(self, user, a_i):
        
        self.user = user
        self.a_i = a_i
        self.turns()
        self.proclaim_winner()

    def turns(self):
        while self.user.health > 0 and self.a_i.health > 0:
            self.user.smash(self.a_i)
            time.sleep(2.5)
            if  self.a_i.health <= 0:
                return
            self.a_i.smash(self.user)
            if self.user.health <= 0:
                return
            time.sleep(2.5)

    def proclaim_winner(self):
        if self.a_i.health < 1:
            print(f'{self.user.name} has Defeated their enemy. Who will be the next contender?!')
        else:
            print(f'{self.a_i.name} says you were defeated by a measly A.I. How does it feel?!')


   