# muse
import csv
import numpy as np

from utils.file_utils import *


'''
    muse:   根据killmap.csv 生成 kill_matrix。每个元素唯一标识了一个测试在一个mutant下的执行情况。1为PASS,0为其他。
    META:   根据killmap.csv 生成 kill_matrix。每个元素唯一标识了一个测试在一个mutant下的执行情况。
            1为PASS(可能出现在所有行),2为FAIL -> FAIL_(只会出现在initially_falling_tests所在的行)，0为其他。
    MICRO:  同META。
'''


def generate_muse_kill_matrix(program_data_path, matrix_row, matrix_col, all_tests_list):
    initially_falling_tests_list = []
    kill_matrix = np.zeros((matrix_row, matrix_col))
    with open(os.path.join(program_data_path, 'killmap.csv'), newline='', encoding='utf-8') as f:
        csv_lines = csv.reader(_.replace('\x00', '') for _ in f)
        for line in csv_lines:
            if line[1] == '0' and line[7] != '':
                initially_falling_tests_list.append(line[0])
            if line[1] != '0' and line[3] == 'PASS':
                test_index = all_tests_list.index(line[0])
                mutant_id = int(line[1])
                kill_matrix[test_index][mutant_id - 1] = 1
    f.close()
    return kill_matrix, initially_falling_tests_list



