import numpy as np
import os

'''
    对结果进行排序
'''


def result_sorter(lines_suspicious_score, top):
    index_list = np.argsort(-np.array(lines_suspicious_score))
    candidate_list_top = index_list[:top]
    return candidate_list_top


'''
    结果展示
'''


def collect_candidate_lines(lines_suspicious_score, class_line_pair_list, des_dir, des_file, top):
    if not os.path.isdir(des_dir):
        os.makedirs(des_dir)
    f = open(os.path.join(des_dir, des_file), 'w')
    rank = 0
    candidate_list_top = result_sorter(lines_suspicious_score, top)
    for e in candidate_list_top:
        candidate_line = str(rank + 1) + '#' + class_line_pair_list[e][0] + '#' + class_line_pair_list[e][1] + '#' + str(lines_suspicious_score[e])
        rank += 1
        f.write(candidate_line + '\n')
    f.close()

#lines_suspicious_score
#class_line_pair_list
# def collect_spectrum_candidate_lines(lines_suspicious_score, class_line_pair_list, des_dir, des_file, top):
# def collect_spectrum_candidate_lines(lines_and_pairs, des_dir, des_file, top):
def collect_spectrum_candidate_lines(lines_and_pairs, project_id, formula_id_list, bug_id, mode, top):
    for i in range(len(lines_and_pairs)):
        des_dir = os.path.join(os.path.abspath('..'),
                               'candidate-lines-result',
                               str(mode).lower(),
                               str(formula_id_list[i]),
                               str(project_id).lower())
        des_file = str(project_id + str(bug_id) + '.txt')
        lines_suspicious_score = lines_and_pairs[i][0]
        class_line_pair_list = lines_and_pairs[i][1]
        if not os.path.isdir(des_dir):
            os.makedirs(des_dir)
        f = open(os.path.join(des_dir, des_file), 'w')
        rank = 0
        candidate_list_top = result_sorter(lines_suspicious_score, top)
        for e in candidate_list_top:
            candidate_line = str(rank + 1) + '#' + class_line_pair_list[e][0] + '#' + class_line_pair_list[e][
                1] + '#' + str(lines_suspicious_score[e])
            rank += 1
            f.write(candidate_line + '\n')
        f.close()

def collect_micro_candidate_lines(lines_suspicious_score, class_line_pair_list, lines_mutants_covered, des_dir, des_file, top):
    if not os.path.isdir(des_dir):
        os.makedirs(des_dir)
    f = open(os.path.join(des_dir, des_file), 'w')
    rank = 0
    candidate_list_top = result_sorter(lines_suspicious_score, top)
    for e in candidate_list_top:
        candidate_line = str(rank + 1) + '#' + class_line_pair_list[e][0] + '#' + class_line_pair_list[e][1] + '#' + str(lines_suspicious_score[e]) + '#' + str(lines_mutants_covered[e])
        rank += 1
        f.write(candidate_line + '\n')
    f.close()


#-----------------------------------------------------------------------------------------------------------
#result_ms_sorter()和collect_micro_ms_candidate_lines()是和mutant selection相关
def result_ms_sorter(lines_suspicious_score, lines_mutants_covered, top):
    lines_suspicious_score = np.array(lines_suspicious_score)
    lines_suspicious_score = 1 / (1 + (np.exp(-lines_suspicious_score)))  # sigmoid
    index = 0
    for line_mutants in lines_mutants_covered: #line_mutants  [[],[]]
        for mutant in line_mutants:
            if '[' in mutant[3] and ']' in mutant[3]:
                lines_suspicious_score[index] += 0.4
                break
            if '==' in mutant[1] or '!=' in mutant[1]:
                lines_suspicious_score[index] += 0.2
                break
            if 'true' in mutant[3] or 'TRUE' in mutant[3] or 'false' in mutant[3] or 'FALSE' in mutant[3]:
                lines_suspicious_score[index] += 0.2
                break
            if 'if(' in mutant[3] and ')' in mutant[3]:
                lines_suspicious_score[index] += 0.2
                break
            # if 'null' in mutant[3]:
            #     lines_suspicious_score[index] += 0.2
            #     break
            # if 'return' in mutant[3]:
            #     lines_suspicious_score[index] += 0.2
            #     break
            # if mutant[0] == 'COR' or mutant[0] == 'STD':
            #     lines_suspicious_score[index] += 0.05
            #     break

        index += 1

    index_list = np.argsort(-np.array(lines_suspicious_score))
    candidate_list_top = index_list[:top]
    return candidate_list_top, lines_suspicious_score


def collect_micro_ms_candidate_lines(lines_suspicious_score, class_line_pair_list, lines_mutants_covered, des_dir,
                                     des_file, top):
    if not os.path.isdir(des_dir):
        os.makedirs(des_dir)
    f = open(os.path.join(des_dir, des_file), 'w')
    rank = 0
    candidate_list_top, lines_suspicious_score_ = result_ms_sorter(lines_suspicious_score, lines_mutants_covered, top)  # 索引
    for e in candidate_list_top:
        # candidate_line = str(rank + 1) + '#' + class_line_pair_list[e][0] + '#' + class_line_pair_list[e][
        #     1] + '#' + str(lines_suspicious_score[e]) + '#' + str(lines_mutants_covered[e])
        candidate_line = str(rank + 1) + '#' + class_line_pair_list[e][0] + '#' + class_line_pair_list[e][1] + '#' + str(lines_suspicious_score_[e])
        rank += 1
        f.write(candidate_line + '\n')

    f.close()
