##This is Python Code

import random
import time

##while True:
##    rand = random.randint(1,3)
##    if rand == 1:
##        print('No')
##    if rand == 2:
##        print('Nope')
##    if rand == 3:
##        print('Nuh-Uh')

hp = 100
maxhp = 100
attk = 15
crit = 0.15
defense = 0.0
xp = 0
level = 1
pclass = 'placeholder'
gold = 0
xpgoal = 5
name = ''
critchance = 20
weapon = 'Fist'
wins = 0
totalwins = 0
totallosses = 0
highestlevel = 0
pets = 0
loadedgame = []
played = False
version = 'BETA 1.0.7'
inventory = ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'None', 'None']
experiments = 0

class Enemy:
    def __init__(self, name, atk, hp, critdam, maxhp, defe, critchance):
        self.name = name
        self.atk = atk
        self.hp = hp
        self.critdam = critdam
        self.maxhp = maxhp
        self.defe = defe
        self.critchance = critchance
        #self.petchance = petchance
        
sline = Enemy('Sline', 17, 100, 0.15, 100, 0.0, 0)
smake = Enemy('Smake', 20, 89, 0.13, 89, 0.0, 0)
skeletom = Enemy('Skeletom', 15, 105, 0.1, 105, 0.0, 0)
LEAF = Enemy('LEAF', 17, 115, 0.17, 105, 0.0, 0)
nagic = Enemy('Nagic', 17, 100, 0.15, 100, 0.0, 0)
platypus = Enemy('Platypus', 18, 90, 0.12, 90, 0.0, 0)

class Weapon:
    def __init__(self, name, dmg, cost, critchanceup, isininventory):
        self.name = name
        self.dmg = dmg
        self.cost = cost
        self.critchanceup = critchanceup
        self.isininventory = isininventory

sword = Weapon('Sword', 10, 20, 1, False)
mace = Weapon('Mace', 8, 15, 1, False)
leaf = Weapon('LEAF', 100, 200, 3, False)

print(f'[|=====|]')
time.sleep(0.5)
print(f'[|-====|]')
time.sleep(0.5)
print(f'[|--===|]')
time.sleep(0.5)
print(f'[|---==|]')
time.sleep(0.5)
print(f'[|----=|]')
time.sleep(0.5)
print(f'[|-----|]')
print(f'Load Complete!')
print()
time.sleep(0.5)
print(f'I present...')
time.sleep(1)
print(f'Fist Fight {version}!')
print()
time.sleep(1)
print(f'New game (new) or load game (load)?')
choice = input()

if choice == 'load':
    file = open('SaveFileFistFight.txt', 'r')
    read = file.readlines()
    for line in read:
        loadedgame.append(line.strip())
    length = len(loadedgame)
    if length == 21:
        hpstr = loadedgame[0]
        maxhpstr = loadedgame[1]
        attkstr = loadedgame[2]
        critstr = loadedgame[3]
        defensestr = loadedgame[4]
        pclass = loadedgame[5]
        goldstr = loadedgame[6]
        name = loadedgame[7]
        totalwinsstr = loadedgame[8]
        totallossesstr = loadedgame[9]
        highestlevelstr = loadedgame[10]
        petsstr = loadedgame[11]
        experimentsstr = loadedgame[12]
        inventory[0] = loadedgame[13]
        inventory[1] = loadedgame[14]
        inventory[2] = loadedgame[15]
        inventory[3] = loadedgame[16]
        inventory[4] = loadedgame[17]
        inventory[5] = loadedgame[18]
        inventory[6] = loadedgame[19]
        inventory[7] = loadedgame[20]
        experiments = int(experimentsstr)
        hp = int(hpstr)
        maxhp = int(maxhpstr)
        attk = int(attkstr)
        crit = float(critstr)
        defense = float(defensestr)
        gold = int(goldstr)
        totalwins = int(totalwinsstr)
        totallosses = int(totallossesstr)
        highestlevel = int(highestlevelstr)
        pets = int(petsstr)
        print()
        print(f"Game loaded successfully!")
        print(f"Please now delete the SaveFilesFistFight.txt file.")

    elif length == 22:
        hpstr = loadedgame[0]
        maxhpstr = loadedgame[1]
        attkstr = loadedgame[2]
        critstr = loadedgame[3]
        defensestr = loadedgame[4]
        pclass = loadedgame[5]
        goldstr = loadedgame[6]
        name = loadedgame[7]
        totalwinsstr = loadedgame[8]
        totallossesstr = loadedgame[9]
        highestlevelstr = loadedgame[10]
        petsstr = loadedgame[11]
        petname = loadedgame[12]
        experimentsstr = loadedgame[13]
        inventory[0] = loadedgame[13]
        inventory[1] = loadedgame[14]
        inventory[2] = loadedgame[15]
        inventory[3] = loadedgame[16]
        inventory[4] = loadedgame[17]
        inventory[5] = loadedgame[18]
        inventory[6] = loadedgame[19]
        inventory[7] = loadedgame[20]
        experiments = int(experimentsstr)
        hp = int(hpstr)
        maxhp = int(maxhpstr)
        attk = int(attkstr)
        crit = float(critstr)
        defense = float(defensestr)
        gold = int(goldstr)
        totalwins = int(totalwinsstr)
        totallosses = int(totallossesstr)
        highestlevel = int(highestlevelstr)
        pets = int(petsstr)
        print()
        print(f"Game loaded successfully!")
        print(f"Please now delete the SaveFilesFistFight.txt file.")

    else:
        print(f'Not able to load.')
        
else:
    print("Would you like to activate Experiments? They can be glitchy and usually have bugs! [It is recommended that PlayTesters activate this setting] y/n")
    niput = input()
    
    if niput == 'Y' or niput == 'y':
        print()
        print(f"You decided to turn on Experiments.")
        experiments = 1
        
    else:
        print()
        print(f"You decided not to activate Experiments.")
        experiments = 0
        
    print(f'What would you like your name to be?')
    name = input()
    print()
    
    if name == 'Audrey':
        name = 'bad name'
        maxhp = 0
        print('Bad name. >:(')
        print()

    print(f"Welcome to Fist Fight, {name}!!")
    print()
    print(f'What class would you like to be? different classes apply different traits. You can choose from Nage (nage), Kmight (kmight), Barbariam (barbariam), or Fish (fish).')
    loop = True
    
    while loop == True:
        niput = input()
        
        if niput == 'nage':
            print()
            print(f'You chose to become a nage! Good choice. Being a nage buffs your attack, critical hit bonus, and defense.')
            pclass = 'Nage'
            xpgoal = 7
            defense = 0.06
            attk = 17
            crit = 0.18
            loop = False
            
        elif niput == 'kmight':
            print()
            print(f'You chose to become a kmight! Good choice. Being a kmight buffs your defense, attack, and health.')
            pclass = 'Kmight'
            crit = 0.13
            maxhp = 105
            hp = 105
            defense = 0.05
            attk += 3
            loop = False

        elif niput == 'fish':
            print()
            print(f'You chose to become a fish! Good choice. Being a kmight buffs your attack, health, and critical hit damage.')
            pclass = 'Fish'
            crit = 0.15
            maxhp = 110
            hp = 110
            loop = False

        elif niput == 'barbariam':
            print()
            print(f'You chose to become a barbariam! Good choice. Being a barbariam buffs your critical hit chance, attack, and critical hit damage.')
            pclass = 'Barbariam'
            maxhp = 95
            crit = 0.20
            critchance -= 2
            attk += 5
            loop = False
            
        elif niput == 'leaf':
            print(f'Please input the password. ________')
            pas = input()
            
            if pas == 'password':
                print(f'Please enter password #2. _________')
                passw = 'i am LEAF'
                pas = input()
                
                if pas == passw:
                    print()
                    print(f'You chose to become a leaf! Good choice. Being a leaf makes you god!')
                    maxhp = 1000
                    hp = 1000
                    defense = 0.60
                    attk += 100
                    loop = False
                    
                else:
                    print(f'HAHAHAHAHAHAHAHA >:)')
                    
            else:
                print(f'Leaf me alone :(')
                print()
                
        else:
            print(f'Please choose a valid class. You must choose nage or kmight.')
            
buffs = [xpgoal, defense, attk, crit, hp, maxhp, critchance]

print()
print(f'Welcome to the dungeon.')
print()
gameloop = True

while gameloop == True:
    hp = maxhp
    print()
    print(f'FIST FIGHT')
    print(f'Main Menu')
    print()
    print(f'Options:')
    print(f'Fight! (fight)')
    
    if experiments == 1:
        print(f'Equip Items! (eitems)')
        
    else:
        print(f'This action is locked behind the Experiment setting.')
    print(f'Save Game! (save game)')
    
    if pets > 0:
        print(f'Pets! (pets)')
        
    else:
        print(f'[Locked]')
        
    if experiments == 1:
        print(f'Shop! (shop)')
        
    else:
        print(f'This action is locked behind the Experiment setting.')
        
    print(f'Stats! (stats)')
    print(f'Quit Game! (qgame)')
    print(f'Credits! (credits)')
    niput = input()
    print()
    
    if niput == 'fight' or niput == 'Fight' or niput == 'fight!' or niput == 'Fight!':
        loop = True
        
        while loop == True:
            enemy = random.randint(1,6)
            
            if enemy == 1:
                currentenemy = sline
                
            elif enemy == 2:
                currentenemy = smake
                
            elif enemy == 3:
                currentenemy = skeletom
                
            elif enemy == 4:
                currentenemy = LEAF
                
            elif enemy == 5:
                currentenemy = nagic
                
            elif enemy == 6:
                currentenemy = platypus
                
            print(f'A wild {currentenemy.name} has appeared!')
            hp = maxhp
            currentenemy.hp = currentenemy.maxhp
            
            if wins == 10: currentenemy.hp += 10
            print()
            loop1 = True
            
            while loop1 == True:
                
                if loop1 == True:
                    hp = int(hp)
                    maxhp = int(maxhp)
                    attk = int(attk)
                    crit = float(crit)
                    defense = float(defense)
                    gold = int(gold)
                    totalwins = int(totalwins)
                    totallosses = int(totallosses)
                    highestlevel = int(highestlevel)
                    pets = int(pets)
                    
                    if currentenemy.hp <= 0:
                        thing = random.randint(2,5)
                        xp += thing
                        wins += 1
                        totalwins += 1
                        
                        if level > highestlevel: highestlevel = level
                        
                        goldget = random.randint(1,5)
                        gold += goldget
                        print(f'You won the battle! Congratulations! You got {thing} xp and {goldget} gold!')
                        
                        if xp >= xpgoal:
                            xp -= xpgoal
                            xpgoal += 5
                            level += 1
                            eupgrade = random.randint(1,4)
                            
                            if eupgrade == 1:
                                sline.hp += 7
                                sline.maxhp += 7
                                smake.hp += 7
                                smake.maxhp += 7
                                skeletom.hp += 7
                                skeletom.maxhp += 7
                                LEAF.hp += 7
                                LEAF.maxhp += 7
                                platypus.hp += 7
                                platypus.maxhp += 7
                                nagic.hp += 7
                                nagic.maxhp += 7
                                
                            elif eupgrade == 2:
                                sline.atk += 7
                                smake.atk += 7
                                skeletom.atk += 7
                                LEAF.atk += 7
                                platypus.atk += 7
                                nagic.atk += 7
                                
                            elif eupgrade == 3:
                                sline.defe += 0.05
                                smake.defe += 0.05
                                skeletom.defe += 0.05
                                LEAF.defe += 0.05
                                platypus.defe += 0.05
                                nagic.defe += 0.05

                            elif eupgrade == 4 and currentenemy.critchance >= 5:
                                sline.critchance -= 1
                                smake.critchance -= 1
                                skeletom.critchance -= 1
                                LEAF.critchance -= 1
                                platypus.critchance -= 1
                                nagic.critchance -= 1
                                
                            print(f'You leveled up! Congrats! You are now level {level}!')
                            print(f'You get a bonus upgrade! Your options are to upgrade defense, attack, and health.')
                            
                            if critchance >= 5:
                                print(f'You are able to upgrade your chance of getting a critical hit (crit).')
                                
                            else:
                                print(f'Critical hit chance: MAX')
                                
                            niput = input()
                            
                            if niput == 'health':
                                maxhp += 4
                                
                            elif niput == 'attack':
                                attk += 7
                                
                            elif niput == 'defense':
                                defense += 0.03
                                
                            elif niput == 'crit' and critchance >= 5:
                                critchance -= 1
                                
                        loop1 = False
                        wins += 1
                        
                    elif hp <= 0:
                        totallosses += 1
                        print(f'You lost. :( You defeated {wins} enemies.')
                        print(f'Would you like to play again? This cost 3 gold. You have {gold} gold.y/n')
                        loop2 = True
                        
                        while loop2 == True:
                            niput = input()
                            
                            if niput == 'y' and gold >= 3 or niput == 'Y' and gold >= 3:
                                gold -= 3
#                                hp = [4]
#                                maxhp = [5]
#                                attk = [2]
#                                crit = [3]
#                                defense = [1]
#                                xp = 0
#                                level = 1
#                                xpgoal = [0]
#                                critchance = [6]
#                                wins = 0
#                                ##eupgradehp = randint(1,3)
#                                                                
#                                class Enemy:
#                                    def __init__(self, name, atk, hp, critdam, maxhp, defe, critchance):
#                                        self.name = name
#                                        self.atk = atk
#                                        self.hp = hp
#                                        self.critdam = critdam
#                                        self.maxhp = maxhp
#                                        self.defe = defe
#                                        self.critchance = critchance
#                                        
#                                sline = Enemy('Sline', 12, 100, 0.15, 100, 0.0, 0)
#                                smake = Enemy('Smake', 15, 89, 0.13, 89, 0.0, 0)
#                                skeletom = Enemy('Skeletom', 15, 105, 0.1, 105, 0.0, 0)
#                                LEAF = Enemy('LEAF', 16, 105, 0.17, 105, 0.0, 0)
#                                nagic = Enemy('Nagic', 15, 100, 0.15, 100, 0.0, 0)
#                                platypus = Enemy('Platypus', 12, 90, 0.12, 90, 0.0, 0)
#                                
#                                class Weapon:
#                                    def __init__(self, name, dmg, cost, critchanceup, isininventory):
#                                        self.name = name
#                                        self.dmg = dmg
#                                        self.cost = cost
#                                        self.critchanceup = critchanceup
#                                        self.isininventory = isininventory#\
#
#                                sword = Weapon('Sword', 10, 20, 1, False)
#                                mace = Weapon('Mace', 8, 15, 1, False)
#                                leaf = Weapon('LEAF', 100, 350, 3, False)
                                loop2 = False
                                
                            else:
                                print(f'Are you sure? y/n')
                                niput = input()
                                
                                if niput == 'y' or niput == 'Y':
                                    loop2 = False
                                    loop1 = False
                                    loop = False
                                    
                                else:
                                    print()
                                    print(f'Would you like to play again? y/n')
                        
                    elif hp > 0 and currentenemy.hp > 0:
                        ##hp = int(hp * 1000) / 1000
                        critchanc = buffs[6]
                        ##currentenemy.hp = int(currentenemy.hp * 1000) / 1000
                        
                        if hp > maxhp: hp = maxhp
                        
                        if currentenemy.hp > currentenemy.maxhp: currentenemy.hp = currentenemy.maxhp
                        currentenemy.hp = round(currentenemy.hp, 1)
                        hp = round(hp, 1)
                        print(f"Health: You: {hp}. {currentenemy.name}: {currentenemy.hp}.")
                        print(f'What will you do? You can heal, attack, or run away (h,a, or r)')
                        
                        if currentenemy.hp <= 10 and level >= 2 and pets == 0 and experiments == 1:
                            print(f'You can capture this enemy and make it your pet! (pet)')
                            
                        niput = input()
                        print()
                        
                        if niput == 'attack' or niput == 'a':
                            critc = random.randint(1,critchanc)
                            dmgvary = random.randint(1,3)
                                  
                            if critc == 1:
                                critatk = attk * crit
                                totalatk = critatk + attk
                                edefe = totalatk * currentenemy.defe
                                totalatk -= edefe
                                totalatk = round(totalatk, 1)
                                  
                                if dmgvary == 1:
                                    totalatk += 1
                                  
                                if dmgvary == 2:
                                    totalatk -= 1
                                  
                                if dmgvary == 3:
                                    totalatk = totalatk
                                  
                                currentenemy.hp -= totalatk
                                print(f'You got a critical hit! You did {totalatk} damage with your {weapon}.')
                                
                            else:
                                edefe = attk * currentenemy.defe
                                totalatk = attk - edefe
                                totalatk = round(totalatk)
                                  
                                if dmgvary == 1:
                                    totalatk += 1
                                  
                                if dmgvary == 2:
                                    totalatk -= 1
                                  
                                if dmgvary == 3:
                                    totalatk = totalatk
                                  
                                currentenemy.hp -= totalatk
                                print(f'You attacked the {currentenemy.name} with your {weapon} and did {totalatk} damage.')
                                
                        elif niput == 'heal' or niput == 'h':
                            healamount = random.randint(20,35)
                            hp += healamount
                            print(f'You healed yourself and healed {healamount} health.')
                            
                        elif niput == 'run away' or niput == 'r':
                            print(f'You decided to run away. You ended up at level {level} and you defeated {wins} enemies.')
                            print(f'Would you like to go back to the main menu? Staying in the game costs 3 gold. You have {gold} gold. y/n')
                            niput = input()
                            
                            if niput == 'n' or niput == 'N' and gold >= 3:
                                gold -= 3
                                print(f'You continued the game.')
                                print()
                                
                            elif niput == 'y' or niput == 'Y' and gold <= 3:
                                print(f"Sadly, you didn't have enough gold to continue. You have to go back to the main menu.")
                                loop1 = False
                                totallosses += 1
#                                hp = [4]
#                                maxhp = [5]
#                                attk = [2]
#                                crit = [3]
#                                defense = [1]
#                                xp = 0
#                                level = 1
#                                xpgoal = [0]
#                                critchance = [6]
#                                wins = 0
#                                ##eupgradehp = randint(1,3)
#                                                                
#                                class Enemy:
#                                    def __init__(self, name, atk, hp, critdam, maxhp, defe, critchance):
#                                        self.name = name
#                                        self.atk = atk
#                                        self.hp = hp
#                                        self.critdam = critdam
#                                        self.maxhp = maxhp
#                                        self.defe = defe
#                                        self.critchance = critchance
#                                        
#                                sline = Enemy('Sline', 12, 100, 0.15, 100, 0.0, 0)
#                                smake = Enemy('Smake', 15, 89, 0.13, 89, 0.0, 0)
#                                skeletom = Enemy('Skeletom', 15, 105, 0.1, 105, 0.0, 0)
#                                LEAF = Enemy('LEAF', 16, 105, 0.17, 105, 0.0, 0)
#                                nagic = Enemy('Nagic', 15, 100, 0.15, 100, 0.0, 0)
#                                platypus = Enemy('Platypus', 12, 90, 0.12, 90, 0.0, 0)
#                                
#                                class Weapon:
#                                    def __init__(self, name, dmg, cost, critchanceup, isininventory):
#                                        self.name = name
#                                        self.dmg = dmg
#                                        self.cost = cost
#                                        self.critchanceup = critchanceup
#                                        self.isininventory = isininventory#\
#
#                                sword = Weapon('Sword', 10, 20, 1, False)
#                                mace = Weapon('Mace', 8, 15, 1, False)
#                                leaf = Weapon('LEAF', 100, 350, 3, False)
                                
                            else:
                                print(f'You went back to the main menu.')
                                loop1 = False
                                totallosses += 1
#                                hp = [4]
#                                maxhp = [5]
#                                attk = [2]
#                                crit = [3]
#                                defense = [1]
#                                xp = 0
#                                level = 1
#                                xpgoal = [0]
#                                critchance = [6]
#                                wins = 0
#                                ##eupgradehp = randint(1,3)
#                                                                
#                                class Enemy:
#                                    def __init__(self, name, atk, hp, critdam, maxhp, defe, critchance):
#                                        self.name = name
#                                        self.atk = atk
#                                        self.hp = hp
#                                        self.critdam = critdam
#                                        self.maxhp = maxhp
#                                        self.defe = defe
#                                        self.critchance = critchance
#                                        
#                                sline = Enemy('Sline', 12, 100, 0.15, 100, 0.0, 0)
#                                smake = Enemy('Smake', 15, 89, 0.13, 89, 0.0, 0)
#                                skeletom = Enemy('Skeletom', 15, 105, 0.1, 105, 0.0, 0)
#                                LEAF = Enemy('LEAF', 16, 105, 0.17, 105, 0.0, 0)
#                                nagic = Enemy('Nagic', 15, 100, 0.15, 100, 0.0, 0)
#                                platypus = Enemy('Platypus', 12, 90, 0.12, 90, 0.0, 0)
#                                
#                                class Weapon:
#                                    def __init__(self, name, dmg, cost, critchanceup, isininventory):
#                                        self.name = name
#                                        self.dmg = dmg
#                                        self.cost = cost
#                                        self.critchanceup = critchanceup
#                                        self.isininventory = isininventory#\
#
#                                sword = Weapon('Sword', 10, 20, 1, False)
#                                mace = Weapon('Mace', 8, 15, 1, False)
#                                leaf = Weapon('LEAF', 100, 350, 3, False)

                        elif currentenemy.hp <= 10 and level >= 2 and niput == 'pet' and experiments == 1:
                            getpet = random.randint(1,3)
                            
                            if getpet == 1:
                                print(f'You failed to tame the enemy.')
                                
                            else:
                                print(f'You successfully got a pet {currentenemy.name} that you can bring into future battles with you!')
                                currentenemy.hp = currentenemy.maxhp
                                petname = currentenemy.name
                                loop2 = False
                                petstats = currentenemy
                                pets = 1
                                
                        else:
                            print(f'That is not a valid action.')

                        if loop1 == True:
                            print()
                            rando = random.randint(1,11)
                            
                            if currentenemy.hp < currentenemy.hp * 0.9 and rando == 1:
                                healamount = random.randint(25,35)
                                print(f'The {currentenemy.name} healed {healamount} health!')
                                
                            else:
                                ecritchance = 20
                                ecritchance -= currentenemy.critchance
                                cri = random.randint(1,ecritchance)
                                dmgvary = random.randint(1,3)
                                  
                                if cri == 1:
                                    critatk = currentenemy.atk * currentenemy.critdam
                                    atk = critatk + currentenemy.atk
                                    resist = atk * defense
                                    atk -= resist
                                    atk = round(atk, 1)
                                  
                                    if dmgvary == 1:
                                        atk += 1
                                  
                                    if dmgvary == 2:
                                        atk -= 1
                                  
                                    if dmgvary == 3:
                                        atk = atk
                                  
                                    hp -= atk
                                    print(f'The {currentenemy.name} got a critical hit! They did {atk} damage.')
                                    
                                else:
                                    atk = currentenemy.atk
                                    resist = atk * defense
                                    atk -= resist
                                    atk = round(atk)
                                          
                                    if dmgvary == 1:
                                        atk += 1
                                          
                                    if dmgvary == 2:
                                        atk -= 1
                                          
                                    if dmgvary == 3:
                                        atk = atk
                                          
                                    hp -= atk
                                    print(f'The {currentenemy.name} attacked you and did {atk} damage!')
                                print()
        
                    
                
    elif niput == 'credits' or niput == 'Credits' or niput == 'credits!' or niput == 'Credits!':
        print(f'Credits:')
        print()
        print(f'Creator & Programmer: Joey Bacon, Docter of Computer Science & Programming')
        print(f'Engine: IDLE Python Shell 3.11.4/3.11.5')
        print(f'Game version: {version}.')
        print(f'Playtesters: Eli Cardoso, Soar Mutl, Molly Bacon, Mateo Donado, Noah Magone, ')
        ##Type your first and last names here, inside the quote
        print()
        print(f'Return to Main Menu?')
        niput = input()

    elif niput == 'shop' or niput == 'Shop' or niput == 'shop!' or niput == 'Shop!' and experiments == 1:
        print(f'Welcome to the shop! There are a few things for sale.')
        item1 = random.randint(1,5)
        item2 = random.randint(1,5)
        item3 = random.randint(1,5)
        print()
        print(f'You have', gold, 'gold.')
                                          
        if item1 == 1:
            item1 = 'Tooth Relic (trelic) - 25 Gold'
                                          
        if item1 == 2:
            item1 = 'Heart Relic (hrelic) - 40 Gold'
                                          
        if item1 == 3:
            item1 = '[OUT OF STOCK]'
                                          
        if item1 == 4:
            item1 = 'Dagger (dagger) - 60 Gold'
                                          
        if item1 == 5:
            item1 = 'Shield Relic (srelic) - 50 Gold'
                                          
        if item2 == 1:
            item2 = 'Tooth Relic (trelic) - 25 Gold'
                                          
        if item2 == 2:
            item2 = 'Heart Relic (hrelic) - 40 Gold'
                                          
        if item2 == 3:
            item2 = '[OUT OF STOCK]'
                                          
        if item2 == 4:
            item2 = 'Dagger (dagger) - 60 Gold'
                                          
        if item2 == 5:
            item2 = 'Shield Relic (srelic) - 50 Gold'
                                          
        if item3 == 1:
            item3 = 'Tooth Relic (trelic) - 25 Gold'
                                          
        if item3 == 2:
            item3 = 'Heart Relic (hrelic) - 40 Gold'
                                          
        if item3 == 3:
            item3 = '[OUT OF STOCK]'
                                          
        if item3 == 4:
            item3 = 'Dagger (dagger) - 60 Gold'
                                          
        if item3 == 5:
            item3 = 'Shield Relic (srelic) - 50 Gold'

        print()
        print(f'Items for sale:')
        print(f'Item 1: {item1}!')
        print(f'Item 2: {item2}!')
        print(f'Item 3: {item3}!')
        print()
        print(f'Please choose which item you want. If you do not want any items, type no.')
        niput = input()
              
        if niput == 'trelic' and item1 == 'Tooth Relic (trelic) - 25 Gold' or niput == 'trelic' and item2 == 'Tooth Relic (trelic) - 25 Gold' or niput == 'trelic' and item3 == 'Tooth Relic (trelic) - 25 Gold':
            
            if gold >= 25:
                
                if inventory[0] == 'Empty' or inventory[1] == 'Empty' or inventory[2] == 'Empty' or inventory[3] == 'Empty' or inventory[4] == 'Empty' or inventory[5] == 'Empty':
                    print()
                    print('You bought the Tooth Relic.')
                    gold -= 25
                    
                    if inventory[0] == 'Empty':
                        inventory[0] = 'Tooth Relic - Increases Critical hit damage'
                        
                    elif inventory[1] == 'Empty':
                        inventory[1] = 'Tooth Relic - Increases Critical hit damage'
                        
                    elif inventory[2] == 'Empty':
                        inventory[2] = 'Tooth Relic - Increases Critical hit damage'
                        
                    elif inventory[3] == 'Empty':
                        inventory[3] = 'Tooth Relic - Increases Critical hit damage'
                        
                    elif inventory[4] == 'Empty':
                        inventory[4] = 'Tooth Relic - Increases Critical hit damage'
                        
                    elif inventory[5] == 'Empty':
                        inventory[5] = 'Tooth Relic - Increases Critical hit damage'
                else:
                    print("You don't have enough iventory space.")
                
            elif gold < 25:
                print()
                print('You do not have enough gold for this item.')

        elif niput == 'srelic' and item1 == 'Shield Relic (srelic) - 50 Gold' or niput == 'srelic' and item2 == 'Shield Relic (srelic) - 50 Gold' or niput == 'srelic' and item3 == 'Shield Relic (srelic) - 50 Gold':
            
            if gold >= 50:
                
                if inventory[0] == 'Empty' or inventory[1] == 'Empty' or inventory[2] == 'Empty' or inventory[3] == 'Empty' or inventory[4] == 'Empty' or inventory[5] == 'Empty':
                    print()
                    print('You bought the Shield Relic.')
                    gold -= 50
                    
                    if inventory[0] == 'Empty':
                        inventory[0] = 'Shield Relic - Increases defense'
                        
                    elif inventory[1] == 'Empty':
                        inventory[1] = 'Shield Relic - Increases defense'
                        
                    elif inventory[2] == 'Empty':
                        inventory[2] = 'Shield Relic - Increases defense'
                        
                    elif inventory[3] == 'Empty':
                        inventory[3] = 'Shield Relic - Increases defense'
                        
                    elif inventory[4] == 'Empty':
                        inventory[4] = 'Shield Relic - Increases defense'
                        
                    elif inventory[5] == 'Empty':
                        inventory[5] = 'Shield Relic - Increases defense'
                        
                else:
                    print("You don't have enough iventory space.")
                
            elif gold < 50:
                print()
                print('You do not have enough gold for this item.')

        elif niput == 'dagger' and item1 == 'Dagger (dagger) - 60 Gold' or niput == 'dagger' and item2 == 'Dagger (dagger) - 60 Gold' or niput == 'dagger' and item3 == 'Dagger (dagger) - 60 Gold':
            
            if gold >= 60:
                
                if inventory[0] == 'Empty' or inventory[1] == 'Empty' or inventory[2] == 'Empty' or inventory[3] == 'Empty' or inventory[4] == 'Empty' or inventory[5] == 'Empty':
                    print()
                    print('You bought the Dagger.')
                    gold -= 60
                    
                    if inventory[0] == 'Empty':
                        inventory[0] = 'Dagger - Increases damage'
                        
                    elif inventory[1] == 'Empty':
                        inventory[1] = 'Dagger - Increases damage'
                        
                    elif inventory[2] == 'Empty':
                        inventory[2] = 'Dagger - Increases damage'
                        
                    elif inventory[3] == 'Empty':
                        inventory[3] = 'Dagger - Increases damage'
                        
                    elif inventory[4] == 'Empty':
                        inventory[4] = 'Dagger - Increases damage'
                        
                    elif inventory[5] == 'Empty':
                        inventory[5] = 'Dagger - Increases damage'
                        
                else:
                    print("You don't have enough iventory space.")
                
            elif gold < 60:
                print()
                print('You do not have enough gold for this item.')

        elif niput == 'hrelic' and item1 == 'Heart Relic (hrelic) - 40 Gold' or niput == 'hrelic' and item2 == 'Heart Relic (hrelic) - 40 Gold' or niput == 'hrelic' and item3 == 'Heart Relic (hrelic) - 40 Gold':
            
            if gold >= 40:
                
                if inventory[0] == 'Empty' or inventory[1] == 'Empty' or inventory[2] == 'Empty' or inventory[3] == 'Empty' or inventory[4] == 'Empty' or inventory[5] == 'Empty':
                    print()
                    print('You bought the Heart Relic.')
                    gold -= 40
                    
                    if inventory[0] == 'Empty':
                        inventory[0] = 'Heart Relic - Increases health'
                        
                    elif inventory[1] == 'Empty':
                        inventory[1] = 'Heart Relic - Increases health'
                        
                    elif inventory[2] == 'Empty':
                        inventory[2] = 'Heart Relic - Increases health'
                        
                    elif inventory[3] == 'Empty':
                        inventory[3] = 'Heart Relic - Increases health'
                        
                    elif inventory[4] == 'Empty':
                        inventory[4] = 'Heart Relic - Increases health'
                        
                    elif inventory[5] == 'Empty':
                        inventory[5] = 'Heart Relic - Increases health'
                        
                else:
                    print("You don't have enough iventory space.")
                
            elif gold <= 39:
                print()
                print('You do not have enough gold for this item.')

        elif niput == 'no':
            print('You came to your senses and decided that the prices were too high.')

        else:
            print(f'That is not a valid item')
                
            
    elif niput == 'stats' or niput == 'Stats' or niput == 'stats!' or niput == 'Stats!':
        print(f'Statistics:')
        print()
        print(f'Name: {name}.')
        print(f'Class: {pclass}.')
        print(f'Health: {hp}.')
        print(f'Max Health: {maxhp}.')
        print(f'Attack: {attk}.')
        print(f'Defense: {defense}.')
        print(f'Total enemies defeated: {totalwins}.')
        print(f'Total losses: {totallosses}.')
        print(f'Highest level reached: {highestlevel}.')
        print()
        print(f'Return to menu?')
        niput = input()

    elif niput == 'pets' and pets > 0 and experiments == 1 or niput == 'Pets' and pets > 0 and experiments == 1 or niput == 'pets!' and pets > 0 and experiments == 1 or niput == 'Pets!' and pets > 0 and experiments == 1:
        print(f'[This feature is in progress]')
        print(f"Slot 1: You have a pet {petname}! It's stats are: Health: {petstats.hp}, Attack: {petstats.atk}, {petstats.critdam * 100} Percent bonus for critical hits, {petstats.defe * 100} percent defense, and a 1 in {20 - critchance} chance to land a critical blow.")
        print(f'Pet equipped: Yes')
        print(f'Return to menu?')
        niput = input()

    elif niput == 'save game' or niput == 'Save game' or niput == 'Save Game' or niput == 'save Game' or niput == 'same game!' or niput == 'Save game!' or niput == 'save Game!' or niput == 'Save Game!':
        print(f'WARNING!! This feature does not save your pet statistics. Do you wish to continue? y/n')
        choice = input()
        played = True
              
        if choice == 'y' or choice == 'Y':
            
            if pets >= 1:
                hpstr = str(hp)
                maxhpstr = str(maxhp)
                attkstr = str(attk)
                critstr = str(crit)
                defensestr = str(defense)
                goldstr = str(gold)
                totalwinsstr = str(totalwins)
                totallossesstr = str(totallosses)
                highestlevelstr = str(highestlevel)
                petsstr = str(pets)
                experimentsstr = str(experiments)
                ##playedstr = str(played)

                ##petstatshpstr = str(petstats.hp)
                
                with open('SaveFileFistFight.txt', 'w') as f:
                    f.write(hpstr)
                    f.write('\n')
                    f.write(maxhpstr)
                    f.write('\n')
                    f.write(attkstr)
                    f.write('\n')
                    f.write(critstr)
                    f.write('\n')
                    f.write(defensestr)
                    f.write('\n')
                    f.write(pclass)
                    f.write('\n')
                    f.write(goldstr)
                    f.write('\n')
                    f.write(name)
                    f.write('\n')
                    f.write(totalwinsstr)
                    f.write('\n')
                    f.write(totallossesstr)
                    f.write('\n')
                    f.write(highestlevelstr)
                    f.write('\n')
                    f.write(petsstr)
                    f.write('\n')
                    f.write(petname)
                    f.write('\n')
                    f.write(experimentsstr)
                    f.write('\n')
                    f.write(inventory[0])
                    f.write('\n')
                    f.write(inventory[1])
                    f.write('\n')
                    f.write(inventory[2])
                    f.write('\n')
                    f.write(inventory[3])
                    f.write('\n')
                    f.write(inventory[4])
                    f.write('\n')
                    f.write(inventory[5])
                    f.write('\n')
                    f.write(inventory[6])
                    f.write('\n')
                    f.write(inventory[7])
                    f.close()
                    ##f.write('\n')
                    ##f.write(playedstr)
                    ##f.write('\n')
                    ##f.write(petstatshpstr)
                print(f"Your game has been saved in a folder as 'SaveFileFistFight.txt'. Please do not move, edit, or delete this file without also moving the source code file.")
                
            else:
                hpstr = str(hp)
                maxhpstr = str(maxhp)
                attkstr = str(attk)
                critstr = str(crit)
                defensestr = str(defense)
                goldstr = str(gold)
                totalwinsstr = str(totalwins)
                totallossesstr = str(totallosses)
                highestlevelstr = str(highestlevel)
                petsstr = str(pets)
                experimentsstr = str(experiments)
                ##playedstr = str(played)
                
                with open(f'SaveFileFistFight.txt', 'w') as f:
                    f.write(hpstr)
                    f.write('\n')
                    f.write(maxhpstr)
                    f.write('\n')
                    f.write(attkstr)
                    f.write('\n')
                    f.write(critstr)
                    f.write('\n')
                    f.write(defensestr)
                    f.write('\n')
                    f.write(pclass)
                    f.write('\n')
                    f.write(goldstr)
                    f.write('\n')
                    f.write(name)
                    f.write('\n')
                    f.write(totalwinsstr)
                    f.write('\n')
                    f.write(totallossesstr)
                    f.write('\n')
                    f.write(highestlevelstr)
                    f.write('\n')
                    f.write(petsstr)
                    f.write('\n')
                    f.write(experimentsstr)
                    f.write('\n')
                    f.write(inventory[0])
                    f.write('\n')
                    f.write(inventory[1])
                    f.write('\n')
                    f.write(inventory[2])
                    f.write('\n')
                    f.write(inventory[3])
                    f.write('\n')
                    f.write(inventory[4])
                    f.write('\n')
                    f.write(inventory[5])
                    f.write('\n')
                    f.write(inventory[6])
                    f.write('\n')
                    f.write(inventory[7])
                    f.close()
                    ##f.write('\n')
                    ##f.write(playedstr)
            print(f"Your game has been saved in a folder as 'SaveFileFistFight.txt'. Please do not move, edit, or delete this file without also moving the source code file.")
        
        else:
            print()
            print(f'You decided not to save your game. Booooo')

    elif niput == 'eitems' and experiments == 1:
        print('[THIS FEATURE IS IN PROGRESS AND IS NOT FULLY IMPLEMENTED YET]')
        print(f'Inventory:')
        print(f'Slot 1: {inventory[0]}')
        print(f'Slot 2: {inventory[1]}')
        print(f'Slot 3: {inventory[2]}')
        print(f'Slot 4: {inventory[3]}')
        print(f'Slot 5: {inventory[4]}')
        print(f'Slot 6: {inventory[5]}')
        print(f'Equipped Artifact 1: {inventory[6]}')
        print(f'Equipped Artifact 2: {inventory[7]}')
        print()
        print(f'What would you like to do? You can either equip an artifact (equip) or manage your inventory (manage).')
        niput = input()
              
        if niput == 'manage':
            print()
            print(f'You can do things. You can delete an item (delete) or move an item (move).')
            niput = input()
            print()
            
            if niput == 'delete':
                print("To delete an item, just type 'slot ', then the slot number. To not delete anything, type no.")
                niput = input()
                
                if niput == 'slot 1':
                    print('Are you sure? y/n')
                    niput = input()
                    
                    if niput == 'Y' or niput == 'y':
                        inventory[0] = 'Empty'
                        
                    else:
                        print("You didn't delete the item.")

                if niput == 'slot 2':
                    print('Are you sure? y/n')
                    niput = input()
                    
                    if niput == 'Y' or niput == 'y':
                        inventory[1] = 'Empty'
                        
                    else:
                        print("You didn't delete the item.")

                if niput == 'slot 3':
                    print('Are you sure? y/n')
                    niput = input()
                    
                    if niput == 'Y' or niput == 'y':
                        inventory[2] = 'Empty'
                        
                    else:
                        print("You didn't delete the item.")

                if niput == 'slot 4':
                    print('Are you sure? y/n')
                    niput = input()
                    
                    if niput == 'Y' or niput == 'y':
                        inventory[3] = 'Empty'
                        
                    else:
                        print("You didn't delete the item.")

                if niput == 'slot 5':
                    print('Are you sure? y/n')
                    niput = input()
                    
                    if niput == 'Y' or niput == 'y':
                        inventory[4] = 'Empty'
                        
                    else:
                        print("You didn't delete the item.")

                if niput == 'slot 6':
                    print('Are you sure? y/n')
                    niput = input()
                    
                    if niput == 'Y' or niput == 'y':
                        inventory[5] = 'Empty'
                        
                    else:
                        print("You didn't delete the item.")

                else:
                    print("That is not a viable slot")

            elif niput == 'move':
                print(f"Which item would you like to move? Format: 'slot ' numberOfSlot")
                niput = input()
                if niput == 'slot 1':
                    moveslot1 = inventory[0]
                    moveslotnum = 1
                    print('You chose slot 1.')

                elif niput == 'slot 2':
                    moveslot1 = inventory[1]
                    moveslotnum = 2
                    print('You chose slot 2.')

                elif niput == 'slot 3':
                    moveslot1 = inventory[2]
                    moveslotnum = 3
                    print('You chose slot 3.')

                elif niput == 'slot 4':
                    moveslot1 = inventory[3]
                    moveslotnum = 4
                    print('You chose slot 4.')

                elif niput == 'slot 5':
                    moveslot1 = inventory[4]
                    moveslotnum = 5
                    print('You chose slot 5.')

                elif niput == 'slot 6':
                    moveslot1 = inventory[5]
                    moveslotnum = 6
                    print('You chose slot 6.')

                else:
                    print('That is not a valid slot.')
                    moveslot1 = 'none'

                if moveslot != 'none':
                    print("Now choose which slot you want to swap it with. Format: 'slot ' numberOfSlot.")
                    niput = input()
                    
                    if niput == 'slot 1':
                        
                        if moveslotnum == 1:
                            inventory[0] = inventory[0]
                            inventory[0] = moveslot1
                            print('Slots successfully swapped!')
                            
                        if moveslotnum == 2:
                            inventory[1] = inventory[0]
                            inventory[0] = moveslot1
                            print('Slots successfully swapped!')
                            
                        if moveslotnum == 3:
                            inventory[2] = inventory[0]
                            inventory[0] = moveslot1
                            print('Slots successfully swapped!')
                            
                        if moveslotnum == 4:
                            inventory[3] = inventory[0]
                            inventory[0] = moveslot1
                            print('Slots successfully swapped!')

                        if moveslotnum == 5:
                            inventory[4] = inventory[0]
                            inventory[0] = moveslot1
                            print('Slots successfully swapped!')

                        if moveslotnum == 6:
                            inventory[5] = inventory[0]
                            inventory[0] = moveslot1
                            print('Slots successfully swapped!')

                    elif niput == 'slot 2':
                        
                        if moveslotnum == 1:
                            inventory[0] = inventory[1]
                            inventory[1] = moveslot1
                            print('Slots successfully swapped!')
                            
                        if moveslotnum == 2:
                            inventory[1] = inventory[1]
                            inventory[1] = moveslot1
                            print('Slots successfully swapped!')
                            
                        if moveslotnum == 3:
                            inventory[2] = inventory[1]
                            inventory[1] = moveslot1
                            print('Slots successfully swapped!')
                            
                        if moveslotnum == 4:
                            inventory[3] = inventory[1]
                            inventory[1] = moveslot1
                            print('Slots successfully swapped!')

                        if moveslotnum == 5:
                            inventory[4] = inventory[1]
                            inventory[1] = moveslot1
                            print('Slots successfully swapped!')

                        if moveslotnum == 6:
                            inventory[5] = inventory[1]
                            inventory[1] = moveslot1
                            print('Slots successfully swapped!')

                    elif niput == 'slot 3':
                        
                        if moveslotnum == 1:
                            inventory[0] = inventory[2]
                            inventory[2] = moveslot1
                            print('Slots successfully swapped!')
                            
                        if moveslotnum == 2:
                            inventory[1] = inventory[2]
                            inventory[2] = moveslot1
                            print('Slots successfully swapped!')
                            
                        if moveslotnum == 3:
                            inventory[2] = inventory[2]
                            inventory[2] = moveslot1
                            print('Slots successfully swapped!')
                            
                        if moveslotnum == 4:
                            inventory[3] = inventory[2]
                            inventory[2] = moveslot1
                            print('Slots successfully swapped!')

                        if moveslotnum == 5:
                            inventory[4] = inventory[2]
                            inventory[2] = moveslot1
                            print('Slots successfully swapped!')

                        if moveslotnum == 6:
                            inventory[5] = inventory[2]
                            inventory[2] = moveslot1
                            print('Slots successfully swapped!')

                    elif niput == 'slot 4':
                        
                        if moveslotnum == 1:
                            inventory[0] = inventory[3]
                            inventory[3] = moveslot1
                            print('Slots successfully swapped!')
                            
                        if moveslotnum == 2:
                            inventory[1] = inventory[3]
                            inventory[3] = moveslot1
                            print('Slots successfully swapped!')
                            
                        if moveslotnum == 3:
                            inventory[2] = inventory[3]
                            inventory[3] = moveslot1
                            print('Slots successfully swapped!')
                            
                        if moveslotnum == 4:
                            inventory[3] = inventory[3]
                            inventory[3] = moveslot1
                            print('Slots successfully swapped!')

                        if moveslotnum == 5:
                            inventory[4] = inventory[3]
                            inventory[3] = moveslot1
                            print('Slots successfully swapped!')

                        if moveslotnum == 6:
                            inventory[5] = inventory[3]
                            inventory[3] = moveslot1
                            print('Slots successfully swapped!')

                    elif niput == 'slot 5':
                        
                        if moveslotnum == 1:
                            inventory[0] = inventory[4]
                            inventory[4] = moveslot1
                            print('Slots successfully swapped!')
                            
                        if moveslotnum == 2:
                            inventory[1] = inventory[4]
                            inventory[4] = moveslot1
                            print('Slots successfully swapped!')
                            
                        if moveslotnum == 3:
                            inventory[2] = inventory[4]
                            inventory[4] = moveslot1
                            print('Slots successfully swapped!')
                            
                        if moveslotnum == 4:
                            inventory[3] = inventory[4]
                            inventory[4] = moveslot1
                            print('Slots successfully swapped!')

                        if moveslotnum == 5:
                            inventory[4] = inventory[4]
                            inventory[4] = moveslot1
                            print('Slots successfully swapped!')

                        if moveslotnum == 6:
                            inventory[5] = inventory[4]
                            inventory[4] = moveslot1
                            print('Slots successfully swapped!')

                    elif niput == 'slot 6':
                        
                        if moveslotnum == 1:
                            inventory[0] = inventory[5]
                            inventory[5] = moveslot1
                            print('Slots successfully swapped!')
                            
                        if moveslotnum == 2:
                            inventory[1] = inventory[5]
                            inventory[5] = moveslot1
                            print('Slots successfully swapped!')
                            
                        if moveslotnum == 3:
                            inventory[2] = inventory[5]
                            inventory[5] = moveslot1
                            print('Slots successfully swapped!')
                            
                        if moveslotnum == 4:
                            inventory[3] = inventory[5]
                            inventory[5] = moveslot1
                            print('Slots successfully swapped!')

                        if moveslotnum == 5:
                            inventory[4] = inventory[5]
                            inventory[5] = moveslot1
                            print('Slots successfully swapped!')

                        if moveslotnum == 6:
                            inventory[5] = inventory[5]
                            inventory[5] = moveslot1
                            print('Slots successfully swapped!')

                    else:
                        print('That is not a valid slot.')
        
        elif niput == 'equip':
            print("Please choose which item you want to equip, using the format: 'slot ' NumberOfSlot")
            niput = input()

            if niput == 'slot 1' and inventory[0] == 'Empty':
                print('That slot is empty.')

            elif niput == 'slot 2' and inventory[1] == 'Empty':
                print('That slot is empty.')    

            elif niput == 'slot 3' and inventory[2] == 'Empty':
                print('That slot is empty.')

            elif niput == 'slot 4' and inventory[3] == 'Empty':
                print('That slot is empty.')

            elif niput == 'slot 5' and inventory[4] == 'Empty':
                print('That slot is empty.')

            elif niput == 'slot 6' and inventory[5] == 'Empty':
                print('That slot is empty.')

            elif niput == 'slot 1' and inventory[0] != 'Empty':
                
                if inventory[6] == 'None':
                    print(f'You have activated your {inventory[0]}!')
                    inventory[6] = inventory[0]
                    inventory[0] = 'Empty'

                    if inventory[6] == 'Tooth Relic - Increases Critical hit damage':
                        crit += 0.1
                        buffs[3] += 0.1
                        
                    elif inventory[6] == 'Shield Relic - Increases defense':
                        defense += 0.07
                        buffs[1] += 0.07
                        
                    elif inventory[6] == 'Dagger - Increases damage':
                        attk += 3
                        buffs[2] += 3

                    elif inventory[6] == 'Heart Relic - Increases health':
                        maxhp += 3
                        buffs[5] += 3
                    
                elif inventory[7] == 'None':
                    print(f'You have activated your {inventory[0]}!')
                    inventory[6] = inventory[0]
                    inventory[0] = 'Empty'

                    if inventory[7] == 'Tooth Relic - Increases Critical hit damage':
                        crit += 0.1
                        buffs[3] += 0.1
                        
                    elif inventory[7] == 'Shield Relic - Increases defense':
                        defense += 0.07
                        buffs[1] += 0.07
                        
                    elif inventory[7] == 'Dagger - Increases damage':
                        attk += 3
                        buffs[2] += 3

                    elif inventory[7] == 'Heart Relic - Increases health':
                        maxhp += 3
                        buffs[5] += 3

                else:
                    print('You have already equipped the max amount of items.')

            elif niput == 'slot 2' and inventory[1] != 'Empty':

                if inventory[6] == 'None':
                    print(f'You have activated your {inventory[1]}!')
                    inventory[6] = inventory[1]
                    inventory[1] = 'Empty'

                    if inventory[6] == 'Tooth Relic - Increases Critical hit damage':
                        crit += 0.1
                        buffs[3] += 0.1
                        
                    elif inventory[6] == 'Shield Relic - Increases defense':
                        defense += 0.07
                        buffs[1] += 0.07
                        
                    elif inventory[6] == 'Dagger - Increases damage':
                        attk += 3
                        buffs[2] += 3

                    elif inventory[6] == 'Heart Relic - Increases health':
                        maxhp += 3
                        buffs[5] += 3
                    
                elif inventory[7] == 'None':
                    print(f'You have activated your {inventory[1]}!')
                    inventory[6] = inventory[1]
                    inventory[1] = 'Empty'

                    if inventory[7] == 'Tooth Relic - Increases Critical hit damage':
                        crit += 0.1
                        buffs[3] += 0.1
                        
                    elif inventory[7] == 'Shield Relic - Increases defense':
                        defense += 0.07
                        buffs[1] += 0.07
                        
                    elif inventory[7] == 'Dagger - Increases damage':
                        attk += 3
                        buffs[2] += 3

                    elif inventory[7] == 'Heart Relic - Increases health':
                        maxhp += 3
                        buffs[5] += 3

                else:
                    print('You have already equipped the max amount of items.')

            elif niput == 'slot 3' and inventory[2] != 'Empty':

                if inventory[6] == 'None':
                    print(f'You have activated your {inventory[2]}!')
                    inventory[6] = inventory[2]
                    inventory[2] = 'Empty'

                    if inventory[6] == 'Tooth Relic - Increases Critical hit damage':
                        crit += 0.1
                        buffs[3] += 0.1
                        
                    elif inventory[6] == 'Shield Relic - Increases defense':
                        defense += 0.07
                        buffs[1] += 0.07
                        
                    elif inventory[6] == 'Dagger - Increases damage':
                        attk += 3
                        buffs[2] += 3

                    elif inventory[6] == 'Heart Relic - Increases health':
                        maxhp += 3
                        buffs[5] += 3
                    
                elif inventory[7] == 'None':
                    print(f'You have activated your {inventory[2]}!')
                    inventory[6] = inventory[2]
                    inventory[2] = 'Empty'

                    if inventory[7] == 'Tooth Relic - Increases Critical hit damage':
                        crit += 0.1
                        buffs[3] += 0.1
                        
                    elif inventory[7] == 'Shield Relic - Increases defense':
                        defense += 0.07
                        buffs[1] += 0.07
                        
                    elif inventory[7] == 'Dagger - Increases damage':
                        attk += 3
                        buffs[2] += 3

                    elif inventory[7] == 'Heart Relic - Increases health':
                        maxhp += 3
                        buffs[5] += 3

                else:
                    print('You have already equipped the max amount of items.')

            elif niput == 'slot 4' and inventory[3] != 'Empty':

                if inventory[6] == 'None':
                    print(f'You have activated your {inventory[3]}!')
                    inventory[6] = inventory[3]
                    inventory[3] = 'Empty'

                    if inventory[6] == 'Tooth Relic - Increases Critical hit damage':
                        crit += 0.1
                        buffs[3] += 0.1
                        
                    elif inventory[6] == 'Shield Relic - Increases defense':
                        defense += 0.07
                        buffs[1] += 0.07
                        
                    elif inventory[6] == 'Dagger - Increases damage':
                        attk += 3
                        buffs[2] += 3

                    elif inventory[6] == 'Heart Relic - Increases health':
                        maxhp += 3
                        buffs[5] += 3
                        
                elif inventory[7] == 'None':
                    print(f'You have activated your {inventory[3]}!')
                    inventory[6] = inventory[3]
                    inventory[3] = 'Empty'

                    if inventory[7] == 'Tooth Relic - Increases Critical hit damage':
                        crit += 0.1
                        buffs[3] += 0.1
                        
                    elif inventory[7] == 'Shield Relic - Increases defense':
                        defense += 0.07
                        buffs[1] += 0.07
                        
                    elif inventory[7] == 'Dagger - Increases damage':
                        attk += 3
                        buffs[2] += 3

                    elif inventory[7] == 'Heart Relic - Increases health':
                        maxhp += 3
                        buffs[5] += 3

                else:
                    print('You have already equipped the max amount of items.')

            elif niput == 'slot 5' and inventory[4] != 'Empty':

                if inventory[6] == 'None':
                    print(f'You have activated your {inventory[4]}!')
                    inventory[6] = inventory[4]
                    inventory[4] = 'Empty'

                    if inventory[6] == 'Tooth Relic - Increases Critical hit damage':
                        crit += 0.1
                        buffs[3] += 0.1
                        
                    elif inventory[6] == 'Shield Relic - Increases defense':
                        defense += 0.07
                        buffs[1] += 0.07
                        
                    elif inventory[6] == 'Dagger - Increases damage':
                        attk += 3
                        buffs[2] += 3

                    elif inventory[6] == 'Heart Relic - Increases health':
                        maxhp += 3
                        buffs[5] += 3
                    
                elif inventory[7] == 'None':
                    print(f'You have activated your {inventory[4]}!')
                    inventory[6] = inventory[4]
                    inventory[4] = 'Empty'

                    if inventory[7] == 'Tooth Relic - Increases Critical hit damage':
                        crit += 0.1
                        buffs[3] += 0.1
                        
                    elif inventory[7] == 'Shield Relic - Increases defense':
                        defense += 0.07
                        buffs[1] += 0.07
                        
                    elif inventory[7] == 'Dagger - Increases damage':
                        attk += 3
                        buffs[2] += 3

                    elif inventory[7] == 'Heart Relic - Increases health':
                        maxhp += 3
                        buffs[5] += 3

                else:
                    print('You have already equipped the max amount of items.')

            elif niput == 'slot 6' and inventory[5] != 'Empty':

                if inventory[6] == 'None':
                    print(f'You have activated your {inventory[5]}!')
                    inventory[6] = inventory[5]
                    inventory[5] = 'Empty'

                    if inventory[6] == 'Tooth Relic - Increases Critical hit damage':
                        crit += 0.1
                        buffs[3] += 0.1
                        
                    elif inventory[6] == 'Shield Relic - Increases defense':
                        defense += 0.07
                        buffs[1] += 0.07
                        
                    elif inventory[6] == 'Dagger - Increases damage':
                        attk += 3
                        buffs[2] += 3

                    elif inventory[6] == 'Heart Relic - Increases health':
                        maxhp += 3
                        buffs[5] += 3
                    
                elif inventory[7] == 'None':
                    print(f'You have activated your {inventory[5]}!')
                    inventory[6] = inventory[5]
                    inventory[5] = 'Empty'

                    if inventory[7] == 'Tooth Relic - Increases Critical hit damage':
                        crit += 0.1
                        buffs[3] += 0.1
                        
                    elif inventory[7] == 'Shield Relic - Increases defense':
                        defense += 0.07
                        buffs[1] += 0.07
                        
                    elif inventory[7] == 'Dagger - Increases damage':
                        attk += 3
                        buffs[2] += 3

                    elif inventory[7] == 'Heart Relic - Increases health':
                        maxhp += 3
                        buffs[5] += 3

                else:
                    print('You have already equipped the max amount of items.')

            else:
                print('That is not a valid slot.')

    elif niput == 'qgame':
        print()
        print("You quit the game. A backup has been made.")
        
        if pets >= 1:
            hpstr = str(hp)
            maxhpstr = str(maxhp)
            attkstr = str(attk)
            critstr = str(crit)
            defensestr = str(defense)
            goldstr = str(gold)
            totalwinsstr = str(totalwins)
            totallossesstr = str(totallosses)
            highestlevelstr = str(highestlevel)
            petsstr = str(pets)
            experimentsstr = str(experiments)
            
            with open('SaveFileFistFight.txt', 'w') as f:
                f.write(hpstr)
                f.write('\n')
                f.write(maxhpstr)
                f.write('\n')
                f.write(attkstr)
                f.write('\n')
                f.write(critstr)
                f.write('\n')
                f.write(defensestr)
                f.write('\n')
                f.write(pclass)
                f.write('\n')
                f.write(goldstr)
                f.write('\n')
                f.write(name)
                f.write('\n')
                f.write(totalwinsstr)
                f.write('\n')
                f.write(totallossesstr)
                f.write('\n')
                f.write(highestlevelstr)
                f.write('\n')
                f.write(petsstr)
                f.write('\n')
                f.write(petname)
                f.write('\n')
                f.write(experimentsstr)
                f.write('\n')
                f.write(inventory[0])
                f.write('\n')
                f.write(inventory[1])
                f.write('\n')
                f.write(inventory[2])
                f.write('\n')
                f.write(inventory[3])
                f.write('\n')
                f.write(inventory[4])
                f.write('\n')
                f.write(inventory[5])
                f.write('\n')
                f.write(inventory[6])
                f.write('\n')
                f.write(inventory[7])
                f.close()
            print(f"Your game has been saved in a folder as 'SaveFileFistFight.txt'. Please do not move, edit, or delete this file without also moving the source code file.")
            
        else:
            hpstr = str(hp)
            maxhpstr = str(maxhp)
            attkstr = str(attk)
            critstr = str(crit)
            defensestr = str(defense)
            goldstr = str(gold)
            totalwinsstr = str(totalwins)
            totallossesstr = str(totallosses)
            highestlevelstr = str(highestlevel)
            petsstr = str(pets)
            experimentsstr = str(experiments)
            
            with open(f'SaveFileFistFight.txt', 'w') as f:
                f.write(hpstr)
                f.write('\n')
                f.write(maxhpstr)
                f.write('\n')
                f.write(attkstr)
                f.write('\n')
                f.write(critstr)
                f.write('\n')
                f.write(defensestr)
                f.write('\n')
                f.write(pclass)
                f.write('\n')
                f.write(goldstr)
                f.write('\n')
                f.write(name)
                f.write('\n')
                f.write(totalwinsstr)
                f.write('\n')
                f.write(totallossesstr)
                f.write('\n')
                f.write(highestlevelstr)
                f.write('\n')
                f.write(petsstr)
                f.write('\n')
                f.write(experimentsstr)
                f.write('\n')
                f.write(inventory[0])
                f.write('\n')
                f.write(inventory[1])
                f.write('\n')
                f.write(inventory[2])
                f.write('\n')
                f.write(inventory[3])
                f.write('\n')
                f.write(inventory[4])
                f.write('\n')
                f.write(inventory[5])
                f.write('\n')
                f.write(inventory[6])
                f.write('\n')
                f.write(inventory[7])
                f.close()
        print(f"Your game has been saved in a folder as 'SaveFileFistFight.txt'. Please do not move, edit, or delete this file without also moving the source code file.")

        loop = False
        loop1 = False
        loop2 = False
        gameloop = False
        time.sleep(2)
        print()
        print(f'Credits:')
        print()
        time.sleep(2)
        print(f'Creator & Programmer: Joey Bacon, Docter of Computer Science & Programming')
        time.sleep(2)
        print(f'Engine: IDLE Python Shell 3.11.4/3.11.5')
        time.sleep(2)
        print(f'Game version: {version}.')
        time.sleep(3)
        print(f"And finally...")
        time.sleep(4)
        print(f'Playtesters: Eli Cardoso, Soar Mutl, Molly Bacon, Mateo Donado, Noah Magone, ')
        time.sleep(3)
        
    else:
        print(f'That is not a valid action.')
        
print()
print()
print()
print("Process exited. No errors detected with save file.")
