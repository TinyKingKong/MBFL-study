import numpy as np
import math

'''    
    根据kill_matrix,对每个mutants生成mutant_suspicious_score
'''


def generate_spectrum_mutants_suspicious_vector(kill_matrix,
                                                initially_falling_tests_list,
                                                all_tests_list,
                                                mutants_num):
    total_failed = len(initially_falling_tests_list)
    total_pass = len(all_tests_list) - total_failed;
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
    # Tarantula_mutants_suspicious_vector = (failed_m / total_failed) / (failed_m / total_failed + pass_m / total_pass)
    # Op2_mutants_suspicious_vector = failed_m - (pass_m / (total_pass + 1))
    # Barinel_mutants_suspicious_vector = 1 - pass_m / (pass_m + failed_m)
    # DStar_2 = failed_m ** 2 / (pass_m + (total_failed - failed_m))

    # Ochiai2_mutants_suspicious_vector = (failed_m * (total_pass - pass_m)) / np.sqrt((failed_m + pass_m) * (total_failed + total_pass - failed_m - pass_m) * total_failed * total_pass)
    # M1_mutants_suspicious_vector = (failed_m + (total_pass - pass_m)) / (pass_m + (total_failed - failed_m))
    # M2_mutants_suspicious_vector = failed_m / (total_pass + 2 * total_failed - failed_m + pass_m)
    # Euclid_mutants_suspicious_vector = np.sqrt(failed_m + pass_m)
    # Wong1_mutants_suspicious_vector = failed_m
    # Wong2_mutants_suspicious_vector = failed_m - pass_m
    # Kulczynskil1_mutants_suspicious_vector = failed_m / (total_failed - failed_m + pass_m)
    # Kulczynskil2_mutants_suspicious_vector = 1/2 * (failed_m / total_failed + failed_m / (failed_m + pass_m))


    Jaccard_mutants_suspicious_vector = failed_m / (pass_m + total_failed)
    Anderberg_mutants_suspicious_vector = failed_m / (failed_m + 2 * (total_failed - failed_m + pass_m))
    Sorensen_Dice_mutants_suspicious_vector = 2 * failed_m / (failed_m + pass_m + total_failed)
    Dice_mutants_suspicious_vector = 2 * failed_m / (total_failed + pass_m)
    Russell_and_rao_mutants_suspicious_vector = failed_m / (total_failed + total_pass)
    Hamann_mutants_suspicious_vector = (total_pass + total_failed - 2 * (failed_m + pass_m)) / (total_failed + total_pass)
    Simple_Matching_mutants_suspicious_vector = (failed_m + total_pass - pass_m) / (total_failed + total_pass)
    Sokal_mutants_suspicious_vector = 2 * (failed_m + total_pass - pass_m) / (2 * (failed_m + total_pass - pass_m) + pass_m + total_failed - failed_m)
    Rogers_and_Tanimoto_mutants_suspicious_vector = (failed_m + total_pass - pass_m) / (total_pass + total_failed + pass_m + total_failed - failed_m)
    Goodman_mutants_suspicious_vector = (2 * failed_m - pass_m - (total_failed - failed_m)) / (2 * failed_m + pass_m + (total_failed - failed_m))
    hamming_mutants_suspicious_vector = failed_m + total_pass - pass_m
    Zoltar_mutants_suspicious_vector = failed_m / ((failed_m + pass_m + total_failed - failed_m) + (10000 * (total_failed - failed_m) * pass_m / failed_m))
    Ample_mutants_suspicious_vector = np.abs(failed_m / total_failed - pass_m / total_pass)
    Geometric_meam_mutants_suspicious_vector = (failed_m * (total_pass - pass_m) - pass_m * (total_failed - failed_m)) / np.sqrt((failed_m + pass_m) * (total_pass + total_failed - failed_m - pass_m) * total_failed * total_pass)
    Harmonic_mean_mutants_suspicious_vector = (failed_m * (total_pass - pass_m) - pass_m * (total_failed - failed_m)) * ((failed_m + pass_m) * (total_failed + total_failed - failed_m - pass_m) + total_failed * total_pass) / ((failed_m + pass_m) * (total_pass + total_failed - failed_m - pass_m) * total_failed * total_pass)
    Arithmetic_mean_mutants_suspicious_vector = 2 * (failed_m * (total_pass - pass_m) - pass_m * (total_failed - failed_m)) / ((failed_m + pass_m) * (total_pass + total_failed - failed_m - pass_m) + total_failed * total_pass)
    Cohen_mutants_suspicious_vector = 2 * (failed_m * (total_pass - pass_m) - pass_m * (total_failed - failed_m)) / ((failed_m + pass_m) * total_pass + total_failed * total_pass)


    #Overlap_mutants_suspicious_vector = failed_m / np.min([np.min(failed_m), np.min(pass_m), np.min(total_failed - failed_m)])


    return [Jaccard_mutants_suspicious_vector, Anderberg_mutants_suspicious_vector, Sorensen_Dice_mutants_suspicious_vector, Dice_mutants_suspicious_vector,
            Russell_and_rao_mutants_suspicious_vector, Hamann_mutants_suspicious_vector, Simple_Matching_mutants_suspicious_vector, Sokal_mutants_suspicious_vector,
            Rogers_and_Tanimoto_mutants_suspicious_vector, Goodman_mutants_suspicious_vector, hamming_mutants_suspicious_vector, Zoltar_mutants_suspicious_vector,
            Ample_mutants_suspicious_vector, Geometric_meam_mutants_suspicious_vector, Harmonic_mean_mutants_suspicious_vector, Arithmetic_mean_mutants_suspicious_vector, Cohen_mutants_suspicious_vector]
