import time  # time.sleep(x) USED FOR DELAYS
import random  # random.randint(x, y) USED FOR COMBAT

# BUGS:
# 1)

# TO DO LIST:
# 1)Dodge System (Gonna be hell since this wasn't done with functions Q_Q)
# 2)Second Fight, Targetting system so there is actual player interaction during combat. (Use functions this time :x)
# 3)Different Stages of Combat (Rather than continuous while loop, possible for loop???)
# 4)Finish Crossbow
# 5)Armour/Resistance System (Reduction in overall damage based on armour)

replay = "YES"  # Replay System
hitChance = 0.4  # Roll higher than 0.4 out of 0-1 to hit
dodgeChance = 0.7  # DODGE MECHANIC?! - Not implemented, yet.

charInventory = []  # Array for Inventory
charRaces = ["Human", "Elf", "Dwarf", "Orc"]  # Array of races

def title():
    border = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    title = "The Legend of The Forgotten Realms\n"
    return border + title + border

while replay == "YES":
    replay = "NO"
    print(title())
    time.sleep(2)

    # Introduction
    print(
        "Welcome to The Forgotten Realms, times are dangerous nowadays so watch your step.\n")
    nameRepeat = 0
    while nameRepeat == 0:
        # Name Selection
        charName = str(
            input("Now, what is your name? [Maximum of 14 Characters]\n"))
        time.sleep(2)

        if len(charName) <= 14:  # Name length check
            print("Hello,", charName, "Welcome to The Forgotten Realms\n")
            time.sleep(2)
            break

        else:
            print(
                "Sorry but '",
                charName,
                "' has more than 14 characters, please try again.\n")  # repeat loop if invalid entry
            time.sleep(1)
            continue

    else:
        print("")

    raceRepeat = 0
    while raceRepeat == 0:
        charRace = str(
            input("What race are you? Human/Elf/Dwarf/Orc\n"))  # Race selection
        charRace = charRace.upper()
        if charRace == "HUMAN":
            charRace = "Human"
        if charRace == "ELF":
            charRace = "Elf"
        if charRace == "DWARF":
            charRace = "Dwarf"
        if charRace == "ORC":
            charRace = "Orc"

        if charRace in ["Human", "Elf", "Dwarf", "Orc"]:  # Array of races
            print("Good choice,", charRace, "it is then.\n")
            time.sleep(2)
            break

        else:
            print(
                "Sorry but '",
                charRace,
                "' is not a valid race, please try again.\n Tip: Your answer is case sensitive!\n")
            time.sleep(1)
            continue

    weaponRepeat = 0
    while weaponRepeat == 0:
        # Weapon selection
        charWeapon = str(input(
            "What weapon do you wield? Sword/Axe/Spear/Crossbow \n Weapon Rundown: \n Sword:- A fast versatile weapon. 80% accuracy, Maximum of 4 Damage \n Axe:- A devastatingly powerful and heavy weapon. 60% accuracy, Maximum of 8 Damage \n Spear:- When used in close range is an almost guaranteed hit, but ineffective. 100% accuracy, Maximum of 3 Damage \n Crossbow:- Powerful and accurate weapon, ignores heavy armour resistance. 80% Accuracy, Maximum of 4 Damage"))
        charWeapon = charWeapon.upper()
        if charWeapon == "SWORD":
            charWeapon = "Sword"
        if charWeapon == "AXE":
            charWeapon = "Axe"
        if charWeapon == "SPEAR":
            charWeapon = "Spear"
        if charWeapon == "CROSSBOW":
            charWeapon = "Crossbow"

        if charWeapon in [
                "Sword",
                "Axe",
                "Spear",
                "Crossbow"]:  # Array of weapons
            print("A", charWeapon, "is a fine choice of weapon.\n")
            charInventory.append(charWeapon)
            time.sleep(2)
            break

        else:
            print(
                "Sorry but",
                charWeapon,
                "is not a weapon choice currently, please try again \n Tip: Your answer is case sensitive!\n")
            time.sleep(1)
            continue

    print("You are a", charRace, "wielding a", charWeapon, "\n")
    time.sleep(2)

    print("Now lets test your combat prowess!\n")
    time.sleep(2)

    # A function defined for the Hitpoint system.
    def printCombatHP(charHP, enemyName, enemyHP):
        print("Your HP:", charHP, "    ", enemyName, "HP:", enemyHP, "\n")

    # List of 'IF' statements deciding on opponent based on race selected.
    if charRace == "Human":
        enemyWarrior = str("Orc Raider")
        print(
            charName,
            "since you are a",
            charRace,
            "you shall face a",
            enemyWarrior,
            "good luck!\n")
        time.sleep(2)
    elif charRace == "Elf":
        enemyWarrior = str("Dwarven Fighter")
        print(
            charName,
            "since you are a",
            charRace,
            "you shall face a",
            enemyWarrior,
            "good luck!\n")
        time.sleep(2)
    elif charRace == "Dwarf":
        enemyWarrior = str("Elven Warrior")
        print(
            charName,
            "since you are a",
            charRace,
            "you shall face a",
            enemyWarrior,
            "good luck!\n")
        time.sleep(2)
    elif charRace == "Orc":
        enemyWarrior = str("Human Soldier")
        print(
            charName,
            "since you are a",
            charRace,
            "you shall face a",
            enemyWarrior,
            "good luck!\n")
        time.sleep(2)

    charHP = 15
    enemyWarriorHP = 12

    # COMBAT LOOP START
    while charHP > 0:
        printCombatHP(
            charHP,
            enemyWarrior,
            enemyWarriorHP)  # Using function created earlier for combat HP

        if charInventory[0] == "Sword":
            charHitChance = random.uniform(
                0.2,
                1.0)  # Weapon specific hit chance
            if charHitChance >= hitChance:
                charDmg = random.randint(1, 4)
                # Making sure that damage does not exceed health (no minus
                # health)
                if charDmg >= enemyWarriorHP:
                    charDmg = enemyWarriorHP
                # Damage is subtracted from HP, result then stored again within
                # the HP variable
                enemyWarriorHP -= charDmg
                print("You sucessfully hit!\n")
                time.sleep(3)
                print(
                    "You slash at the",
                    enemyWarrior,
                    "severing a few arteries inflicting",
                    charDmg,
                    "damage!\n")
                time.sleep(3)

                if enemyWarriorHP <= 0:
                    printCombatHP(charHP, enemyWarrior, enemyWarriorHP)
                    print("The", enemyWarrior, "falls before you.\n")
                    break

                enemyHitChance = random.uniform(0.1, 1.0)
                if enemyHitChance >= hitChance:
                    enemyWarriorDmg = random.randint(1, 4)
                    if enemyWarriorDmg >= charHP:
                        enemyWarriorDmg = charHP
                    charHP -= enemyWarriorDmg
                    print("The", enemyWarrior, "hits!\n")
                    print(
                        "The",
                        enemyWarrior,
                        "strikes you dealing",
                        enemyWarriorDmg,
                        "damage!\n")
                    time.sleep(3)

                    if charHP <= 0:
                        printCombatHP(charHP, enemyWarrior, enemyWarriorHP)
                        print(
                            "Unfortunately",
                            charName,
                            "you were defeated in combat.\n")
                        break
                    continue

                else:
                    print(
                        "Luckily he misses and you successfully dodge his attack!\n")
                    time.sleep(3)
                    continue

            else:
                print(
                    "Unfortunately you failed to successfully strike the",
                    enemyWarrior,
                    "and they parry your attack!\n")
                time.sleep(3)

                enemyHitChance = random.uniform(0.1, 1.0)
                if enemyHitChance >= hitChance:
                    enemyWarriorDmg = random.randint(1, 4)
                    if enemyWarriorDmg >= charHP:
                        enemyWarriorDmg = charHP
                    charHP -= enemyWarriorDmg
                    print("The", enemyWarrior, "hits!\n")
                    print(
                        "The",
                        enemyWarrior,
                        "strikes you dealing",
                        enemyWarriorDmg,
                        "damage!\n")
                    time.sleep(3)
                    if charHP <= 0:
                        print(
                            "Unfortunately",
                            charName,
                            "you were defeated in combat.\n")
                        break
                    continue

        if charInventory[0] == "Axe":
            charHitChance = random.uniform(0.0, 1.0)
            if charHitChance >= hitChance:
                charDmg = random.randint(1, 8)
                if charDmg >= enemyWarriorHP:
                    charDmg = enemyWarriorHP
                enemyWarriorHP -= charDmg
                print("You sucessfully hit!\n")
                time.sleep(3)
                print(
                    "You cleave at the",
                    enemyWarrior,
                    "severing a few arteries inflicting",
                    charDmg,
                    "damage!\n")
                time.sleep(3)

                if enemyWarriorHP <= 0:
                    printCombatHP(charHP, enemyWarrior, enemyWarriorHP)
                    print("The", enemyWarrior, "falls before you.\n")
                    break

                enemyHitChance = random.uniform(0.1, 1.0)
                if enemyHitChance >= hitChance:
                    enemyWarriorDmg = random.randint(1, 4)
                    if enemyWarriorDmg >= charHP:
                        enemyWarriorDmg = charHP
                    charHP -= enemyWarriorDmg
                    print("The", enemyWarrior, "hits!\n")
                    print(
                        "The",
                        enemyWarrior,
                        "strikes you dealing",
                        enemyWarriorDmg,
                        "damage!\n")
                    time.sleep(3)

                    if charHP <= 0:
                        print(
                            "Unfortunately",
                            charName,
                            "you were defeated in combat.\n")
                        break
                    continue

                else:
                    print("Luckily he misses you!\n")
                    time.sleep(3)
                    continue

            else:
                print(
                    "Unfortunately your attack misses as the",
                    enemyWarrior,
                    "dodges to the side!\n")
                time.sleep(3)

                enemyHitChance = random.uniform(0.1, 1.0)
                if enemyHitChance >= hitChance:
                    enemyWarriorDmg = random.randint(1, 4)
                    if enemyWarriorDmg >= charHP:
                        enemyWarriorDmg = charHP
                    charHP -= enemyWarriorDmg
                    print("The", enemyWarrior, "hits!\n")
                    print(
                        "The",
                        enemyWarrior,
                        "strikes you dealing",
                        enemyWarriorDmg,
                        "damage!\n")
                    time.sleep(3)
                    if charHP <= 0:
                        print(
                            "Unfortunately",
                            charName,
                            "you were defeated in combat.\n")
                        break
                    continue

                else:
                    print("Luckily he misses you!\n")
                    time.sleep(3)
                    continue

        if charInventory[0] == "Spear":
            charHitChance = random.uniform(0.4, 1.0)
            if charHitChance >= hitChance:
                charDmg = random.randint(1, 3)
                if charDmg >= enemyWarriorHP:
                    charDmg = enemyWarriorHP
                enemyWarriorHP -= charDmg
                print("You sucessfully hit!\n")
                time.sleep(3)
                print(
                    "You drive your spear right into the",
                    enemyWarrior,
                    "dealing",
                    charDmg,
                    "damage!\n")
                time.sleep(3)

                if enemyWarriorHP <= 0:
                    printCombatHP(charHP, enemyWarrior, enemyWarriorHP)
                    print("The", enemyWarrior, "falls before you.\n")
                    break

            else:
                # This line should never run.
                print(
                    "Unfortunately you missed somehow with the 100% accurate weapon wtf\n")
                time.sleep(3)

            enemyHitChance = random.uniform(0.1, 1.0)
            if enemyHitChance >= hitChance:
                enemyWarriorDmg = random.randint(1, 4)
                if enemyWarriorDmg >= charHP:
                    enemyWarriorDmg = charHP
                charHP -= enemyWarriorDmg
                print("The", enemyWarrior, "hits!\n")
                time.sleep(3)
                print(
                    "The",
                    enemyWarrior,
                    "strikes you dealing",
                    enemyWarriorDmg,
                    "damage!\n")
                time.sleep(3)
                if charHP <= 0:
                    printCombatHP(charHP, enemyWarrior, enemyWarriorHP)
                    print(
                        "Unfortunately",
                        charName,
                        "you were defeated in combat.\n")
                    break
                continue

        if charInventory[0] == "Crossbow":
            charHitChance = random.uniform(0.2, 1.0)
            if charHitChance >= hitChance:
                charDmg = random.randint(1, 4)
                if charDmg >= enemyWarriorHP:
                    charDmg = enemyWarriorHP
                enemyWarriorHP -= charDmg
                print("You sucessfully hit!\n")
                time.sleep(3)
                print(
                    "You ready your",
                    charWeapon,
                    "and fire a bolt at the",
                    enemyWarrior,
                    "! piercing his armour and dealing",
                    charDmg,
                    "damage!\n")
                time.sleep(3)
                if enemyWarriorHP <= 0:
                    printCombatHP(charHP, enemyWarrior, enemyWarriorHP)
                    print("The", enemyWarrior, "falls before you.\n")
                    break

                enemyHitChance = random.uniform(0.3, 1.0)
                if enemyHitChance >= hitChance:
                    enemyWarriorDmg = random.randint(1, 4)
                    if enemyWarriorDmg >= charHP:
                        enemyWarriorDmg = charHP
                    charHP -= enemyWarriorDmg
                    print("The", enemyWarrior, "hits!\n")
                    print(
                        "The",
                        enemyWarrior,
                        "strikes you dealing",
                        enemyWarriorDmg,
                        "damage!\n")
                    time.sleep(3)

                    if charHP <= 0:
                        print(
                            "Unfortunately",
                            charName,
                            "you were defeated in combat.\n")
                        break
                    continue
                else:
                    print("Luckily he misses you!\n")

            else:
                print("Unfortunately you missed!\n")
                time.sleep(3)
                enemyHitChance = random.uniform(0.1, 1.0)
                if enemyHitChance >= hitChance:
                    enemyWarriorDmg = random.randint(1, 4)
                    if enemyWarriorDmg >= charHP:
                        enemyWarriorDmg = charHP
                    charHP -= enemyWarriorDmg
                    print("The", enemyWarrior, "hits!\n")
                    time.sleep(3)
                    print(
                        "The",
                        enemyWarrior,
                        "strikes you dealing",
                        enemyWarriorDmg,
                        "damage!\n")
                    time.sleep(3)
                    if charHP <= 0:
                        print(
                            "Unfortunately",
                            charName,
                            "you were defeated in combat.\n")
                        break
                    continue
    # COMBAT LOOP END

    if charHP > 0:
        print("Congratulations!\n")
    else:
        replay = str(input("Try again? Yes/No\n"))
        replay = replay.upper()
        if replay == "NO":
            print(
                "I hope you enjoyed your time playing The Legend of The Forgotten Realms!")
