import numpy as np
import os


"""
    根据 mutants_suspicious_vector,生成语句可疑分数。
    m_index_list:记录了不重复的 class:line 在mutants.log里的索引。从1开始。
    如: [1,123,456,...,1990,1990]表示第一个class:line从第1行开始。第二个class:line从123行开始
"""


def generate_meta_lines_suspicious_vector(mutants_suspicious_vector, program_data_path):
    with open(os.path.join(program_data_path, 'mutants.log'), newline='', encoding='utf-8') as f:
        mutants = f.readlines()
        f.close()
    m_index = 0
    class_line_pair_list, m_index_list = [], []

    for m in mutants:
        m_index += 1
        m_list = m.split(':')
        if [m_list[4], m_list[5]] not in class_line_pair_list:
            m_index_list.append(m_index)
            class_line_pair_list.append([m_list[4], m_list[5]])
    mutants_log_lines = int(mutants_suspicious_vector.shape[0])
    print('mutants_log_lines:{}'.format(mutants_log_lines))
    m_index_list.append(mutants_log_lines + 1)
    lines_suspicious_score = []
    for l in range(len(m_index_list) - 1):
        mutants_num = m_index_list[l + 1] - m_index_list[l]
        if mutants_num == 0:
            mutants_num += 1
            print('mutants number is 0, add one automatically, m_index_list = {}'.format(m_index_list[l]))
        np_arr_m = np.zeros(mutants_num)
        i = 0
        for idx in range(m_index_list[l] - 1, m_index_list[l + 1] - 1):
            np_arr_m[i] = mutants_suspicious_vector[idx]
            i += 1
        lines_suspicious_score.append(np.max(np_arr_m))

    assert len(lines_suspicious_score) == len(class_line_pair_list)
    return lines_suspicious_score, class_line_pair_list



