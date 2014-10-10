import time # time.sleep(x) USED FOR DELAYS
import random #random.randint(x, y) USED FOR COMBAT


hitChance = 0.4 #Roll higher than 0.4 out of 0-1 to hit

charInventory = [] #Array for Inventory
charRaces = ["Human", "Elf", "Dwarf", "Orc"] #Array of races

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("|The Legend of The Forgotten Realms|")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

time.sleep(2)

print("Welcome to The Forgotten Realms, times are dangerous nowadays so watch your step.\n") #Introduction
nameRepeat = 0
while nameRepeat == 0:
    charName = str(input("Now, what is your name? [Maximum of 14 Characters]\n")) #Name Selection
    time.sleep(2)

    if len(charName) <= 14: #Name length check
        print("Hello," ,charName, "Welcome to The Forgotten Realms\n")
        time.sleep(2)
        break

    else:
        print("Your name has more than 14 characters, please try again.\n")
        time.sleep(1)
        continue


raceRepeat = 0
while raceRepeat == 0:
    charRace = str(input("What race are you? Human/Elf/Dwarf/Orc\n")) #Race selection
    #charRace = charRace.upper() --- If I want 0 chance of case issues

    if charRace in ["Human", "Elf", "Dwarf", "Orc"]: #Array of races
        print("Good choice," ,charRace, "it is then.\n")
        time.sleep(2)
        break

    else:
        print("Thats not a valid race, please try again.\n")
        time.sleep(1)
        continue

weaponRepeat = 0
while weaponRepeat == 0:
    charWeapon = str(input("What weapon do you wield? Sword/Axe/Spear/Bow/Crossbow\n")) #Weapon selection
    #charWeapon = charWeapon.upper() --- If I want 0 chance of case issues

    if charWeapon in ["Sword", "Axe", "Spear", "Bow", "Crossbow"]: #Array of weapons
        print("A",charWeapon,"is a fine choice of weapon.\n")
        charInventory.append(charWeapon)
        time.sleep(2)
        break

    else:
        print("That is not a weapon choice currently, please try again\n")
        time.sleep(1)
        continue
    
print("You are a" ,charRace, "wielding a" ,charWeapon ,"\n")
time.sleep(2)

print("Now lets test your combat prowess!\n")
time.sleep(2)

def printCombatHP(charHP, enemyName, enemyHP): #A function defined for the Hitpoint system.
    print("Your HP:", charHP,"    ", enemyName, "HP:", enemyHP, "\n")

if charRace == "Human": #List of 'IF' statements deciding on opponent based on race selected.
    enemyWarrior = str("Orc Raider")
    print("Since you are a", charRace, "you shall face a" ,enemyWarrior, "good luck!\n")
    time.sleep(2)
elif charRace == "Elf":
    enemyWarrior = str("Dwarven Fighter")
    print("Since you are a", charRace, "you shall face a" ,enemyWarrior, "good luck!\n")
    time.sleep(2)
elif charRace == "Dwarf":
    enemyWarrior = str("Elven Warrior")
    print("Since you are a", charRace, "you shall face a" ,enemyWarrior, "good luck!\n")
    time.sleep(2)
elif charRace == "Orc":
    enemyWarrior = str("Human Soldier")
    print("Since you are a", charRace, "you shall face a" ,enemyWarrior, "good luck!\n")
    time.sleep(2)

charHP = 15
enemyWarriorHP = 12


#COMBAT LOOP BEGINS
while charHP > 0:
    printCombatHP(charHP, enemyWarrior, enemyWarriorHP)#Using function created earlier for combat HP

    if charInventory[0] == "Sword":
        charHitChance = random.uniform(0.2, 1.0)
        if charHitChance >= hitChance:
            charDmg = random.randint(1,4)
            enemyWarriorHP -= charDmg
            print("You sucessfully hit!\n")
            time.sleep(3)
            print("You slash at the", enemyWarrior, "severing a few arteries and inflicting", charDmg, "damage!\n")
            time.sleep(3)
            charDmg >= enemyWarriorHP
            charDmg = enemyWarriorHP
            if enemyWarriorHP <= 0:
                print("The", enemyWarrior, "falls before you.\n")
                break
            
            enemyHitChance = random.uniform(0.1, 1.0)
            if enemyHitChance >= hitChance:
                enemyWarriorDmg = random.randint(1,4)
                charHP -= enemyWarriorDmg
                print("The", enemyWarrior, "hits!\n")
                print("The", enemyWarrior, "strikes you dealing", enemyWarriorDmg, "damage!\n")
                time.sleep(3)
                
            else:
                print("Luckily he misses you!\n")
                time.sleep(3)
                    
        else:
            print("Unfortunately you missed!\n")
            time.sleep(3)

            enemyHitChance = random.uniform(0.1, 1.0)
            if enemyHitChance >= hitChance:
                enemyWarriorDmg = random.randint(1,4)
                charHP -= enemyWarriorDmg
                print("The", enemyWarrior, "hits!\n")
                print("The", enemyWarrior, "strikes you dealing", enemyWarriorDmg, "damage!\n")
                time.sleep(3)
                continue
            
    elif charInventory[0] == "Axe":
            charHitChance = random.uniform(0.0, 1.0)
            if charHitChance >= hitChance:
                charDmg = random.randint(1,8)
                enemyWarriorHP -= charDmg
                print("You sucessfully hit!\n")
                time.sleep(3)
                print("You cleave at the", enemyWarrior, "severing a few arteries and inflicting", charDmg, "damage!\n")
                time.sleep(3)
            charDmg >= enemyWarriorHP
            charDmg = enemyWarriorHP
            if enemyWarriorHP <= 0:
                printCombatHP(charHP, enemyWarrior, enemyWarriorHP)
                print("The", enemyWarrior, "falls before you.\n")
                break
            
            enemyHitChance = random.uniform(0.1, 1.0)
            if enemyHitChance >= hitChance:
                enemyWarriorDmg = random.randint(1,4)
                charHP -= enemyWarriorDmg
                print("The", enemyWarrior, "hits!\n")
                print("The", enemyWarrior, "strikes you dealing", enemyWarriorDmg, "damage!\n")
                time.sleep(3)
                
            else:
                print("Luckily he misses you!\n")
                time.sleep(3)
                
    else:
        print("Unfortunately you missed!\n")
        time.sleep(3)

        enemyHitChance = random.uniform(0.1, 1.0)
        if enemyHitChance >= hitChance:
            enemyWarriorDmg = random.randint(1,4)
            charHP -= enemyWarriorDmg
            print("The", enemyWarrior, "hits!\n")
            print("The", enemyWarrior, "strikes you dealing", enemyWarriorDmg, "damage!\n")
            time.sleep(3)
            continue
            
        if charInventory[0] == "Spear":
            charHitChance = random.uniform(0.4, 1.0)
            if charHitChance >= hitChance:
                charDmg = random.randint(1,3)
                enemyWarriorHP -= charDmg
                print("You sucessfully hit!\n")
                time.sleep(3)
                print("You drive your spear right into the", enemyWarrior, "dealing", charDmg, "damage!\n")
                time.sleep(3)
            charDmg >= enemyWarriorHP
            charDmg = enemyWarriorHP
            if enemyWarriorHP <= 0:
                print("The", enemyWarrior, "falls before you.\n")
                break
                
            else:
                print("Unfortunately you missed somehow with the 100% accurate weapon wtf\n") #Confirm if the weapon doesn't function as intended.
                time.sleep(3)

                enemyHitChance = random.uniform(0.1, 1.0)
            if enemyHitChance >= hitChance:
                enemyWarriorDmg = random.randint(1,4)
                charHP -= enemyWarriorDmg
                print("The", enemyWarrior, "hits!\n")
                print("The", enemyWarrior, "strikes you dealing", enemyWarriorDmg, "damage!\n")
                time.sleep(3)
                continue
            
        if charInventory[0] == "Bow":
            charHitChance = random.uniform(0.3, 1.0)
            if charHitChance >= hitChance:
                charDmg = random.randint(1,4)
                enemyWarriorHP -= charDmg
                print("You sucessfully hit!\n")
                print("You take a step back and fire an arrow that hits in a gap between the armour of the", enemyWarrior, "and inflicting" ,charDmg, "damage!\n")
            else:
                print("Unfortunately you missed!\n")
                time.sleep(3)
                
                enemyHitChance = random.uniform(0.1, 1.0)
            if enemyHitChance >= hitChance:
                enemyWarriorDmg = random.randint(1,4)
                charHP -= enemyWarriorDmg
                print("The", enemyWarrior, "hits!\n")
                print("The", enemyWarrior, "strikes you dealing", enemyWarriorDmg, "damage!\n")
                time.sleep(3)
                continue
            
        if charInventory[0] == "Crossbow":
            charHitChance = random.uniform(0.1, 1.0)
            if charHitChance >= hitChance:
                charDmg = random.randint(1,5)
                enemyWarriorHP -= charDmg
                print("You sucessfully hit!\n")
                print("You ready your", charWeapon, "and fire a bolt at the", enemyWarrior,"! piercing his armour and dealing", charDmg, "damage!\n")
                charDmg >= enemyWarriorHP
                charDmg = enemyWarriorHP
                if enemyWarriorHP <= 0:
                    print("The", enemyWarrior, "falls before you.\n")
                    break
                
        else:
            print("Unfortunately you missed!\n")
            time.sleep(3)
            
            enemyHitChance = random.uniform(0.1, 1.0)
            if enemyHitChance >= hitChance:
                enemyWarriorDmg = random.randint(1,4)
                charHP -= enemyWarriorDmg
                print("The", enemyWarrior, "hits!\n")
                print("The", enemyWarrior, "strikes you dealing", enemyWarriorDmg, "damage!\n")
                time.sleep(3)
                continue
#COMBAT LOOP END