import os
import numpy as np
import math
import functions as f


#Initialize menu variables
hero = 'nobody'
enemy = 'still nobody'
match_result = 'nothing happened'
result_mag = 'gg ez'
skill_level = 'git gud'
user_input = ' '
program_check = 'pgc'
menu_check = 'mnc'

# List of playable heroes
hero_list = ["Overall", "Warden", "Conqueror", "Peacekeeper", "Lawbringer", "Centurion", "Gladiator", "Vortiger", 
                 "Raider", "Warlord", "Berserker", "Valkyrie", "Highlander", "Shaman", "Jormungandr", 
                 "Kensei", "Shugoki", "Orochi", "Nobushi", "Shinobi", "Aramusha", "Hitokiri", "Tiandi", "Jiang Jun", 
                 "Nuxia", "Shaolin", "Zhanhu"]

#Initialize arrays for hero statistics (and put them in a list)
overall_data = np.zeros((1, 20))
warden_data = conq_data = pk_data = law_data = cent_data = glad_data = bp_data = np.zeros((26, 20))
raider_data = warlord_data = zerk_data = valk_data = high_data = shaman_data = jorm_data = np.zeros((26,20))
kensei_data = goki_data = roach_data = nobu_data = shinobi_data = musha_data = hito_data = np.zeros((26,20))
tiandi_data = jun_data = nuxia_data = shaolin_data = zhanhu_data =  np.zeros((26,20))

data_list = [overall_data, warden_data, conq_data, pk_data, law_data, cent_data, glad_data, bp_data, raider_data, warden_data, zerk_data, valk_data, 
             high_data, shaman_data, jorm_data, kensei_data, goki_data, hito_data, nobu_data, shinobi_data, musha_data, hito_data,
             tiandi_data, jun_data, nuxia_data, shaolin_data, zhanhu_data]

#Creating/Initializing files to save the statistics to
here = os.path.dirname(os.path.abspath('functions.py'))
for i in hero_list:
    if os.path.isfile(i + "_data"):
        pass
    else:
        for j, k in enumerate (data_list):
            file = open(hero_list[j] + "_data", "wb")
            np.save(file, k)
            file.close

#Prompt for hero played/played against, win or loss, magnitude of win or loss and relative skill
#FIXME: Add menu option 4
while user_input != "q":
    print("""
    Welcome to your personal For Honor statistics calculator!

    Main Menu:
    Press 1 to see the list of heroes
    Press 2 to enter new data
    Press 3 to calculate statistics
    Press m at any time to return to  main menu
    Press q at any time to quit the program
        """)
    user_input = input()

    if user_input == "1":
        hero_list_it = iter(hero_list)
        next(hero_list_it, None)
        for i in hero_list_it:
            print(i)
        continue

    elif user_input == "2":
        while user_input != "q":
            user_input = str(input("What hero did you play as? Please enter hero name\n"))
            hero = user_input.capitalize()
            if (user_input == "q") or (user_input == "m"):
                break             
            elif hero not in hero_list:
                print("Invalid hero name, please try again\n\n")
                continue        
            
            user_input = input("Who did you play against? Please enter hero name\n")
            enemy = user_input.capitalize()
            if (user_input == "q") or (user_input == "m"):
                break
            if enemy not in hero_list:
                print("Invalid hero name, please try again\n\n")
                continue

            user_input = input("Did you win? Please enter 'yes' or 'no'\n")
            match_result = user_input.lower()
            if (user_input == "q") or (user_input == "m"):
                break           
            elif match_result == "yes" or match_result == "y":
                print("What was the magnitude of your win? Enter one of the options below\n")
                user_input = input("'3-0' or '3-1' or '3-2'\n")
                result_mag = user_input
                if (user_input == "q") or (user_input == "m"):
                    break                
                elif (result_mag != "3-0") and (result_mag != "3-1") and (result_mag != "3-2"):
                    print("Invalid response, please try again\n\n")
                    continue
            elif match_result == "no" or match_result == "n":
                print("What was the magnitude of your loss? Enter one of the options below\n")
                user_input = input("'0-3' or '1-3' or '2-3'\n")
                result_mag = user_input
                if (user_input == "q") or (user_input == "m"):
                    break
                elif (result_mag != "0-3") and (result_mag != "1-3") and (result_mag != "2-3"):
                    print("Invalid response, please try again\n\n")
                    continue
            else:
                print("Invalid response, please try again\n\n")
                continue

            print("What was your skill leve realtive to your opponent? Enter one of the options below\n")
            user_input = input("'higher' or 'same' or 'lower'\n")
            skill_level = user_input.lower()
            if (user_input == "q") or (user_input == "m"):
                break
            elif skill_level != "higher" and skill_level != "same" and skill_level != "lower":
                print("Invalid response, please try again\n\n")
                continue        
            print("Thank you! The database will be updated\n\n")

            #Initialize variables and lists
            new_data = []
            overall_data = []
            hero_data = []
            infile = 'in???'
            outfile = 'out???'
            row_num = -69
    
            #Update the overall_data file with the new data from the questionnaire
            infile = open("Overall_data", "rb")
            new_data = np.load(infile, allow_pickle = True)
            infile.close
            outfile = open("Overall_data", "wb")

            row_num = 0
            overall_data = f.update_data(match_result, skill_level, result_mag, row_num, new_data)
            np.save(outfile, overall_data)
            outfile.close

            #Update hero specific data with the new data from the questionnaire
            infile = open(hero + "_data", "rb") 
            new_data = np.load(infile, allow_pickle = True)
            infile.close
            outfile = open(hero + "_data", "wb")

            #Determine which row of the matrix to update based on the enemy fought
            for i, j in enumerate (hero_list):
                if enemy == j:
                    row_num = i - 1
                    break

            hero_data = f.update_data(match_result, skill_level, result_mag, row_num, new_data)
            np.save(outfile, new_data)
            outfile.close
            
            #Ask if they would like to quit or return to menu or calculate statistics
            break
    
        elif (user_input == "q") or (user_input == "m"):
        continue
    else:
        print("Invalid Response")
        continue
    continue
    ##Next menu options - calculate statistics or close program
    #if user_input == 
    #while menu_check != "q":
    #    user_input = input("Would you like to calculate statistics? Please enter 'yes' or 'no'\n\n")
    #    if user_input == "no":
    #        print("Goodbye :)")
    #        program_check = "q"
    #        break;
    #    elif (user_input != "yes") and (user_input != "no"):
    #        print("Invalid input, please try again")
    #        continue
    #    if user_input == "yes":
    #        print("Which statistics would you like to calculate? Select an option below:\\n")
    #        print("""
    #        1. Overall data 
    #        2. Hero data   
    #        """)
    #        user_input = input("Please enter '1' or '2'\\n")
 


    #FIX ME: Determine the overall data (total wins, total losses, win %)
   
    #FIX ME: Determine the data for the hero you played as (total wins, total losses, win %
    #   wins/losses against specific heroes, win % against specific heroes) 
    #   calculate the matchup score (higher = better) for each hero
    
    #FIX ME: Determine the best hero using the average of all matchup scores (higher = better)
       



        




