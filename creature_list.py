# create a monster. All monsters have a name, type, life, and body.

class creature:
    def __init__(self, name, life):
        self.creature_name = name
        self.creature_life = life

    def set_name(self, name):
        self.creature_name = name
    
    def set_life(self, life):
        self.creature_life = life

    def set_attack(self, attack):
        self.creature_attack = attack

    def get_name(self):
        return self.creature_name
    
    def get_life(self):
        return self.creature_life
    
    def take_hit(self, hit_value):
        if self.life > hit_value:
            self.life = self.life - hit_value
            print(f'{inbound_attack} of {hit_value} hurts {self.get_name}!')
            return self.life
        else:
            self.life = 0
            print(f'{opponent_name} destroyed {self.creature_name}. You lose!')

    
class WaterCreature(creature):

    def __init__(self, name, life, creature_type):
        super().__init__( name, life)
        self.life = 100
        self.creature_type = creature_type
        self.attacks = {'Wash': 5, 'Spew': 8, 'Dunk':7}
        self.body = '\033[34m           \n   ^  ^   \n    @     \n  /   \\ \n    JL    \n\033[0m'

class EarthCreature(creature):

    def __init__(self, name, life, creature_type):
        super().__init__( name, life)
        self.life = 130
        self.creature_type = creature_type
        self.attacks = {'Crumble': 3, 'Smash': 6, 'Dig':5}
        self.body = '\033[32m          \n   *  *   \n   -$-    \n  <~~>    \n   000    \n\033[0m'

class FireCreature(creature):

    def __init__(self, name, life, creature_type):
        super().__init__( name, life)
        self.life = 80
        self.creature_type = creature_type
        self.attacks = {'Blaze': 8, 'Torch': 10, 'Simmer':5}
        self.body = '\033[31m          \n   )  (   \n   00    \n  ###     \n  {] [}    \n\033[0m'

def render_character(character):
    print(character)
    print(f"Your stats:\n     Life:{life}\n     Attacks:{attack_list}\n\n")

#def select_attack(character):
#    
#    for i in attack_list:
#        if attack_list_count[i] > 0:
#            print(f"{attack_list}")
#


    
#    selection = input("Select your attack!")
#    if selection in range(len(attack_list + 1)):
#        if attack_list[selection] > 0:
#            attack_list_count[selection] = selection -1
#            print(f'{character} used {attack_list[selection]}!')

        


render_character(water_creature)
select_attack