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

#List of playable heroes
hero_list = ["Warden", "Conqueror", "Peacekeeper", "Lawbringer", "Centurion", "Gladiator", "Vortiger", 
                 "Raider", "Warlord", "Berserker", "Valkyrie", "Highlander", "Shaman", "Jormungandr", 
                 "Kensei", "Shugoki", "Orochi", "Nobushi", "Shinobi", "Aramusha", "Hitokiri", "Tiandi", "Jiang Jun", 
                 "Nuxia", "Shaolin", "Zhanhu"] 

#Initialize arrays for hero data (and put them in a list)
overall_data = np.zeros((1, 20))
warden_data = conq_data = pk_data = law_data = cent_data = glad_data = bp_data = np.zeros((26, 20))
raider_data = warlord_data = zerk_data = valk_data = high_data = shaman_data = jorm_data = np.zeros((26,20))
kensei_data = goki_data = roach_data = nobu_data = shinobi_data = musha_data = hito_data = np.zeros((26,20))
tiandi_data = jun_data = nuxia_data = shaolin_data = zhanhu_data = np.zeros((26,20))

datafile_list = [overall_data, warden_data, conq_data, pk_data, law_data, cent_data, glad_data, bp_data, raider_data, warlord_data, zerk_data, valk_data, 
             high_data, shaman_data, jorm_data, kensei_data, goki_data, roach_data, hito_data, nobu_data, shinobi_data, musha_data, hito_data,
             tiandi_data, jun_data, nuxia_data, shaolin_data, zhanhu_data]

#Creating/Initializing files to save the data to
f.create_files()

#Prompt for hero played/played against, win or loss, magnitude of win or loss and relative skill
print("Welcome to your personal For Honor statistics calculator!")
while user_input != "q":
    user_input = input("""
    Main Menu:
    Press 1 to see the list of heroes
    Press 2 to enter new data
    Press 3 to calculate new statistics
    Press 4 to show most recent statistics
    Press m at any time to return to main menu
    Press q at any time to quit the program
        """)

    if user_input == "1":
        for i in hero_list:
            print(i)
    elif user_input == "2":
        while user_input != "q":
            user_input = str(input("What hero did you play as? Please enter hero name\n"))
            hero = user_input.title()
            if (user_input == "q") or (user_input == "m"):
                break             
            elif hero not in hero_list:
                print("Invalid hero name, please try again\n\n")
                continue        
            
            user_input = input("Who did you play against? Please enter hero name\n")
            enemy = user_input.title()
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

            print("What was your skill level realtive to your opponent? Enter one of the options below\n")
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
            with open(hero + "_data", "rb") as infile: 
                new_data = np.load(infile, allow_pickle = True)
                outfile = open(hero + "_data", "wb")

            #Determine which row of the matrix to update based on the enemy fought
            for i, j in enumerate (hero_list):
                if enemy == j:
                    row_num = i - 1
                    break
            hero_data = f.update_data(match_result, skill_level, result_mag, row_num, new_data)
            np.save(outfile, new_data)
            outfile.close   
            break

        continue

    elif user_input == "3":
        print("Calculating statistics, please stand by :)")
        f.calculate_stats(hero_list)
        
    elif(user_input == "4"):      
        print("""
        What statistics would you like to see?
        1. Overall statistics
        2. Individual Hero statistics 
        """)
        stat_option = input("Select option '1' or '2'\n")
        if stat_option == '1':
            #Put the hero scores into a dicitonary
            with open("Hero_stats", "rb") as hero_file:
                stats = np.load(hero_file)
                hero_scores = {}
                hero_scores2 = {}
                for i, hero in enumerate(hero_list[1:26]):
                    hero_scores.update({hero : stats[i][107]})
                    hero_scores2.update({hero : stats[i][107]})
                
            #Obtain the top 3 heroes and worst 3 heroes from the dictionary
            best = []
            worst = []
            for i in range(3):
                best.append(max(hero_scores, key=hero_scores.get))
                worst.append(min(hero_scores2, key=hero_scores2.get))
                del hero_scores[best[i]]
                del hero_scores2[worst[i]]     
                
            with open("Overall_stats", "rb") as overall_file:
                stats = np.load(overall_file)

            print("""
            Total wins: {0}
            Total losses: {1}
            Win ratio: %{2}
            
            Best 3 Heroes:
            1. {3}
            2. {4}
            3. {5}

            Worst 3 Heroes:
            1. {6}
            2. {7}
            3. {8}

            """.format(stats[0], stats[1], stats[2], best[0], best[1], best[2], worst[0], worst[1], worst[2]))
            #FIXME: Put this into function

        if stat_option == '2':
            index = 69420
            with open("Hero_stats", "rb") as file:
                stats = np.load(file)
                option = input("""
                Which hero statistics would you like to see?
                Please enter hero name
                """)
                option = option.title()
                index = f.stats_index(option)

                hero_matchups = {}
                hero_matchups2 = {}
                for i, hero in enumerate(hero_list):
                    hero_matchups.update({hero : stats[index][81 + i]})
                    hero_matchups2.update({hero : stats[index][81 + i]})
                
                #Obtain the top 3 heroes and worst 3 heroes
                best = []
                worst = []
                for i in range(3):
                    best.append(max(hero_matchups, key=hero_matchups.get))
                    worst.append(min(hero_matchups2, key=hero_matchups2.get))
                    del hero_matchups[best[i]]
                    del hero_matchups2[worst[i]]
                #Print the stats based on the character selected
                print("""
                Hero: {0}

                Wins: {1}
                Losses: {2}
                Win Ratio: %{3}

                Best Matchups
                1. {4}
                2. {5}
                3. {6}

                Worst Matchups:
                1. {7}
                2. {8}
                3. {9}
                """.format(option, stats[index][0], stats[index][1], stats[index][2], best[0], best[1], best[2], worst[0], worst[1], worst[2]))
                #FIXME: Add an option to select the opponent you want the stats about, for example:
                #Warden vs Conq - show wins, losses, %, matchup score for my warden against conquerors
        else:
            print("Invalid Response")

        continue                                              
         
    elif (user_input == "q") or (user_input == "m"):
        continue
    else:
        print("Invalid Response")

    continue



        




