import os


def read_txt_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        f.close()
    return lines


def result_show(mode, project_id_list, method_level_bug_position_root_path, method_level_candidate_root_path):
    project_candidate_list_list = []
    project_id_list = []
    for project_id in projects_id:
        candidate_file_path = os.path.join(method_level_candidate_root_path, str(mode), str(project_id))
        candidate_files = [f for f in os.listdir(candidate_file_path) if f.endswith('.txt')]

        for candidate_file in candidate_files:
            method_level_bug_position_path = os.path.join(method_level_bug_position_root_path, str(project_id), str(candidate_file))


            candidate_methods = read_txt_file(os.path.join(candidate_file_path, str(candidate_file)))
            bug_methods = read_txt_file(method_level_bug_position_path)

            if not os.path.exists(os.path.join(os.path.abspath('.'), 'method-level-result', str(mode).lower())):
                os.makedirs(os.path.join(os.path.abspath('.'), 'method-level-result', str(mode).lower()))

            candidate_list = []
            for bug_method in bug_methods:
                for candidate_method in candidate_methods:
                    candidate_method_info = candidate_method.split('#')
                    if len(candidate_method_info[1].split('@')) < 2:
                        candidate_class_name = candidate_method_info[1].split('@')[0]
                        candidate_method_name = 'xxx'
                    else:
                        candidate_class_name = candidate_method_info[1].split('@')[0]
                        candidate_method_name = candidate_method_info[1].split('@')[1]
                    candidate_line = int(candidate_method_info[2])

                    bug_method_info = bug_method.split('#')
                    bug_class_name = bug_method_info[0]
                    bug_method_name = bug_method_info[1]
                    bug_method_start_line = int(bug_method_info[2])
                    bug_method_end_line = int(bug_method_info[3])

                    #if candidate_class_name == bug_class_name and candidate_method_name == bug_method_name and bug_method_start_line <= candidate_line <= bug_method_end_line:
                    if candidate_class_name == bug_class_name and candidate_method_name == bug_method_name:
                        candidate_list.append(candidate_method)

            #
            with open(os.path.join(os.path.abspath('.'), 'method-level-result', str(mode).lower(), str(project_id) + '.txt'), 'a') as f:
                f.write('----------' + str(candidate_file.split('.')[0]) + '----------\n')
                for candidate in candidate_list:
                    f.write(str(candidate))

            project_candidate_list_list.append(candidate_list)
            project_id_list.append(str(candidate_file.split('.')[0]))
    return project_candidate_list_list, project_id_list



def top_show(project_candidate_list_list, project_id_list):
    top1_list, top3_list, top5_list, top10_list = [], [], [], []
    top1, top3, top5, top10 = 0, 0, 0, 0
    assert len(project_candidate_list_list) == len(project_id_list)
    rank_list_list = []
    for project_id in project_id_list:
        project_candidates_list = project_candidate_list_list[project_id_list.index(project_id)]
        rank_list = []
        for project_candidate in project_candidates_list:
            rank_list.append(int(project_candidate.split('#')[0]))
        rank_list_list.append(rank_list)

    for project_id in project_id_list:
        rank_list = rank_list_list[project_id_list.index(project_id)]
        if any(x == 1 for x in rank_list):
            top1_list.append(project_id)
            top1 = top1 + 1
            top3_list.append(project_id)
            top3 = top3 + 1
            top5_list.append(project_id)
            top5 = top5 + 1
            top10_list.append(project_id)
            top10 = top10 + 1
            continue
        if any(x <= 3 for x in rank_list):
            top3_list.append(project_id)
            top3 = top3 + 1
            top5_list.append(project_id)
            top5 = top5 + 1
            top10_list.append(project_id)
            top10 = top10 + 1
            continue
        if any(x <= 5 for x in rank_list):
            top5_list.append(project_id)
            top5 = top5 + 1
            top10_list.append(project_id)
            top10 = top10 + 1
            continue
        if any(x <= 10 for x in rank_list):
            top10_list.append(project_id)
            top10 = top10 + 1


    print('top1:' + str(top1) + ',' + str(top1 / 395))
    print('top3:' + str(top3) + ',' + str(top3 / 395))
    print('top5:' + str(top5) + ',' + str(top5 / 395))
    print('top10:' + str(top10) + ',' + str(top10 / 395))

    print('top1_list', top1_list)
    print('top3_list', top3_list)
    print('top5_list', top5_list)
    print('top10_list', top10_list)

    Chart, Lang, Math, Time, Mockito, Closure = 0, 0, 0, 0, 0, 0
    for t1 in top1_list:
        if t1.startswith('Chart'):
            Chart = Chart + 1
        if t1.startswith('Lang'):
            Lang = Lang + 1
        if t1.startswith('Math'):
            Math = Math + 1
        if t1.startswith('Time'):
            Time = Time + 1
        if t1.startswith('Mockito'):
            Mockito = Mockito + 1
        if t1.startswith('Closure'):
            Closure = Closure + 1
    print('top1:')
    print(Chart, Lang, Math, Time, Mockito, Closure)
    print(Chart + Lang + Math + Time + Mockito + Closure)

    Chart, Lang, Math, Time, Mockito, Closure = 0, 0, 0, 0, 0, 0
    for t1 in top3_list:
        if t1.startswith('Chart'):
            Chart = Chart + 1
        if t1.startswith('Lang'):
            Lang = Lang + 1
        if t1.startswith('Math'):
            Math = Math + 1
        if t1.startswith('Time'):
            Time = Time + 1
        if t1.startswith('Mockito'):
            Mockito = Mockito + 1
        if t1.startswith('Closure'):
            Closure = Closure + 1
    print('top3:')
    print(Chart, Lang, Math, Time, Mockito, Closure)
    print(Chart + Lang + Math + Time + Mockito + Closure)

    Chart, Lang, Math, Time, Mockito, Closure = 0, 0, 0, 0, 0, 0
    for t1 in top5_list:
        if t1.startswith('Chart'):
            Chart = Chart + 1
        if t1.startswith('Lang'):
            Lang = Lang + 1
        if t1.startswith('Math'):
            Math = Math + 1
        if t1.startswith('Time'):
            Time = Time + 1
        if t1.startswith('Mockito'):
            Mockito = Mockito + 1
        if t1.startswith('Closure'):
            Closure = Closure + 1
    print('top5:')
    print(Chart, Lang, Math, Time, Mockito, Closure)
    print(Chart + Lang + Math + Time + Mockito + Closure)

    Chart, Lang, Math, Time, Mockito, Closure = 0, 0, 0, 0, 0, 0
    for t1 in top10_list:
        if t1.startswith('Chart'):
            Chart = Chart + 1
        if t1.startswith('Lang'):
            Lang = Lang + 1
        if t1.startswith('Math'):
            Math = Math + 1
        if t1.startswith('Time'):
            Time = Time + 1
        if t1.startswith('Mockito'):
            Mockito = Mockito + 1
        if t1.startswith('Closure'):
            Closure = Closure + 1
    print('top10:')
    print(Chart, Lang, Math, Time, Mockito, Closure)
    print(Chart + Lang + Math + Time + Mockito + Closure)






if __name__ == '__main__':

    mode = 'micro_10_1'
    mode = "spectrum//jaccard"
    mode = "spectrum//op2"
    projects_id = ['chart', 'closure', 'lang', 'math', 'mockito', 'time']
    #projects_id = ['chart']
    method_level_bug_position_root_path = 'E:\\defects4j\\fault-localization\\eval\\method-level-BugPosition'
    method_level_candidate_root_path = 'E:\\defects4j\\fault-localization\\candidate-lines-result'
    #method_level_candidate_root_path = 'E:\\defects4j\\fault-localization\\candidate-lines-result-selection'
    project_candidate_list_list, project_id_list = result_show(mode, projects_id, method_level_bug_position_root_path, method_level_candidate_root_path)
    top_show(project_candidate_list_list, project_id_list)


    # Mockito3
    # top1_list101 = ['Chart11', 'Chart14', 'Chart18', 'Chart22', 'Chart7', 'Closure31', 'Closure62', 'Closure63', 'Lang1', 'Lang10', 'Lang12', 'Lang14', 'Lang15', 'Lang16', 'Lang18', 'Lang19', 'Lang20', 'Lang21', 'Lang22', 'Lang27', 'Lang28', 'Lang3', 'Lang30', 'Lang31', 'Lang34', 'Lang35', 'Lang36', 'Lang37', 'Lang39', 'Lang4', 'Lang44', 'Lang46', 'Lang48', 'Lang5', 'Lang50', 'Lang51', 'Lang52', 'Lang53', 'Lang54', 'Lang55', 'Lang57', 'Lang58', 'Lang6', 'Lang63', 'Lang7', 'Math101', 'Math105', 'Math106', 'Math23', 'Math24', 'Math26', 'Math3', 'Math38', 'Math40', 'Math44', 'Math52', 'Math55', 'Math61', 'Math63', 'Math64', 'Math65', 'Math66', 'Math68', 'Math7', 'Math78', 'Math79', 'Math81', 'Math84', 'Math89', 'Math92', 'Math94', 'Math95', 'Math97', 'Mockito1', 'Mockito12', 'Mockito16', 'Mockito19', 'Mockito8', 'Time15', 'Time2', 'Time27']
    # top1_list51 = ['Chart11', 'Chart16', 'Chart18', 'Chart22', 'Chart7', 'Closure31', 'Closure62', 'Closure63', 'Lang1', 'Lang10', 'Lang12', 'Lang14', 'Lang15', 'Lang16', 'Lang18', 'Lang19', 'Lang20', 'Lang21', 'Lang22', 'Lang27', 'Lang28', 'Lang3', 'Lang30', 'Lang31', 'Lang34', 'Lang35', 'Lang36', 'Lang37', 'Lang39', 'Lang4', 'Lang44', 'Lang46', 'Lang48', 'Lang5', 'Lang50', 'Lang51', 'Lang52', 'Lang53', 'Lang54', 'Lang55', 'Lang57', 'Lang58', 'Lang6', 'Lang63', 'Lang7', 'Math101', 'Math105', 'Math106', 'Math23', 'Math24', 'Math26', 'Math3', 'Math38', 'Math40', 'Math44', 'Math52', 'Math55', 'Math61', 'Math63', 'Math64', 'Math65', 'Math66', 'Math68', 'Math7', 'Math78', 'Math79', 'Math81', 'Math84', 'Math89', 'Math92', 'Math94', 'Math95', 'Math97', 'Mockito1', 'Mockito12', 'Mockito16', 'Mockito19', 'Mockito3', 'Mockito8', 'Time15', 'Time2', 'Time27']
    # print(len(top1_list101))
    # print(len(top1_list51))









