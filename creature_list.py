# create a monster. All monsters have a name, type, life, and body.

WATER_BODY = ('\033[34m           \n   ^  ^   \n    @     \n  /   \\ \n    JL    \n\033[0m')
EARTH_BODY = ('\033[32m          \n   *  *   \n   -$-    \n  <~~>    \n   000    \n\033[0m')
FIRE_BODY = ('\033[31m          \n   )  (   \n   00    \n  ###     \n  {] [}    \n\033[0m')




class Creature:
    def __init__(self, name, life, attacks, creature_type):
        self.name = name
        self.life = life
        self.attacks = attacks
        self.type = creature_type

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
    
    def take_hit(self, hit_value, inbound_attack="Attack", opponent_name="Opponent"):
        if self.life > hit_value:
            self.life -= hit_value
            print(f'{inbound_attack} of {hit_value} hurts {self.get_name()}!')
            return self.life
        else:
            self.life = 0
            print(f'{opponent_name} destroyed {self.name}. You lose!')


    
class WaterCreature(Creature):
    def __init__(self, name, life=100):
        attacks = {'Wash': 5, 'Spew': 8, 'Dunk': 7}
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
    for name, damage in character.attacks.items():
        print(f"  - {name}")
    print('')
    print(f"Life: {character.life}")



Ainew = WaterCreature('Aniew')
render_character(Ainew)
