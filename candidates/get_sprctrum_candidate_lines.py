import os

from spectrum_based.generate_spectrum_kill_matrix import generate_spectrum_kill_matrix
from spectrum_based.generate_spectrum_lines_suspicious_vector import generate_spectrum_lines_suspicious_vector
from spectrum_based.generate_spectrum_mutants_suspicious_vector import generate_spectrum_mutants_suspicious_vector
from utils.candidates_utils import collect_spectrum_candidate_lines
from utils.file_utils import determine_dir, get_kill_matrix_row_number, get_kill_matrix_col_number, get_all_tests_list
from utils.mode_utils import is_spertrum_mode


def calculate_spectrum_and_save(raw_data_path, project_id, formula_id_list, bug_id, mode, top):
    project_id = str(project_id)
    killmap = determine_dir(raw_data_path)
    if killmap == 'empty':
        print('----------Using mode: ' + mode.upper() + '----------')
        print('----------Project-id: ' + str(project_id) + str(bug_id) + '----------')
        print('Project: ' + str(project_id) + '-' + str(bug_id) + ' does not contains a killmap. Auto skip...\n')
        return
    if killmap == 'Invalid path':
        print('----------Using mode: ' + mode.upper() + '----------')
        print('----------Project-id: ' + str(project_id) + str(bug_id) + '----------')
        print('Project: ' + str(project_id) + '-' + str(bug_id) + 'does not exits!\n')
        return
    raw_data_path = os.path.join(raw_data_path, killmap, str(project_id), str(bug_id))

    if is_spertrum_mode(mode):
        print('----------Using mode: ' + mode.upper() + '----------')
        print('----------Project-id: ' + str(project_id) + str(bug_id) + '----------')
        row = get_kill_matrix_row_number(raw_data_path)
        col = get_kill_matrix_col_number(raw_data_path)
        all_tests_list = get_all_tests_list(raw_data_path)
        if row == 0 or col == 0:
            print('Read from file: ' + raw_data_path + ' Kill matrix is empty!')
            return
        if len(all_tests_list) == 0:
            print('Require at least 1 candidates!')
            return
        print('Generating kill matrix...')
        kill_matrix, initially_falling_tests_list = generate_spectrum_kill_matrix(raw_data_path, row, col,
                                                                                  all_tests_list)
        print(initially_falling_tests_list)
        print('Complete.')
        print('Generating mutants suspicious vector...')
        mutants_suspicious_vector_list = generate_spectrum_mutants_suspicious_vector(kill_matrix,
                                                                                     initially_falling_tests_list,
                                                                                     all_tests_list,
                                                                                     col)
        print('Complete.')
        print('Generating lines suspicious vector...')
        lines_and_pairs = generate_spectrum_lines_suspicious_vector(mutants_suspicious_vector_list, raw_data_path)
        print('Complete.')
        # collect_spectrum_candidate_lines(lines_and_pairs,
        #                                  os.path.join(os.path.abspath('..'), 'candidate-lines-result',
        #                                               str(mode).lower(),
        #                                               str(project_id).lower()),
        #                                  str(project_id + str(bug_id) + '.txt'),
        #                                  top)
        collect_spectrum_candidate_lines(lines_and_pairs, project_id, formula_id_list, bug_id, mode, top)
    else:
        print("Invalid mode.")
        return


def calculate_spectrum_and_save_candidates(projects_root_path, project_id, project_num, mode, top):
    #formula_id_list = ['Tarantula', 'Op2', 'Barinel', 'DStar_2']
    #formula_id_list = ['Ochiai2', 'M1', 'M2', 'Euclid', 'Wong1', 'Wong2', 'Kulczynskil1', 'Kulczynskil2']
    formula_id_list = ['Jaccard', 'Anderberg', 'Sorensen_Dice', 'Dice', 'Russell_and_rao', 'Hamann', 'Simple_Matching', 'Sokal', 'Rogers_and_Tanimoto',
                       'Goodman', 'hamming', 'Zoltar', 'Ample', 'Geometric_meam', 'Harmonic_mean', 'Arithmetic_mean', 'Cohen']
    project_root_path = os.path.join(projects_root_path, str(project_id))
    for i in range(int(project_num)):
        bug_id = str(i + 1)
        pdp = os.path.join(project_root_path, str(bug_id))
        calculate_spectrum_and_save(pdp, project_id, formula_id_list, bug_id, mode, top)


if __name__ == '__main__':
    # 读文件，要给killmap.csv和mutants.log那个路径.
    # 比如：E:\defects4j\fault-localization-data\fault-localization.cs.washington.edu\data\Chart\10\killmaps\Chart\10
    # 写结果是独立的。根据project_id，bug_id来确定文件名

    mode = 'spectrum'
    top = 200
    chart_lang_math_mockito_time_projects_root_path = os.path.join(os.path.abspath('../..'), 'fault-localization-data',
                                                                   'fault-localization.cs.washington.edu',
                                                                   'data')

    closure_project_root_path = os.path.join('G:' + '\\')

    calculate_spectrum_and_save_candidates(chart_lang_math_mockito_time_projects_root_path, 'Chart', 26, mode, top)
    calculate_spectrum_and_save_candidates(chart_lang_math_mockito_time_projects_root_path, 'Lang', 65, mode, top)
    calculate_spectrum_and_save_candidates(chart_lang_math_mockito_time_projects_root_path, 'Math', 106, mode, top)
    calculate_spectrum_and_save_candidates(chart_lang_math_mockito_time_projects_root_path, 'Mockito', 38, mode, top)
    calculate_spectrum_and_save_candidates(chart_lang_math_mockito_time_projects_root_path, 'Time', 27, mode, top)
    calculate_spectrum_and_save_candidates(closure_project_root_path, 'Closure', 133, mode, top)
