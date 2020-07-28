import numpy as np
import math
import os

def update_data(match_result, skill_level, result_mag, row_num, new_data):
    #Update the data based on the new data
    if match_result == "yes" or match_result == "y":
        new_data[row_num, 0] += 1
        if result_mag == "3-0" and skill_level == "higher":
            new_data[row_num, 2] += 1 
        elif result_mag == "3-0" and skill_level == "same":
            new_data[row_num, 3] += 1
        elif result_mag == "3-0" and skill_level == "lower":
            new_data[row_num, 4] += 1
        elif result_mag == "3-1" and skill_level == "higher":
            new_data[row_num, 5] += 1
        elif result_mag == "3-1" and skill_level == "same":
            new_data[row_num, 6] += 1
        elif result_mag == "3-1" and skill_level == "lower":
            new_data[row_num, 7] += 1
        elif result_mag == "3-2" and skill_level == "higher":
            new_data[row_num, 8] += 1
        elif result_mag == "3-2" and skill_level == "same":
            new_data[row_num, 9] += 1
        elif result_mag == "3-2" and skill_level == "lower":
            new_data[row_num, 10] += 1
    elif match_result == "no" or match_result == "n":
        new_data[row_num, 1] += 1
        if result_mag == "0-3" and skill_level == "higher":
            new_data[row_num, 11] += 1 
        elif result_mag == "0-3" and skill_level == "same":
            new_data[row_num, 12] += 1
        elif result_mag == "0-3" and skill_level == "lower":
            new_data[row_num, 13] += 1
        elif result_mag == "1-3" and skill_level == "higher":
            new_data[row_num, 14] += 1
        elif result_mag == "1-3" and skill_level == "same":
            new_data[row_num, 15] += 1
        elif result_mag == "1-3" and skill_level == "lower":
            new_data[row_num, 16] += 1
        elif result_mag == "2-3" and skill_level == "higher":
            new_data[row_num, 17] += 1
        elif result_mag == "2-3" and skill_level == "same":
            new_data[row_num, 18] += 1
        elif result_mag == "2-3" and skill_level == "lower":
            new_data[row_num, 19] += 1

    return new_data

def create_files():
    file_names = ["Overall", "Warden", "Conqueror", "Peacekeeper", "Lawbringer", "Centurion", "Gladiator", "Vortiger", 
                 "Raider", "Warlord", "Berserker", "Valkyrie", "Highlander", "Shaman", "Jormungandr", 
                 "Kensei", "Shugoki", "Orochi", "Nobushi", "Shinobi", "Aramusha", "Hitokiri", "Tiandi", "Jiang Jun", 
                 "Nuxia", "Shaolin", "Zhanhu"]
    for i in file_names:
        if os.path.isfile(i + "_data"):
            pass
        else:
            for j, k in enumerate(datafile_list):
                file = open(file_names[j] + "_data", "wb")
                np.save(file, k)
                file.close

def calculate_stats(hero_list):
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
    with open("Overall_data", "rb") as file:
        overall_data = np.load(file)
        #Load the hero data into a list of seperate numpy arrays
        for i, j in enumerate (hero_list):
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

    #Save the statistics arrays to the corresponding files
    file1 = open("Overall_stats", "wb")
    file2 = open("Hero_stats", "wb")
    np.save(file1, overall_stats)
    np.save(file2, stats_list)
    file1.close
    file2.close

def stats_index(option):
    if option == "Warden":
        loc = 0
    elif option == "Conqueror":
        loc = 1
    elif option == "Peacekeeper":
        loc = 2
    elif option == "Lawbringer":
        loc = 3
    elif option == "Centurion":
        loc = 4
    elif option == "Gladiator":
        loc = 5
    elif option == "Vortiger":
        loc = 6
    elif option == "Raider":
        loc = 7
    elif option == "Warlord":
        loc = 8
    elif option == "Berserker":
        loc = 9
    elif option == "Valkyrie":
        loc = 10
    elif option == "Highlander":
        loc = 11
    elif option == "Shaman":
        loc = 12
    elif option == "Jormungandr":
        loc = 13
    elif option == "Kensei":
        loc = 14
    elif option == "Shugoki":
        loc = 15
    elif option == "Orochi":
        loc = 16
    elif option == "Nobushi":
        loc = 17
    elif option == "Shinobi":
        loc = 18
    elif option == "Aramusha":
        loc = 19
    elif option == "Hitokiri":
        loc = 20
    elif option == "Tiandi":
        loc = 21
    elif option == "Jiang Jun":
        loc = 22
    elif option == "Nuxia":
        loc = 23
    elif option == "Shaolin":
        loc = 24
    elif option == "Zhanhu":
        loc = 25
    return loc