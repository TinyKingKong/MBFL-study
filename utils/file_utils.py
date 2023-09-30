import csv
import os
'''
计算kill_matrix的列数,列与mutants相关
'''


def get_kill_matrix_col_number(program_data_path):
    with open(os.path.join(program_data_path, 'mutants.log'), 'r',encoding='utf-8') as f:
        lines = f.readlines()
        last_line = lines[-1]
        mutants_number = last_line.split(':')[0]
        f.close()
    return int(mutants_number)


'''
    计算kill_matrix的行数,即不重复的tests的个数。同时返回去重后的tests的列表
'''


def get_kill_matrix_row_number(program_data_path):
    csv.field_size_limit(500 * 1024 * 1024)
    with open(os.path.join(program_data_path, 'killmap.csv'), newline='', encoding='utf-8') as f:
        csv_lines = csv.reader(_.replace('\x00', '') for _ in f)
        tests_count = 0
        all_tests_list = []
        for line in csv_lines:
            if line[0] not in all_tests_list:
                all_tests_list.append(line[0])
                tests_count += 1
        f.close()
    return tests_count


def get_all_tests_list(program_data_path):
    csv.field_size_limit(500 * 1024 * 1024)
    with open(os.path.join(program_data_path, 'killmap.csv'), newline='', encoding='utf-8') as f:
        csv_lines = csv.reader(_.replace('\x00', '') for _ in f)
        all_tests_list = []
        for line in csv_lines:
            if line[0] not in all_tests_list:
                all_tests_list.append(line[0])
        f.close()
    return all_tests_list

def determine_dir(path_name):
    if os.path.exists(path_name):
        dir_list = os.listdir(path_name)
        if len(dir_list) == 0:
            return 'empty'
        else:
            if 'killmaps' in dir_list:
                using_dir = 'killmaps'
            if 'killmaps-unoptimized' in dir_list:
                using_dir = 'killmaps-unoptimized'
            return using_dir
    else:
        return 'Invalid path'




