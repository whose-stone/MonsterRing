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
        print("\n--- Training Guessing Game ---")
        print("Guess a number between 1 and 3. You must win 2 out of 3 to train successfully!")
        wins = 0
        for round in range(3):
            guess = input(f"Round {round+1} - Enter your guess: ")
            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input, counted as a loss.")
                continue
            number = random.randint(1,3)
            if guess == number:
                print("Correct!")
                wins += 1
            else:
                print(f"Wrong! The number was {number}.")
        if wins >= 2:
            self.train_count += 1
            self.train_up += 1
            self.attacks = {name: dmg + 1 for name, dmg in self.attacks.items()}
            self.life += 20
            if self.life > 100:  # cap life
                self.life = 100
            print(f"{self.name} trained successfully! Level {self.train_up}, attacks powered up. Life restored to {self.life}.")
        else:
            print(f"{self.name} failed training. No improvements this time.")


    def attack(self, opponent, move=None):
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
        attacks = {'Flood': 15, 'Spew': 18, 'Dunk': 17}
        super().__init__(name, life, attacks, "Water")
        self.body = WATER_BODY
        self.secret_move = ("Tsunami", 25)

class EarthCreature(Creature):
    def __init__(self, name, life=130):
        attacks = {'Crumble': 13, 'Smash': 16, 'Dig': 15}
        super().__init__(name, life, attacks, "Earth")
        self.body = EARTH_BODY
        self.secret_move = ("Land Slide", 20)

class FireCreature(Creature):
    def __init__(self, name, life=80):
        attacks = {'Blaze': 18, 'Torch': 20, 'Simmer': 15}
        super().__init__(name, life, attacks, "Fire")
        self.body = FIRE_BODY
        self.secret_move = ("Explode", 28)

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
        print("\nYour attacks:")
        for i, (name, dmg) in enumerate(monster1.attacks.items(), start=1):  #this is the proper way to do it, not the hacky way 
            print(f"{i}. {name} (damage {dmg})")
        choice = input("Choose your attack (number): ")
        try:
            choice_index = int(choice) - 1
            move1 = list(monster1.attacks.keys())[choice_index]
        except (ValueError, IndexError):
            print("Invalid choice! Random attack used.")
            move1 = random.choice(list(monster1.attacks.keys()))

        monster1.attack(monster2, move1)
        print(f"Remaining Life -> {monster1.name}: {monster1.get_life()} | {monster2.name}: {monster2.get_life()}")

        if monster2.get_life() <= 0:
            print(f"\n{monster2.name} has been defeated!")
            monster1.record_win()
            monster2.record_loss()
            node.record_battle("Win")
            break

        # --- Opponent attacks randomly ---
        move2 = random.choice(list(monster2.attacks.keys()))
        monster2.attack(monster1, move2)
        print(f"Remaining Life -> {monster1.name}: {monster1.get_life()} | {monster2.name}: {monster2.get_life()}")

        if monster1.get_life() <= 0:
            print(f"\n{monster1.name} has been defeated!")
            monster2.record_win()
            monster1.record_loss()
            node.record_battle("Loss")
            break

    print("\nBattle over!")
    print(f"{monster1.name} record: {monster1.record}")
    print(f"{monster2.name} record: {monster2.record}")

def create_monster():
    name = input("Enter your monster's name: ")
    monster_type = input("Choose a type (Water, Earth, Fire): ").lower()

    if monster_type == "water":
        monster = WaterCreature(name)
    elif monster_type == "earth":
        monster = EarthCreature(name)
    elif monster_type == "fire":
        monster = FireCreature(name)
    else:
        print("Invalid type! Defaulting to Water.")
        monster = WaterCreature(name)

    return monster

def guessing_game(monster):
    print("\n--- Number Guessing Game ---")
    print("Guess a number between 1 and 3. You must win 2 out of 3 to regain life!")
    wins = 0
    for round in range(3):
        guess = input(f"Round {round+1} - Enter your guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input, counted as a loss.")
            continue
        number = random.randint(1,3)
        if guess == number:
            print("Correct!")
            wins += 1
        else:
            print(f"Wrong! The number was {number}.")
    if wins >= 2:
        monster.life = 50  # restore some life
        print(f"{monster.name} regains life! Current life: {monster.life}")
    else:
        print("You failed the guessing game. Train harder next time!")

def main():
    user_monster = create_monster()
    print(f"\nMonster created!\nName: {user_monster.name}\nType: {user_monster.type}\nLife: {user_monster.life}")
    print(user_monster.body)

    battle_tree = build_battle_tree(user_monster.type, user_monster.name)

    # Loop until both opponents are defeated
    while not (battle_tree.left.fought and battle_tree.right.fought):
        action = input("\nDo you want to FIGHT or TRAIN? ").lower()
        if action == "train":
            user_monster.train()
            continue
        elif action == "fight":
            print(f"Left Opponent: {battle_tree.left.monster.name} ({battle_tree.left.monster.type})")
            print(f"Right Opponent: {battle_tree.right.monster.name} ({battle_tree.right.monster.type})")
            side = input("Choose LEFT or RIGHT opponent: ").lower()
            if side == "left" and not battle_tree.left.fought:
                battle(user_monster, battle_tree.left.monster, battle_tree.left)
                if battle_tree.left.result == "Win":
                    move, dmg = user_monster.secret_move
                    user_monster.attacks[move] = dmg
                    print(f"{user_monster.name} unlocked secret move: {move}!")
                else:
                    guessing_game(user_monster)
            elif side == "right" and not battle_tree.right.fought:
                battle(user_monster, battle_tree.right.monster, battle_tree.right)
                if battle_tree.right.result == "Win":
                    move, dmg = user_monster.secret_move
                    user_monster.attacks[move] = dmg
                    print(f"{user_monster.name} unlocked secret move: {move}!")
                else:
                    guessing_game(user_monster)
            else:
                print("That opponent is already defeated or invalid choice.")
        else:
            print("Invalid action. Type FIGHT or TRAIN.")

    print("\n--- All Opponents Defeated! ---")
    print(f"{user_monster.name} record: {user_monster.record}")



if __name__ == "__main__":
    input("Welcome to MONSTER MASH! Where you will create and fight your own monster! Use CTRL + C to quit at any time. Press Enter to continue...")

    print("You can choose from three kinds of monsters. Water, Earth, and Fire \n"
          f"Water {WATER_BODY}\n"
          f"Earth {EARTH_BODY}\n"
          f"Fire {FIRE_BODY}\n"
          )
    
    main()
