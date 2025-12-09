# create a monster. All monsters have a name, type, and body.



Ainew ='\033[34m           \n   ^  ^   \n    @     \n  /     \ \n    JL    \n\033[0m'

Mylo = '\033[32m          \n   *  *   \n   -$-    \n  <~~>    \n   000    \n\033[0m'

Garro = '\033[31m          \n   )  (   \n   00    \n  ###     \n  {] [}    \n\033[0m'

#print(Ainew)
#print(Mylo)
#print(Garro)

life = 80

attack_list = ['Strike', 'Block', 'Spew']
attack_list_count = [3,0,1]

def render_character(character):
    print(character)
    print(f"Your stats:\n     Life:{life}\n     Attacks:{attack_list}\n\n")

def select_attack(character):
    
    for i in attack_list:
        if attack_list_count[i] > 0:


    print(f{attack_list})
    selection = input("Select your attack!")
    if selection in range(len(attack_list + 1)):
        if attack_list[selection] > 0:
            attack_list_count[selection] = selection -1
            print(f'{character} used {attack_list[selection]}!')

        


render_character(Ainew)
select_attack