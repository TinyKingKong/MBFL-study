import numpy as np
import math

'''    
    根据kill_matrix,对每个mutants生成mutant_suspicious_score
'''


def generate_meta_mutants_suspicious_vector(kill_matrix,
                                            initially_falling_tests_list,
                                            all_tests_list,
                                            mutants_num):
    total_failed = len(initially_falling_tests_list)
    failed_m, pass_m = np.zeros(mutants_num), np.zeros(mutants_num)
    initially_falling_tests_index_list = []
    for test in initially_falling_tests_list:
        initially_falling_tests_index_list.append(all_tests_list.index(test))

    for col in range(mutants_num):
        for f_row in initially_falling_tests_index_list:
            if (kill_matrix[:, col][f_row] == 1) or (kill_matrix[:, col][f_row] == 2):
                failed_m[col] += 1
        for row in range(len(all_tests_list)):
            if row not in initially_falling_tests_index_list and kill_matrix[:, col][row] == 0:
                pass_m[col] += 1
    mutants_suspicious_vector = failed_m / np.sqrt(total_failed * (failed_m + pass_m))
    return mutants_suspicious_vector






