import numpy as np
import math
import os

'''    
    根据kill_matrix,对每个mutants生成mutant_suspicious_score
'''


def generate_micro_mutants_suspicious_vector(kill_matrix,
                                             initially_falling_tests_list,
                                             all_tests_list,
                                             mutants_num,
                                             proj=None,
                                             proj_id=None):
    if not proj is None and not proj_id is None:
        muid_path = os.path.join(os.path.abspath('..'), 'mutant_selection', 'process_datacopy_muid', proj.lower(),
                                 'muid_' + proj + proj_id + ".txt")
        murank_path = os.path.join(os.path.abspath('..'), 'mutant_selection', 'mutant_ranked', proj.lower(),
                                   'mutant_ranked_' + proj + proj_id + ".txt")
        file = open(muid_path, mode='r', encoding='UTF-8')
        muid = file.readlines()
        muid = muid[1:]
        muid1 = [int(i) for i in muid]

        file = open(murank_path, mode='r', encoding='UTF-8')
        murank = file.readlines()
        murank1 = [float(i) for i in murank]

        select_result = []
        idx_rank = np.argsort(np.array(murank1))
        for idx in idx_rank:
            select_result.append(muid1[idx])
    keep_rate = 0.5
    s = int(len(select_result) * keep_rate)

    f2p, f2f_, p2f = 0, 0, 0
    total_failed = len(initially_falling_tests_list)
    failed_2_pass_m, failed_2_failed__m, pass_2_failed_m = np.zeros(mutants_num), np.zeros(mutants_num), np.zeros(mutants_num)


    # total_failed = len(initially_falling_tests_list)
    # failed_m, pass_m = np.zeros(mutants_num), np.zeros(mutants_num)
    initially_falling_tests_index_list = []
    for test in initially_falling_tests_list:
        initially_falling_tests_index_list.append(all_tests_list.index(test))

    for index in select_result[s:]:
        kill_matrix[:, index - 1] = -1

    for index in range(len(all_tests_list)):
        if index in initially_falling_tests_index_list and np.sum(kill_matrix[index] == 1) > 0:
            f2p += 1
        if index in initially_falling_tests_index_list and np.sum(kill_matrix[index] == 2) > 0:
            f2f_ += 1
        if index not in initially_falling_tests_index_list and np.sum(kill_matrix[index] == 0) > 0:
            p2f += 1


    for col in range(mutants_num):
        for f_row in initially_falling_tests_index_list:
            if kill_matrix[:, col][f_row] == 1:
                failed_2_pass_m[col] += 1

            if kill_matrix[:, col][f_row] == 2:
                failed_2_failed__m[col] += 1
        for row in range(len(all_tests_list)):
            if row not in initially_falling_tests_index_list and kill_matrix[:, col][row] == 0:
                pass_2_failed_m[col] += 1

    if p2f == 0:
        print('p2f equals 1.')
        p2f += 1
    #mutants_suspicious_vector = 10 * failed_2_pass_m + 1 * failed_2_failed__m - ((f2p + f2f_) / p2f) * pass_2_failed_m
    #mutants_suspicious_vector = (failed_2_pass_m + failed_2_failed__m) / np.sqrt(total_failed * (failed_2_pass_m + failed_2_failed__m + pass_2_failed_m))
    mutants_suspicious_vector = failed_2_pass_m + (f2p / p2f) * pass_2_failed_m
    for idx in select_result[s:]:
        mutants_suspicious_vector[idx - 1] = -9999

    return mutants_suspicious_vector
