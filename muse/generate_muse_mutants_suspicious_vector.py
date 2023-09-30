import numpy as np

'''    
    根据kill_matrix,对每个mutants生成mutant_suspicious_score
'''


def generate_muse_mutants_suspicious_vector(kill_matrix,
                                            initially_falling_tests_list,
                                            all_tests_list,
                                            mutants_num):
    f2p, p2f = 0, 0
    failed_m, pass_m = np.zeros(mutants_num), np.zeros(mutants_num)
    initially_falling_tests_index_list = []
    for test in initially_falling_tests_list:
        initially_falling_tests_index_list.append(all_tests_list.index(test))

    # 检查kill_matrix的行
    for index in range(len(all_tests_list)):
        if index in initially_falling_tests_index_list and np.sum(kill_matrix[index] == 1) > 0:
            f2p += 1
        if index not in initially_falling_tests_index_list and np.sum(kill_matrix[index] == 0) > 0:
            p2f += 1

    # 检查kill_matrix的列,计算mutants suspicious vector。
    # kill_matrix[:,col]为kill_matrix的一列
    for col in range(mutants_num):
        for idx in initially_falling_tests_index_list:
            if kill_matrix[:, col][idx] == 1:
                failed_m[col] += 1
        for row in range(len(all_tests_list)):
            if row not in initially_falling_tests_index_list and kill_matrix[:, col][row] == 0:
                pass_m[col] += 1
    if p2f == 0:
        print('p2f equals 1.')
        p2f += 1
    mutants_suspicious_vector = failed_m - (f2p / p2f) * pass_m
    return mutants_suspicious_vector
