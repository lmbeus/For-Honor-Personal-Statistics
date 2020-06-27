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
