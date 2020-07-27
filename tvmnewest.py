import random
import time
import os


# Welcome screen

print('\n\n           ============= Welcome to TANK MASTERS =============')
print('\n\n              ============= created by commRat =============')
print('\n\n                    ============= 2020 =============')


# Screen stays for 3 secs, then disappear

time.sleep(3)
cls = lambda: os.system('cls')
cls()


# Name in battle, HP, lowest dmg, highest dmg

# M1A2C Abrams 
abrams_bn = 'Abrams'
abrams_hp = 3000
abrams_min = 100
abrams_max = 200

# T-14, Armata 
armata_bn = 'Armata'
armata_hp = 2000
armata_min = 150
armata_max = 350

# 2S25 Sprut-SD
sprut_bn = 'Sprut'
sprut_hp = 1500
sprut_min = 200
sprut_max = 450

# K2 Black Panther
panther_bn = 'Black Panther'
panther_hp = 3500
panther_min = 50
panther_max = 150

# Type 15
typ_bn = 'Type 15'
typ_hp = 2500
typ_min = 120
typ_max = 300

# MYSTERY TANK 
mystery_bn = 'Mystery tank'
mystery_hp = random.randint(1000, 3500)
mystery_min = random.randint(1, 200)
mystery_max = random.randint(220, 450)


# Define function, set x_dmg_done to zero, which will increase with every randomly
# generated shoot, when HP are lower or equal to 0, loop breaks

def fight(player_bn, player_hp, player_max, player_min, 
          villain_bn, villain_hp, villain_max, villain_min):
    player_dmg_done = 0
    villain_dmg_done = 0
    print()
    while player_hp >= villain_dmg_done or villain_hp >= player_dmg_done:
        x = random.randint(1, 10)
        if x < 8:
            player_shoot = random.randint(player_min, player_max)
            player_dmg_done += player_shoot
            time.sleep(2)
            print(player_bn + ' shooted: ' + str(player_shoot) + ' dmg to ' + villain_bn)
            left = -(player_dmg_done - villain_hp)
            print('HP left: ' + str(left) + ' from ' + str(villain_hp))
            print()
            if player_dmg_done > villain_hp:
                print('YOU WON! ' + player_bn + ' survived.')
                print('Meanwhile ' + villain_bn + ' is destroyed.')
                break
            
        elif x >= 8:
            player_shoot = random.randint(player_min*2, player_max*2)
            player_dmg_done += player_shoot
            time.sleep(2)
            print(player_bn + ' shooted: ' + str(player_shoot) + ' CRITICAL dmg to ' + villain_bn)
            left = -(player_dmg_done - villain_hp)
            print('HP left: ' + str(left) + ' from ' + str(villain_hp))
            print()
            if player_dmg_done > villain_hp:
                print('YOU WON! ' + player_bn + ' survived.')
                print('Meanwhile ' + villain_bn + ' is destroyed.')
                break
        
        y = random.randint(1, 10)
        if y < 8:
            villain_shoot = random.randint(villain_min, villain_max)
            villain_dmg_done += villain_shoot
            time.sleep(2)
            print(villain_bn + ' shooted: ' + str(villain_shoot) + ' dmg to ' + player_bn)
            left = -(villain_dmg_done - player_hp)
            print('HP left: ' + str(left) + ' from ' + str(player_hp))
            print()
            if villain_dmg_done > player_hp:
                print('YOU LOST... ' + villain_bn + ' survived.')
                print('Meanwhile ' + player_bn + ' is destroyed.')
                break
            
        elif y >= 8:
            villain_shoot = random.randint(villain_min*2, villain_max*2)
            villain_dmg_done += villain_shoot
            time.sleep(2)
            print(villain_bn + ' shooted: ' + str(villain_shoot) + ' CRITICAL dmg to ' + player_bn)
            left = -(villain_dmg_done - player_hp)
            print('HP left: ' + str(left) + ' from ' + str(player_hp))
            print()
            if villain_dmg_done > player_hp:
                print('YOU LOST... ' + villain_bn + ' survived.')
                print('Meanwhile ' + player_bn + ' is destroyed.')
                break



# Program ask the user to pick his own tank and enemy tank

read_p = open('Player_tank.txt', 'r').read()
print(read_p)
player = input('')
cls()
read_e = open('Enemy_tank.txt', 'r').read()
print(read_e)
villain = input('')
cls()



# We have to rename parameters, so we can use them in function properly

if player == str(1) and villain == str(1):
    player_bn = abrams_bn
    player_hp = abrams_hp
    player_min = abrams_min
    player_max = abrams_max

    villain_bn = abrams_bn
    villain_hp = abrams_hp
    villain_min = abrams_min
    villain_max = abrams_max
    
elif player == str(1) and villain == str(2):
    player_bn = abrams_bn
    player_hp = abrams_hp
    player_min = abrams_min
    player_max = abrams_max

    villain_bn = armata_bn
    villain_hp = armata_hp
    villain_min = armata_min
    villain_max = armata_max
    
elif player == str(1) and villain == str(3):
    player_bn = abrams_bn
    player_hp = abrams_hp
    player_min = abrams_min
    player_max = abrams_max

    villain_bn = sprut_bn
    villain_hp = sprut_hp
    villain_min = sprut_min
    villain_max = sprut_max
    
elif player == str(1) and villain == str(4):
    player_bn = abrams_bn
    player_hp = abrams_hp
    player_min = abrams_min
    player_max = abrams_max

    villain_bn = panther_bn
    villain_hp = panther_hp
    villain_min = panther_min
    villain_max = panther_max  
    
elif player == str(1) and villain == str(5):
    player_bn = abrams_bn
    player_hp = abrams_hp
    player_min = abrams_min
    player_max = abrams_max

    villain_bn = typ_bn
    villain_hp = typ_hp
    villain_min = typ_min
    villain_max = typ_max  
    
elif player == str(1) and villain == str(6):
    player_bn = abrams_bn
    player_hp = abrams_hp
    player_min = abrams_min
    player_max = abrams_max

    villain_bn = mystery_bn
    villain_hp = mystery_hp
    villain_min = mystery_min
    villain_max = mystery_max
    
elif player == str(2) and villain == str(1):
    player_bn = armata_bn
    player_hp = armata_hp
    player_min = armata_min
    player_max = armata_max

    villain_bn = abrams_bn
    villain_hp = abrams_hp
    villain_min = abrams_min
    villain_max = abrams_max
    
elif player == str(2) and villain == str(2):
    player_bn = armata_bn
    player_hp = armata_hp
    player_min = armata_min
    player_max = armata_max

    villain_bn = armata_bn
    villain_hp = armata_hp
    villain_min = armata_min
    villain_max = armata_max
    
elif player == str(2) and villain == str(3):
    player_bn = armata_bn
    player_hp = armata_hp
    player_min = armata_min
    player_max = armata_max

    villain_bn = sprut_bn
    villain_hp = sprut_hp
    villain_min = sprut_min
    villain_max = sprut_max

elif player == str(2) and villain == str(4):
    player_bn = armata_bn
    player_hp = armata_hp
    player_min = armata_min
    player_max = armata_max

    villain_bn = panther_bn
    villain_hp = panther_hp
    villain_min = panther_min
    villain_max = panther_max 

elif player == str(2) and villain == str(5):
    player_bn = armata_bn
    player_hp = armata_hp
    player_min = armata_min
    player_max = armata_max

    villain_bn = typ_bn
    villain_hp = typ_hp
    villain_min = typ_min
    villain_max = typ_max
    
elif player == str(2) and villain == str(6):
    player_bn = armata_bn
    player_hp = armata_hp
    player_min = armata_min
    player_max = armata_max

    villain_bn = mystery_bn
    villain_hp = mystery_hp
    villain_min = mystery_min
    villain_max = mystery_max
    
elif player == str(3) and villain == str(1):
    player_bn = sprut_bn
    player_hp = sprut_hp
    player_min = sprut_min
    player_max = sprut_max

    villain_bn = abrams_bn
    villain_hp = abrams_hp
    villain_min = abrams_min
    villain_max = abrams_max

elif player == str(3) and villain == str(2):
    player_bn = sprut_bn
    player_hp = sprut_hp
    player_min = sprut_min
    player_max = sprut_max

    villain_bn = armata_bn
    villain_hp = armata_hp
    villain_min = armata_min
    villain_max = armata_max
    
elif player == str(3) and villain == str(3):
    player_bn = sprut_bn
    player_hp = sprut_hp
    player_min = sprut_min
    player_max = sprut_max

    villain_bn = sprut_bn
    villain_hp = sprut_hp
    villain_min = sprut_min
    villain_max = sprut_max
    
elif player == str(3) and villain == str(4):
    player_bn = sprut_bn
    player_hp = sprut_hp
    player_min = sprut_min
    player_max = sprut_max

    villain_bn = panther_bn
    villain_hp = panther_hp
    villain_min = panther_min
    villain_max = panther_max 

elif player == str(3) and villain == str(5):
    player_bn = sprut_bn
    player_hp = sprut_hp
    player_min = sprut_min
    player_max = sprut_max

    villain_bn = typ_bn
    villain_hp = typ_hp
    villain_min = typ_min
    villain_max = typ_max

elif player == str(3) and villain == str(6):
    player_bn = sprut_bn
    player_hp = sprut_hp
    player_min = sprut_min
    player_max = sprut_max

    villain_bn = mystery_bn
    villain_hp = mystery_hp
    villain_min = mystery_min
    villain_max = mystery_max
    
elif player == str(4) and villain == str(1):
    player_bn = panther_bn
    player_hp = panther_hp
    player_min = panther_min
    player_max = panther_max

    villain_bn = abrams_bn
    villain_hp = abrams_hp
    villain_min = abrams_min
    villain_max = abrams_max
    
elif player == str(4) and villain == str(2):
    player_bn = panther_bn
    player_hp = panther_hp
    player_min = panther_min
    player_max = panther_max

    villain_bn = armata_bn
    villain_hp = armata_hp
    villain_min = armata_min
    villain_max = armata_max
    
elif player == str(4) and villain == str(3):
    player_bn = panther_bn
    player_hp = panther_hp
    player_min = panther_min
    player_max = panther_max

    villain_bn = sprut_bn
    villain_hp = sprut_hp
    villain_min = sprut_min
    villain_max = sprut_max
    
elif player == str(4) and villain == str(4):
    player_bn = panther_bn
    player_hp = panther_hp
    player_min = panther_min
    player_max = panther_max

    villain_bn = panther_bn
    villain_hp = panther_hp
    villain_min = panther_min
    villain_max = panther_max 
    
elif player == str(4) and villain == str(5):
    player_bn = panther_bn
    player_hp = panther_hp
    player_min = panther_min
    player_max = panther_max

    villain_bn = typ_bn
    villain_hp = typ_hp
    villain_min = typ_min
    villain_max = typ_max
    
elif player == str(4) and villain == str(6):
    player_bn = panther_bn
    player_hp = panther_hp
    player_min = panther_min
    player_max = panther_max

    villain_bn = mystery_bn
    villain_hp = mystery_hp
    villain_min = mystery_min
    villain_max = mystery_max
    
elif player == str(5) and villain == str(1):
    player_bn = typ_bn
    player_hp = typ_hp
    player_min = typ_min
    player_max = typ_max

    villain_bn = abrams_bn
    villain_hp = abrams_hp
    villain_min = abrams_min
    villain_max = abrams_max
    
elif player == str(5) and villain == str(2):
    player_bn = typ_bn
    player_hp = typ_hp
    player_min = typ_min
    player_max = typ_max

    villain_bn = armata_bn
    villain_hp = armata_hp
    villain_min = armata_min
    villain_max = armata_max

elif player == str(5) and villain == str(3):
    player_bn = typ_bn
    player_hp = typ_hp
    player_min = typ_min
    player_max = typ_max

    villain_bn = sprut_bn
    villain_hp = sprut_hp
    villain_min = sprut_min
    villain_max = sprut_max

elif player == str(5) and villain == str(4):
    player_bn = typ_bn
    player_hp = typ_hp
    player_min = typ_min
    player_max = typ_max

    villain_bn = panther_bn
    villain_hp = panther_hp
    villain_min = panther_min
    villain_max = panther_max 

elif player == str(5) and villain == str(5):
    player_bn = typ_bn
    player_hp = typ_hp
    player_min = typ_min
    player_max = typ_max

    villain_bn = typ_bn
    villain_hp = typ_hp
    villain_min = typ_min
    villain_max = typ_max

elif player == str(5) and villain == str(6):
    player_bn = typ_bn
    player_hp = typ_hp
    player_min = typ_min
    player_max = typ_max

    villain_bn = mystery_bn
    villain_hp = mystery_hp
    villain_min = mystery_min
    villain_max = mystery_max

elif player == str(6) and villain == str(1):
    player_bn = mystery_bn
    player_hp = mystery_hp
    player_min = mystery_min
    player_max = mystery_max

    villain_bn = abrams_bn
    villain_hp = abrams_hp
    villain_min = abrams_min
    villain_max = abrams_max

elif player == str(6) and villain == str(2):
    player_bn = mystery_bn
    player_hp = mystery_hp
    player_min = mystery_min
    player_max = mystery_max

    villain_bn = armata_bn
    villain_hp = armata_hp
    villain_min = armata_min
    villain_max = armata_max

elif player == str(6) and villain == str(3):
    player_bn = mystery_bn
    player_hp = mystery_hp
    player_min = mystery_min
    player_max = mystery_max

    villain_bn = sprut_bn
    villain_hp = sprut_hp
    villain_min = sprut_min
    villain_max = sprut_max

elif player == str(6) and villain == str(4):
    player_bn = mystery_bn
    player_hp = mystery_hp
    player_min = mystery_min
    player_max = mystery_max

    villain_bn = panther_bn
    villain_hp = panther_hp
    villain_min = panther_min
    villain_max = panther_max 

elif player == str(6) and villain == str(5):
    player_bn = mystery_bn
    player_hp = mystery_hp
    player_min = mystery_min
    player_max = mystery_max

    villain_bn = typ_bn
    villain_hp = typ_hp
    villain_min = typ_min
    villain_max = typ_max

# We have to redefine enemy mystery tank, so it can generate new stats
    
elif player == str(6) and villain == str(6):
    player_bn = mystery_bn
    player_hp = mystery_hp
    player_min = mystery_min
    player_max = mystery_max

    villain_bn = mystery_bn
    villain_hp = random.randint(1000, 3500)
    villain_min = random.randint(1, 200)
    villain_max = mystery_max = random.randint(220, 450)

else:
    print('You have to make a choice between 1 and 6 to pick a tank.')
    input('Press ENTER to quit app. Next time pick right numbers.')
    cls()
    print('\n\n       =============Thanks for playing!=============')
    print('\n\n       ============= See you next time =============')
    time.sleep(3)



# Call the fight() method with reassigned variables

fight(player_bn, player_hp, player_max, player_min, villain_bn, villain_hp, villain_max, villain_min)

finish = False

while finish is False:
    end = input('Do you wish to continue? (Y) for continue, (N) for exit.')
    if end.lower() == 'n':
        break
   
    else:
        read_p = open('Player_tank.txt', 'r').read()
        print(read_p)
        player = input('')
        cls()
        read_e = open('Enemy_tank.txt', 'r').read()
        print(read_e)
        villain = input('')
        cls()
        
        if player == str(1) and villain == str(1):
            player_bn = abrams_bn
            player_hp = abrams_hp
            player_min = abrams_min
            player_max = abrams_max

            villain_bn = abrams_bn
            villain_hp = abrams_hp
            villain_min = abrams_min
            villain_max = abrams_max
    
        elif player == str(1) and villain == str(2):
            player_bn = abrams_bn
            player_hp = abrams_hp
            player_min = abrams_min
            player_max = abrams_max

            villain_bn = armata_bn
            villain_hp = armata_hp
            villain_min = armata_min
            villain_max = armata_max
    
        elif player == str(1) and villain == str(3):
            player_bn = abrams_bn
            player_hp = abrams_hp
            player_min = abrams_min
            player_max = abrams_max

            villain_bn = sprut_bn
            villain_hp = sprut_hp
            villain_min = sprut_min
            villain_max = sprut_max
    
        elif player == str(1) and villain == str(4):
            player_bn = abrams_bn
            player_hp = abrams_hp
            player_min = abrams_min
            player_max = abrams_max

            villain_bn = panther_bn
            villain_hp = panther_hp
            villain_min = panther_min
            villain_max = panther_max  
    
        elif player == str(1) and villain == str(5):
            player_bn = abrams_bn
            player_hp = abrams_hp
            player_min = abrams_min
            player_max = abrams_max

            villain_bn = typ_bn
            villain_hp = typ_hp
            villain_min = typ_min
            villain_max = typ_max  
    
        elif player == str(1) and villain == str(6):
            player_bn = abrams_bn
            player_hp = abrams_hp
            player_min = abrams_min
            player_max = abrams_max

            villain_bn = mystery_bn
            villain_hp = mystery_hp
            villain_min = mystery_min
            villain_max = mystery_max
    
        elif player == str(2) and villain == str(1):
            player_bn = armata_bn
            player_hp = armata_hp
            player_min = armata_min
            player_max = armata_max

            villain_bn = abrams_bn
            villain_hp = abrams_hp
            villain_min = abrams_min
            villain_max = abrams_max
    
        elif player == str(2) and villain == str(2):
            player_bn = armata_bn
            player_hp = armata_hp
            player_min = armata_min
            player_max = armata_max

            villain_bn = armata_bn
            villain_hp = armata_hp
            villain_min = armata_min
            villain_max = armata_max
    
        elif player == str(2) and villain == str(3):
            player_bn = armata_bn
            player_hp = armata_hp
            player_min = armata_min
            player_max = armata_max

            villain_bn = sprut_bn
            villain_hp = sprut_hp
            villain_min = sprut_min
            villain_max = sprut_max

        elif player == str(2) and villain == str(4):
            player_bn = armata_bn
            player_hp = armata_hp
            player_min = armata_min
            player_max = armata_max

            villain_bn = panther_bn
            villain_hp = panther_hp
            villain_min = panther_min
            villain_max = panther_max 

        elif player == str(2) and villain == str(5):
            player_bn = armata_bn
            player_hp = armata_hp
            player_min = armata_min
            player_max = armata_max

            villain_bn = typ_bn
            villain_hp = typ_hp
            villain_min = typ_min
            villain_max = typ_max
    
        elif player == str(2) and villain == str(6):
            player_bn = armata_bn
            player_hp = armata_hp
            player_min = armata_min
            player_max = armata_max

            villain_bn = mystery_bn
            villain_hp = mystery_hp
            villain_min = mystery_min
            villain_max = mystery_max
    
        elif player == str(3) and villain == str(1):
            player_bn = sprut_bn
            player_hp = sprut_hp
            player_min = sprut_min
            player_max = sprut_max

            villain_bn = abrams_bn
            villain_hp = abrams_hp
            villain_min = abrams_min
            villain_max = abrams_max

        elif player == str(3) and villain == str(2):
            player_bn = sprut_bn
            player_hp = sprut_hp
            player_min = sprut_min
            player_max = sprut_max

            villain_bn = armata_bn
            villain_hp = armata_hp
            villain_min = armata_min
            villain_max = armata_max
    
        elif player == str(3) and villain == str(3):
            player_bn = sprut_bn
            player_hp = sprut_hp
            player_min = sprut_min
            player_max = sprut_max
        
            villain_bn = sprut_bn
            villain_hp = sprut_hp
            villain_min = sprut_min
            villain_max = sprut_max
    
        elif player == str(3) and villain == str(4):
            player_bn = sprut_bn
            player_hp = sprut_hp
            player_min = sprut_min
            player_max = sprut_max

            villain_bn = panther_bn
            villain_hp = panther_hp
            villain_min = panther_min
            villain_max = panther_max 

        elif player == str(3) and villain == str(5):
            player_bn = sprut_bn
            player_hp = sprut_hp
            player_min = sprut_min
            player_max = sprut_max
    
            villain_bn = typ_bn
            villain_hp = typ_hp
            villain_min = typ_min
            villain_max = typ_max

        elif player == str(3) and villain == str(6):
            player_bn = sprut_bn
            player_hp = sprut_hp
            player_min = sprut_min
            player_max = sprut_max

            villain_bn = mystery_bn
            villain_hp = mystery_hp
            villain_min = mystery_min
            villain_max = mystery_max
    
        elif player == str(4) and villain == str(1):
            player_bn = panther_bn
            player_hp = panther_hp
            player_min = panther_min
            player_max = panther_max

            villain_bn = abrams_bn
            villain_hp = abrams_hp
            villain_min = abrams_min
            villain_max = abrams_max
    
        elif player == str(4) and villain == str(2):
            player_bn = panther_bn
            player_hp = panther_hp
            player_min = panther_min
            player_max = panther_max

            villain_bn = armata_bn
            villain_hp = armata_hp
            villain_min = armata_min
            villain_max = armata_max
    
        elif player == str(4) and villain == str(3):
            player_bn = panther_bn
            player_hp = panther_hp
            player_min = panther_min
            player_max = panther_max

            villain_bn = sprut_bn
            villain_hp = sprut_hp
            villain_min = sprut_min
            villain_max = sprut_max
    
        elif player == str(4) and villain == str(4):
            player_bn = panther_bn
            player_hp = panther_hp
            player_min = panther_min
            player_max = panther_max

            villain_bn = panther_bn
            villain_hp = panther_hp
            villain_min = panther_min
            villain_max = panther_max 
    
        elif player == str(4) and villain == str(5):
            player_bn = panther_bn
            player_hp = panther_hp
            player_min = panther_min
            player_max = panther_max

            villain_bn = typ_bn
            villain_hp = typ_hp
            villain_min = typ_min
            villain_max = typ_max
    
        elif player == str(4) and villain == str(6):
            player_bn = panther_bn
            player_hp = panther_hp
            player_min = panther_min
            player_max = panther_max

            villain_bn = mystery_bn
            villain_hp = mystery_hp
            villain_min = mystery_min
            villain_max = mystery_max
    
        elif player == str(5) and villain == str(1):
            player_bn = typ_bn
            player_hp = typ_hp
            player_min = typ_min
            player_max = typ_max

            villain_bn = abrams_bn
            villain_hp = abrams_hp
            villain_min = abrams_min
            villain_max = abrams_max
    
        elif player == str(5) and villain == str(2):
            player_bn = typ_bn
            player_hp = typ_hp
            player_min = typ_min
            player_max = typ_max

            villain_bn = armata_bn
            villain_hp = armata_hp
            villain_min = armata_min
            villain_max = armata_max

        elif player == str(5) and villain == str(3):
            player_bn = typ_bn
            player_hp = typ_hp
            player_min = typ_min
            player_max = typ_max

            villain_bn = sprut_bn
            villain_hp = sprut_hp
            villain_min = sprut_min
            villain_max = sprut_max

        elif player == str(5) and villain == str(4):
            player_bn = typ_bn
            player_hp = typ_hp
            player_min = typ_min
            player_max = typ_max
        
            villain_bn = panther_bn
            villain_hp = panther_hp
            villain_min = panther_min
            villain_max = panther_max 

        elif player == str(5) and villain == str(5):
            player_bn = typ_bn
            player_hp = typ_hp
            player_min = typ_min
            player_max = typ_max
    
            villain_bn = typ_bn
            villain_hp = typ_hp
            villain_min = typ_min
            villain_max = typ_max

        elif player == str(5) and villain == str(6):
            player_bn = typ_bn
            player_hp = typ_hp
            player_min = typ_min
            player_max = typ_max

            villain_bn = mystery_bn
            villain_hp = mystery_hp
            villain_min = mystery_min
            villain_max = mystery_max

        elif player == str(6) and villain == str(1):
            player_bn = mystery_bn
            player_hp = mystery_hp
            player_min = mystery_min
            player_max = mystery_max

            villain_bn = abrams_bn
            villain_hp = abrams_hp
            villain_min = abrams_min
            villain_max = abrams_max

        elif player == str(6) and villain == str(2):
            player_bn = mystery_bn
            player_hp = mystery_hp
            player_min = mystery_min
            player_max = mystery_max

            villain_bn = armata_bn
            villain_hp = armata_hp
            villain_min = armata_min
            villain_max = armata_max

        elif player == str(6) and villain == str(3):
            player_bn = mystery_bn
            player_hp = mystery_hp
            player_min = mystery_min
            player_max = mystery_max

            villain_bn = sprut_bn
            villain_hp = sprut_hp
            villain_min = sprut_min
            villain_max = sprut_max

        elif player == str(6) and villain == str(4):
            player_bn = mystery_bn
            player_hp = mystery_hp
            player_min = mystery_min
            player_max = mystery_max

            villain_bn = panther_bn
            villain_hp = panther_hp
            villain_min = panther_min
            villain_max = panther_max 

        elif player == str(6) and villain == str(5):
            player_bn = mystery_bn
            player_hp = mystery_hp
            player_min = mystery_min
            player_max = mystery_max

            villain_bn = typ_bn
            villain_hp = typ_hp
            villain_min = typ_min
            villain_max = typ_max

    
        elif player == str(6) and villain == str(6):
            player_bn = mystery_bn
            player_hp = mystery_hp
            player_min = mystery_min
            player_max = mystery_max

            villain_bn = mystery_bn
            villain_hp = random.randint(1000, 3500)
            villain_min = random.randint(1, 200)
            villain_max = mystery_max = random.randint(220, 450)
            
        else:
            print('You have to make a choice between 1 and 6 to pick a tank.')
            break
    
    fight(player_bn, player_hp, player_max, player_min, villain_bn, villain_hp, villain_max, villain_min)


    

# Program ends after 3 secs

cls()

print('\n\n       =============Thanks for playing!=============')
print('\n\n       ============= See you next time =============')
time.sleep(3)
