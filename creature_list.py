# create a monster. All monsters have a name, type, life, and body.

water_body = '\033[34m           \n   ^  ^   \n    @     \n  /   \\ \n    JL    \n\033[0m'
earth_body = '\033[32m          \n   *  *   \n   -$-    \n  <~~>    \n   000    \n\033[0m'
fire_body = '\033[31m          \n   )  (   \n   00    \n  ###     \n  {] [}    \n\033[0m'




class Creature:
    def __init__(self, name, life, attacks, type):
        self.creature_name = name
        self.creature_life = life
        self.creature_attacks = attacks
        self.creature_type = type

    def set_name(self, name):
        self.creature_name = name
    
    def set_life(self, life):
        self.creature_life = life

    def set_attack(self, attacks):
        self.creature_attacks = attacks

    def get_name(self):
        return self.creature_name
    
    def get_life(self):
        return self.creature_life
    
    def get_attacks(self):
        return self.creature_attacks
    
    def take_hit(self, hit_value):
        if self.life > hit_value:
            self.life = self.life - hit_value
            print(f'{inbound_attack} of {hit_value} hurts {self.get_name}!')
            return self.life
        else:
            self.life = 0
            print(f'{opponent_name} destroyed {self.creature_name}. You lose!')

    
class WaterCreature(Creature):

    def __init__(self, name, life = 100, attacks = {'Wash': 5, 'Spew': 8, 'Dunk':7}, type = "Water"):
        super().__init__(name, life, attacks, type)
        self.name = name
        self.type = type
        self.life = life
        self.attacks = attacks
        self.body = '\033[34m           \n   ^  ^   \n    @     \n  /   \\ \n    JL    \n\033[0m'

class EarthCreature(Creature):

    def __init__(self, name, life, creature_type):
        super().__init__( name, life)
        self.life = 130
        self.creature_type = creature_type
        self.attacks = {'Crumble': 3, 'Smash': 6, 'Dig':5}
        self.body = '\033[32m          \n   *  *   \n   -$-    \n  <~~>    \n   000    \n\033[0m'

class FireCreature(Creature):

    def __init__(self, name, life, creature_type):
        super().__init__( name, life)
        self.life = 80
        self.creature_type = creature_type
        self.attacks = {'Blaze': 8, 'Torch': 10, 'Simmer':5}
        self.body = '\033[31m          \n   )  (   \n   00    \n  ###     \n  {] [}    \n\033[0m'

def render_character(character):
    print(character.body)
    print(f"Name: {character.name}")
    print(f"Type: {character.type}")
    print("Attacks:")
    for name, damage in character.attacks.items():
        print(f"  - {name}")
    print('')
    print(f"Life: {character.life}")



#Ainew = WaterCreature('Aniew')
#
#render_character(Ainew)

print(WaterCreature.body)