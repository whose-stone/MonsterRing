import random 

WATER_BODY = ('\033[34m           \n   ^  ^   \n    @     \n  /   \\ \n    JL    \n\033[0m')
EARTH_BODY = ('\033[32m          \n   *  *   \n   -$-    \n  <~~>    \n   000    \n\033[0m')
FIRE_BODY = ('\033[31m          \n   )  (   \n   00    \n  ###     \n  {] [}    \n\033[0m')



#create the creatures that will fight
class Creature:
    def __init__(self, name, life, attacks, creature_type, train_level = 1, train_count = 0, win_loss=(0,0)):
        self.name = name
        self.life = life
        self.attacks = attacks
        self.type = creature_type
        self.train_up = train_level
        self.train_count = train_count
        self.record = win_loss

    def set_name(self, name):
        self.name = name
    
    def set_life(self, life):
        self.life = life

    def set_attacks(self, attacks):
        self.attacks = attacks

    def get_name(self):
        return self.name
    
    def get_life(self):
        return self.life
    
    def get_attacks(self):
        return self.attacks
    
    def train(self):
        self.train_count += 1
        self.train_up += 1
        self.attacks = {name: dmg + 1 for name, dmg in self.attacks.items()}
        print(f"{self.name} trained! Level {self.train_up}, attacks powered up.")

    def attack(self, opponent, move=None):
        if move is None:
            move = random.choice(list(self.attacks.keys()))
        if move not in self.attacks:
            print(f"{self.name} doesn't know {move}!")
            return
        
        damage = self.attacks[move]
        print(f"{self.name} uses {move} on {opponent.get_name()} (damage {damage})!")
        opponent.take_hit(damage, inbound_attack=move, opponent_name=self.name)
    
    def take_hit(self, hit_value, inbound_attack="Attack", opponent_name="Opponent"):
        if self.life > hit_value:
            self.life -= hit_value
            print(f'{inbound_attack} of {hit_value} hurts {self.get_name()}!')
            return self.life
        else:
            self.life = 0
            print(f'{opponent_name} destroyed {self.name}. You lose!')
    
    def record_win(self):
        wins, losses = self.record
        self.record = (wins + 1, losses)
    
    def record_loss(self):
        wins, losses = self.record
        self.record = (wins, losses + 1)



    
class WaterCreature(Creature):
    def __init__(self, name, life=100):
        attacks = {'Flood': 5, 'Spew': 8, 'Dunk': 7}
        super().__init__(name, life, attacks, "Water")
        self.body = WATER_BODY


class EarthCreature(Creature):
    def __init__(self, name, life=130):
        attacks = {'Crumble': 3, 'Smash': 6, 'Dig': 5}
        super().__init__(name, life, attacks, "Earth")
        self.body = EARTH_BODY


class FireCreature(Creature):
    def __init__(self, name, life=80):
        attacks = {'Blaze': 8, 'Torch': 10, 'Simmer': 5}
        super().__init__(name, life, attacks, "Fire")
        self.body = FIRE_BODY


def render_character(character):
    print(character.body)
    print(f"Name: {character.name}")
    print(f"Type: {character.type}")
    print("Attacks:")
    for name, damage in character.attacks.items(): #abandoned the value to get just the keys...
        print(f"  - {name}")
    print('')
    print(f"Life: {character.life}")



#Ainew = WaterCreature('Aniew')
#render_character(Ainew)
