import random 
import time

#global variables for the designs of the monsters. Not really well designed but it'll work for now.
WATER_BODY = ('\033[34m           \n   ^  ^   \n    @     \n  /   \\ \n    JL    \n\033[0m')
EARTH_BODY = ('\033[32m          \n   *  *   \n   -$-    \n  <~~>    \n   000    \n\033[0m')
FIRE_BODY = ('\033[31m          \n   )  (   \n   00    \n  ###     \n  {] [}    \n\033[0m')



#create the creatures that will fight, enable abilities such as training, and track success for added moves after wins
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
        import random
        if move is None:
            move = random.choice(list(self.attacks.keys()))
        if move not in self.attacks:
            print(f"{self.name} doesn't know {move}!")
            return
    
        damage = self.attacks[move]

        print("\n--- ATTACK TURN ---")
        print(f"{self.name} (Attacker):")
        print(self.body)
        time.sleep(1)
        print(f"{opponent.name} (Defender):")
        print(opponent.body)
        time.sleep(1)
        
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

#here are the three types of creatures with their default values  
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

#so we can see our monster
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

#creates the tree datatype to track the user's battles
class BattleNode:
    def __init__(self, monster):
        self.monster = monster
        self.fought = False
        self.result = None 
        self.left = None
        self.right = None

    def record_battle(self, result):
        self.fought = True
        self.result = result

#builds the tree based on the user's selection of monster
def build_battle_tree(user_choice, name):
    if user_choice.lower() == "water":
        root = BattleNode(WaterCreature(name))
        root.left = BattleNode(EarthCreature("EarthOpponent"))
        root.right = BattleNode(FireCreature("FireOpponent"))
    elif user_choice.lower() == "earth":
        root = BattleNode(EarthCreature(name))
        root.left = BattleNode(WaterCreature("WaterOpponent"))
        root.right = BattleNode(FireCreature("FireOpponent"))
    else:
        root = BattleNode(FireCreature(name))
        root.left = BattleNode(WaterCreature("WaterOpponent"))
        root.right = BattleNode(EarthCreature("EarthOpponent"))
    return root

#this is the battle engine, it allows for two monsters to fight until one dies
def battle(monster1, monster2, node):
    """Run a battle between two monsters and update the node result."""
    print(f"\nBattle begins: {monster1.name} vs {monster2.name}!\n")

    while monster1.get_life() > 0 and monster2.get_life() > 0:
        # Monster1 attacks
        move1 = random.choice(list(monster1.attacks.keys()))
        monster1.attack(monster2, move1)

        if monster2.get_life() <= 0:
            print(f"\n{monster2.name} has been defeated!")
            monster1.record_win()
            monster2.record_loss()
            node.record_battle("Win")
            break

        # Monster2 attacks
        move2 = random.choice(list(monster2.attacks.keys()))
        monster2.attack(monster1, move2)

        if monster1.get_life() <= 0:
            print(f"\n{monster1.name} has been defeated!")
            monster2.record_win()
            monster1.record_loss()
            node.record_battle("Loss")
            break

    print("\nBattle over!")
    print(f"{monster1.name} record: {monster1.record}")
    print(f"{monster2.name} record: {monster2.record}")

if __name__ == "__main__":
    main()