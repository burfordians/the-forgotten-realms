import time # time.sleep(x) USED FOR DELAYS
import random #random.randint(x, y) USED FOR COMBAT


hitChance = 0.4 #Roll higher than 0.4 out of 0-1 to hit

charInventory = [] #Array for Inventory
charRaces = ["Human", "Elf", "Dwarf", "Orc"] #Array of races

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("|The Legend of The Forgotten Realms|")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

time.sleep(2)

print("Welcome to The Forgotten Realms, times are dangerous nowadays so watch your step.") #Introduction
nameRepeat = 0
while nameRepeat == 0:
    print("") # For space between lines
    charName = str(input("Now, what is your name? [Maximum of 14 Characters]")) #Name Selection
    time.sleep(2)

    if len(charName) <= 14: #Name length check
        print("")
        print("Hello," ,charName, "Welcome to The Forgotten Realms")
        time.sleep(2)
        break

    else:
        print("")
        print("Your name has more than 14 characters, please try again.")
        time.sleep(1)
        continue


raceRepeat = 0
while raceRepeat == 0:
    print("")
    charRace = str(input("What race are you? Human/Elf/Dwarf/Orc")) #Race selection
    #charRace = charRace.upper() --- If I want 0 chance of case issues

    if charRace in ["Human", "Elf", "Dwarf", "Orc"]: #Array of races
        print("")
        print("Good choice," ,charRace, "it is then.")
        time.sleep(2)
        break

    else:
        print("")
        print("Thats not a valid race, please try again.")
        time.sleep(1)
        continue

weaponRepeat = 0
while weaponRepeat == 0:
    print("")
    charWeapon = str(input("What weapon do you wield? Sword/Axe/Spear/Bow/Crossbow")) #Weapon selection
    #charWeapon = charWeapon.upper() --- If I want 0 chance of case issues

    if charWeapon in ["Sword", "Axe", "Spear", "Bow", "Crossbow"]: #Array of weapons
        print("")
        print("A",charWeapon,"is a fine choice of weapon.")
        charInventory.append(charWeapon)
        time.sleep(2)
        break

    else:
        print("")
        print("That is not a weapon choice currently, please try again")
        time.sleep(1)
        continue
    
print("")
print("You are a" ,charRace, "wielding a" ,charWeapon)
time.sleep(2)

print("")
print("Now lets test your combat prowess!")
time.sleep(2)

def printCombatHP(charHP, enemyName, enemyHP): #A function defined for the Hitpoint system.
    print("")
    print("Your HP:", charHP,"    ", enemyName, "HP:", enemyHP)

if charRace == "Human": #List of 'IF' statements deciding on opponent based on race selected.
    enemyWarrior = str("Orc Raider")
    print("")
    print("Since you are a", charRace, "you shall face a" ,enemyWarrior, "good luck!")
    time.sleep(2)
elif charRace == "Elf":
    enemyWarrior = str("Dwarven Fighter")
    print("")
    print("Since you are a", charRace, "you shall face a" ,enemyWarrior, "good luck!")
    time.sleep(2)
elif charRace == "Dwarf":
    enemyWarrior = str("Elven Warrior")
    print("")
    print("Since you are a", charRace, "you shall face a" ,enemyWarrior, "good luck!")
    time.sleep(2)
elif charRace == "Orc":
    enemyWarrior = str("Human Soldier")
    print("")
    print("Since you are a", charRace, "you shall face a" ,enemyWarrior, "good luck!")
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
            print("")
            print("You sucessfully hit!")
            time.sleep(3)
            print("")
            print("You slash at the", enemyWarrior, "severing a few arteries and inflicting", charDmg, "damage!")
            time.sleep(3)
            charDmg >= enemyWarriorHP
            charDmg = enemyWarriorHP
            if enemyWarriorHP <= 0:
                print("The", enemyWarrior, "falls before you.")
                break
            
            enemyHitChance = random.uniform(0.1, 1.0)
            if enemyHitChance >= hitChance:
                enemyWarriorDmg = random.randint(1,4)
                charHP -= enemyWarriorDmg
                print("")
                print("The", enemyWarrior, "hits!")
                print("")
                print("The", enemyWarrior, "strikes you dealing", enemyWarriorDmg, "damage!")
                time.sleep(3)
                
            else:
                print("")
                print("Luckily he misses you!")
                time.sleep(3)
                    
        else:
            print("")
            print("Unfortunately you missed!")
            time.sleep(3)

            enemyHitChance = random.uniform(0.1, 1.0)
            if enemyHitChance >= hitChance:
                enemyWarriorDmg = random.randint(1,4)
                charHP -= enemyWarriorDmg
                print("")
                print("The", enemyWarrior, "hits!")
                print("")
                print("The", enemyWarrior, "strikes you dealing", enemyWarriorDmg, "damage!")
                time.sleep(3)
            continue
            
    elif charInventory[0] == "Axe":
            charHitChance = random.uniform(0.0, 1.0)
            if charHitChance >= hitChance:
                charDmg = random.randint(1,8)
                enemyWarriorHP -= charDmg
                print("")
                print("You sucessfully hit!")
                time.sleep(3)
                print("")
                print("You cleave at the", enemyWarrior, "severing a few arteries and inflicting", charDmg, "damage!")
                time.sleep(3)
            charDmg >= enemyWarriorHP
            charDmg = enemyWarriorHP
            if enemyWarriorHP <= 0:
                printCombatHP(charHP, enemyWarrior, enemyWarriorHP)
                print("The", enemyWarrior, "falls before you.")
                break
            
            enemyHitChance = random.uniform(0.1, 1.0)
            if enemyHitChance >= hitChance:
                enemyWarriorDmg = random.randint(1,4)
                charHP -= enemyWarriorDmg
                print("")
                print("The", enemyWarrior, "hits!")
                print("")
                print("The", enemyWarrior, "strikes you dealing", enemyWarriorDmg, "damage!")
                time.sleep(3)
                
            else:
                print("")
                print("Luckily he misses you!")
                time.sleep(3)
                
    else:
        print("")
        print("Unfortunately you missed!")
        time.sleep(3)

        enemyHitChance = random.uniform(0.1, 1.0)
        if enemyHitChance >= hitChance:
                enemyWarriorDmg = random.randint(1,4)
                charHP -= enemyWarriorDmg
                print("")
                print("The", enemyWarrior, "hits!")
                print("")
                print("The", enemyWarrior, "strikes you dealing", enemyWarriorDmg, "damage!")
                time.sleep(3)
        continue
            
        if charInventory[0] == "Spear":
            charHitChance = random.uniform(0.4, 1.0)
            if charHitChance >= hitChance:
                charDmg = random.randint(1,3)
                enemyWarriorHP -= charDmg
                print("")
                print("You sucessfully hit!")
                time.sleep(3)
                print("")
                print("You drive your spear right into the", enemyWarrior, "dealing", charDmg, "damage!")
                time.sleep(3)
            charDmg >= enemyWarriorHP
            charDmg = enemyWarriorHP
            if enemyWarriorHP <= 0:
                print("The", enemyWarrior, "falls before you.")
                break
                
            else:
                print("")
                print("Unfortunately you missed somehow with the 100% accurate weapon wtf") #Confirm if the weapon doesn't function as intended.
                time.sleep(3)

                enemyHitChance = random.uniform(0.1, 1.0)
            if enemyHitChance >= hitChance:
                enemyWarriorDmg = random.randint(1,4)
                charHP -= enemyWarriorDmg
                print("")
                print("The", enemyWarrior, "hits!")
                print("")
                print("The", enemyWarrior, "strikes you dealing", enemyWarriorDmg, "damage!")
                time.sleep(3)
                continue
            
        if charInventory[0] == "Bow":
            charHitChance = random.uniform(0.3, 1.0)
            if charHitChance >= hitChance:
                charDmg = random.randint(1,4)
                enemyWarriorHP -= charDmg
                print("")
                print("You sucessfully hit!")
                print("")
                print("You take a step back and fire an arrow that hits in a gap between the armour of the", enemyWarrior, "and inflicting" ,charDmg, "damage!")
            else:
                print("")
                print("Unfortunately you missed!")
                time.sleep(3)
                
                enemyHitChance = random.uniform(0.1, 1.0)
            if enemyHitChance >= hitChance:
                enemyWarriorDmg = random.randint(1,4)
                charHP -= enemyWarriorDmg
                print("")
                print("The", enemyWarrior, "hits!")
                print("")
                print("The", enemyWarrior, "strikes you dealing", enemyWarriorDmg, "damage!")
                time.sleep(3)
                continue
            
        if charInventory[0] == "Crossbow":
            charHitChance = random.uniform(0.1, 1.0)
            if charHitChance >= hitChance:
                charDmg = random.randint(1,5)
                enemyWarriorHP -= charDmg
                print("")
                print("You sucessfully hit!")
                print("")
                print("You ready your", charWeapon, "and fire a bolt at the", enemyWarrior,"! piercing his armour and dealing", charDmg, "damage!")
                charDmg >= enemyWarriorHP
                charDmg = enemyWarriorHP
                if enemyWarriorHP <= 0:
                    print("The", enemyWarrior, "falls before you.")
                    break
                
        else:
            print("")
            print("Unfortunately you missed!")
            time.sleep(3)
            
            enemyHitChance = random.uniform(0.1, 1.0)
            if enemyHitChance >= hitChance:
                enemyWarriorDmg = random.randint(1,4)
                charHP -= enemyWarriorDmg
                print("")
                print("The", enemyWarrior, "hits!")
                print("")
                print("The", enemyWarrior, "strikes you dealing", enemyWarriorDmg, "damage!")
                time.sleep(3)
            continue
#COMBAT LOOP ENDS


