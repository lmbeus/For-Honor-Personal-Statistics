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
hero_list_it = iter(hero_list)
next(hero_list_it, None)

#Initialize arrays for hero statistics (and put them in a list)
overall_data = np.zeros((1, 20))
warden_data = conq_data = pk_data = law_data = cent_data = glad_data = bp_data = np.zeros((26, 20))
raider_data = warlord_data = zerk_data = valk_data = high_data = shaman_data = jorm_data = np.zeros((26,20))
kensei_data = goki_data = roach_data = nobu_data = shinobi_data = musha_data = hito_data = np.zeros((26,20))
tiandi_data = jun_data = nuxia_data = shaolin_data = zhanhu_data = np.zeros((26,20))

data_list = [overall_data, warden_data, conq_data, pk_data, law_data, cent_data, glad_data, bp_data, raider_data, warden_data, zerk_data, valk_data, 
             high_data, shaman_data, jorm_data, kensei_data, goki_data, hito_data, nobu_data, shinobi_data, musha_data, hito_data,
             tiandi_data, jun_data, nuxia_data, shaolin_data, zhanhu_data]

#Creating/Initializing files to save the statistics to
#FIXME: Turn this into a function
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
print("Welcome to your personal For Honor statistics calculator!")
while user_input != "q":
    print("""
    Main Menu:
    Press 1 to see the list of heroes
    Press 2 to enter new data
    Press 3 to calculate new statistics
    Press 4 to show most recent statistics
    Press m at any time to return to main menu
    Press q at any time to quit the program
        """)
    user_input = input()

    if user_input == "1":
        for i in hero_list_it:
            print(i)
        continue

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
            break

        continue

    elif user_input == "3":
        print("Calculating statistics, please stand by :)")

        file_list = []
        data_list = []
        stats_list = []
        overall_stats = []

        #Initilaize point weights for calculations
        #wins
        l30 = 5
        s30 = l31 = 4
        h30 = s31 = l32 = 3
        s32 =h31 = 2
        h32 = 1
        #losses
        l23 = -1
        s23 = l13 = -2
        h23 = s13 = l03 = -3
        s03 = h13 = -4
        h03 = -5
        
        #Create statistics files if they do not already exist and fill the statistics with zeros
        if os.path.isfile("Overall_stats") and os.path.isfile("Hero_stats"):
            pass
        else:
            file1 = open("Overall_stats", "wb")
            file2 = open("Hero_stats", "wb")
            np.save(file1, np.zeros(3))
            np.save(file2, np.zeros(108))
            file1.close
            file2.close

        #Load overall data into numpy array
        file = open("Overall_data", "rb")
        overall_data = np.load(file)
        file.close
        #Load the hero data into a list of seperate numpy arrays
        for i, j in enumerate (hero_list_it):
            file_list.append(open(j + "_data", "rb"))
            data_list.append(np.load(file_list[i]))
            file_list[i].close()

        #Calcualte the overall statistics
        #Initialize statistics variables
        overall_wins = overall_data[0,0]
        overall_losses = overall_data[0,1]
        overall_win_ratio = round((overall_wins / (overall_losses + overall_wins)) * 100, 2)
        overall_stats = np.array([overall_wins, overall_losses, overall_win_ratio])

        #Calculate the statistics for each hero
        #Initialize variables - create an array of statistics for each hero in the game
        warden_stats = conq_stats = pk_stats = law_stats = cent_stats = glad_stats = bp_stats = []
        raider_stats = warlord_stats = zerk_stats = valk_stats = high_stats = shaman_stats = jorm_stats = []
        kensei_stats = goki_stats = roach_stats = nobu_stats = shinobi_stats = musha_stats = hito_stats = []
        tiandi_stats = jun_stats = nuxia_stats = shaolin_stats = zhanhu_stats = []

        stats_list = [warden_stats, conq_stats, pk_stats, law_stats, cent_stats, glad_stats, bp_stats, raider_stats, warden_stats, zerk_stats, valk_stats, 
             high_stats, shaman_stats, jorm_stats, kensei_stats, goki_stats, hito_stats, nobu_stats, shinobi_stats, musha_stats, hito_stats,
             tiandi_stats, jun_stats, nuxia_stats, shaolin_stats, zhanhu_stats]

        ##Calcualte the statistics and store them inside each hero stat array
        for i in range(len(stats_list)):
            a = data_list[i] #for simpler code
            stats_list[i] = np.zeros(108)
            #Calcualte the total wins and losses and win ratio for the hero
            stats_list[i][0] =  np.sum(a[0:26, 0])
            stats_list[i][1] =  np.sum(a[0:26, 1])
            total = stats_list[i][0] + stats_list[i][1]
            if total != 0:
                stats_list[i][2] = round(stats_list[i][0] / (total) * 100, 2)  
            else:
                stats_list[i][2] = 0
            #calculate the total wins, total losses, and win ratio against each hero 
            for k in range(26):
                stats_list[i][3 + k] = a[k, 0] #wins
                stats_list[i][29 + k] = a[k, 1] #losses
                total = stats_list[i][3 + k] + stats_list[i][29 + k]
                if total != 0:
                    stats_list[i][55 + k] = round(stats_list[i][3 + k] / total, 2) #win ratio
                else:
                    stats_list[i][55 + k] = 0       
                #Calcualte hero scores using the appropriate weights
                sum_wins = (h30 * a[k, 2] + s30 * a[k, 3] + l30 * a[k, 4] + h31 * a[k, 5] + s31 * a[k, 6] + l31 * a[k, 7] +
                                h32 * a[k, 8] + s32 * a[k, 9] + l32 * a[k, 10])
                sum_losses = (h03 * a[k, 11] + s03 * a[k, 12] + l03 * a[k, 13] + h13 * a[k, 14] + s13 * a[k,15] + l13 * a[k, 16] +
                                 h23 * a[k, 17] + s23 * a[k, 18] + l23 * a[k, 19])
                stats_list[i][81 + k] = (sum_wins + sum_losses) #The last 26 (81-106) are the match-up scores
            stats_list[i][107] = np.sum(stats_list[i][81:107]) / 26 #Take the average of the match-up scores to determine overall hero score
        print(stats_list[0])

        #Save the statistics arrays to the corresponding files
        file1 = open("Overall_stats", "wb")
        file2 = open("Hero_stats", "wb")
        np.save(file1, overall_stats)
        np.save(file2, stats_list)
        file1.close
        file2.close
        #FIXME: Test overall statistics then test individual hero statistics
        #FIXME: Once tested and all is well, move the hero_stats section over to a function (make it as slick looking as possible)

                          
        #In menu option 4 output the wanted statistics  
    elif(user_input == "4"):      
        print("""
        What statistics would you like to see?
        a. Overall statistics
        b. Individual Hero statistics 
        """)
        stat_option = input("Select option 'a' or 'b'\n")
        if stat_option == 'a':
            #Determine the best and worst 3 heroes based on hero score using a dictionary
            with open("Hero_stats", "rb") as hero_file:
                stats = np.load(hero_file)
                hero_scores = {}
                for i, hero in enumerate(hero_list_it):
                    hero_scores.update({hero : stats[i][107]})
            #Obtain the top 3 heroes and worst 3 heroes
            best = []
            worst = []
            for i in range(3):
                best.append(max(hero_scores, key=hero_scores.get))
                #worst.append(min(hero_scores, key=hero_scores.get))
                del hero_scores[best[i]]
                #del hero_scores[worst[i]]     
                
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
            """.format(stats[0], stats[1], stats[2], best[0], best[1], best[2]))
            #FIXME: Put this into function

        if stat_option == 'b':
            #FIXME: Put this into a function
            with open("Hero_stats") as file:
                stats = np.load(file)
                #FIXME: determine the best 3 matchups and worst 3 matchups from the appropriate elements from the stat array
                #FIXME: print wins, losses, ratio, best matchups, worst matchups, overall hero score

                
         
    elif (user_input == "q") or (user_input == "m"):
        continue
    else:
        print("Invalid Response")

    continue

       



        




