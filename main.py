from creature_list import *



input("Welcome to MONSTER MASH! Where you will create and fight your own monster! Press Enter to continue...")

print("You can choose from three kinds of monsters. Water, Earth, and Fire \n"
      f"Water {WATER_BODY}\n"
      f"Earth {EARTH_BODY}\n"
      f"Fire {FIRE_BODY}\n"
      )

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

user_monster = create_monster()
print(f"\nMonster created!\nName: {user_monster.name}\nType: {user_monster.type}\nLife: {user_monster.life}")
print(user_monster.body)







