import os


def result_show(project_id, bug_number, mode):
    with open(os.path.join(os.path.abspath('.'), 'BugPosition.txt'), encoding='utf-8') as f:
        lines = f.readlines()
        f.close()

    # 先从BugPosition.txt中取出project_id相关的行
    projects_bug_positions = []
    for line in lines:
        line = line.replace('\n', '')
        if line.startswith(str(project_id)):
            projects_bug_positions.append(line)

    # 再组合这些行，形成[[...],[...],...,[...]]
    projects_bug_positions_list = []

    for i in range(bug_number):
        tmp_list = []
        for pbp in projects_bug_positions:
            if pbp.startswith(str(project_id) + '_' + str(i + 1) + '#'):
                tmp_list.append(pbp)
        projects_bug_positions_list.append(tmp_list)
    # print(projects_bug_positions_list)

    if not os.path.exists(os.path.join(os.path.abspath('.'), 'result', str(mode).lower())):
        os.makedirs(os.path.join(os.path.abspath('.'), 'result', str(mode).lower()))
    f = open(os.path.join(os.path.abspath('.'), 'result', str(mode).lower(), str(project_id) + '.txt'), 'w')

    result_data_list = []  # 取出 eval/result/meta/Chart.txt的结果，装到list里
    for bug_id in range(bug_number):
        tmp_data_list = []
        # 读candidate-lines-result的结果,形成candidates
        if not os.path.exists(os.path.join(os.path.abspath('..'), 'candidate-lines-result', str(mode).lower(),
                                           str(project_id).lower(),
                                           str(project_id) + str(bug_id + 1) + '.txt')):
            # print(str(project_id) + str(bug_id + 1) + 'does not have a result.')
            f.write('----------' + str(project_id) + str(bug_id + 1) + '\n')
            result_data_list.append(tmp_data_list)
            continue
        #'candidate-lines-result-selection'
        with open(os.path.join(os.path.abspath('..'), 'candidate-lines-result', str(mode).lower(),#改========================================改
                               str(project_id).lower(),
                               str(project_id) + str(bug_id + 1) + '.txt')) as candidate_file:
            candidates = candidate_file.readlines()
            candidate_file.close()

        # 与先从BugPosition.txt里读出的数据比较
        project_bug_position_infos = projects_bug_positions_list[bug_id]
        f.write('----------' + str(project_id) + str(bug_id + 1) + '----------\n')
        for project_bug_position_info in project_bug_position_infos:
            buggy_project_id = project_bug_position_info.split('#')[0]
            buggy_class = project_bug_position_info.split('#')[1]
            buggy_lines = project_bug_position_info.split('#')[2]

            for candidate in candidates:
                candidate_info = candidate.split('#')
                candidate_rank = candidate_info[0]
                candidate_class = candidate_info[1].split('@')[0]
                candidate_line = candidate_info[2]
                if candidate_class in buggy_class and candidate_line in buggy_lines.split(','):
                    f.write(candidate_rank + '#' + candidate_class + '#' + candidate_line + '\n')
                    tmp_data_list.append(candidate_rank + '#' + candidate_class + '#' + candidate_line)
        result_data_list.append(tmp_data_list)
    return result_data_list


def top_show(result_list, project_id, project_num):
    assert len(result_list) == int(project_num)
    top1, top3, top5, top10, top30, top50, top100, top200 = 0, 0, 0, 0, 0, 0, 0, 0
    top1_projects, top3_projects, top5_projects, top10_projects, top30_projects, top50_projects, top100_projects, top200_projects = [], [], [], [], [], [], [], []

    for result in result_list:
        if len(result) == 0:
            continue
        if int(result[0].split('#')[0]) == 1:
            top1 += 1
            top1_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top3 += 1
            top3_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top5 += 1
            top5_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top10 += 1
            top10_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top30 += 1
            top30_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top50 += 1
            top50_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top100 += 1
            top100_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top200 += 1
            top200_projects.append(str(project_id) + str(result_list.index(result) + 1))
            continue
        if int(result[0].split('#')[0]) <= 3:
            top3 += 1
            top3_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top5 += 1
            top5_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top10 += 1
            top10_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top30 += 1
            top30_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top50 += 1
            top50_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top100 += 1
            top100_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top200 += 1
            top200_projects.append(str(project_id) + str(result_list.index(result) + 1))
            continue
        if int(result[0].split('#')[0]) <= 5:
            top5 += 1
            top5_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top10 += 1
            top10_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top30 += 1
            top30_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top50 += 1
            top50_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top100 += 1
            top100_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top200 += 1
            top200_projects.append(str(project_id) + str(result_list.index(result) + 1))
            continue
        if int(result[0].split('#')[0]) <= 10:
            top10 += 1
            top10_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top30 += 1
            top30_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top50 += 1
            top50_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top100 += 1
            top100_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top200 += 1
            top200_projects.append(str(project_id) + str(result_list.index(result) + 1))
            continue
        if int(result[0].split('#')[0]) <= 30:
            top30 += 1
            top30_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top50 += 1
            top50_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top100 += 1
            top100_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top200 += 1
            top200_projects.append(str(project_id) + str(result_list.index(result) + 1))
            continue
        if int(result[0].split('#')[0]) <= 50:
            top50 += 1
            top50_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top100 += 1
            top100_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top200 += 1
            top200_projects.append(str(project_id) + str(result_list.index(result) + 1))
            continue
        if int(result[0].split('#')[0]) <= 100:
            top100 += 1
            top100_projects.append(str(project_id) + str(result_list.index(result) + 1))
            top200 += 1
            top200_projects.append(str(project_id) + str(result_list.index(result) + 1))
            continue
        if int(result[0].split('#')[0]) <= 200:
            top200 += 1
            top200_projects.append(str(project_id) + str(result_list.index(result) + 1))
            continue
    print('project-id: {}\n'
          'top1:{}, top3:{}, top5:{}, top10:{}, top30:{}, top50:{}, top100:{}, top200:{}'.format(str(project_id), top1,
                                                                                                  top3, top5, top10,
                                                                                                  top30, top50, top100,
                                                                                                  top200))
    print(str(top1) + '/' + str(top3) + '/' + str(top5) + '/' + str(top10))
    print('top1:{}\ntop3:{}\ntop5:{}\ntop10:{}\ntop30:{}\ntop50:{}\ntop100:{}\ntop200:{}\n'.format(top1_projects,
                                                                                                   top3_projects,
                                                                                                   top5_projects,
                                                                                                   top10_projects,
                                                                                                   top30_projects,
                                                                                                   top50_projects,
                                                                                                   top100_projects,
                                                                                                   top200_projects))
    print()

    return top1, top3, top5, top10, top30, top50, top100, top200


def result_display(project_id, project_num, mode):
    result_list = result_show(project_id, project_num, mode)
    return top_show(result_list, project_id, project_num)


if __name__ == '__main__':
    #mode = 'micro_1_1'
    mode = 'spectrum//jaccard'
    #mode = 'micro_10_1'
    chart_top1, chart_top3, chart_top5, chart_top10, chart_top30, chart_top50, chart_top100, chart_top200 = result_display(
        project_id='Chart', project_num=26, mode=mode)
    lang_top1, lang_top3, lang_top5, lang_top10, lang_top30, lang_top50, lang_top100, lang_top200 = result_display(
        project_id='Lang', project_num=65, mode=mode)
    math_top1, math_top3, math_top5, math_top10, math_top30, math_top50, math_top100, math_top200 = result_display(
        project_id='Math', project_num=106, mode=mode)
    time_top1, time_top3, time_top5, time_top10, time_top30, time_top50, time_top100, time_top200 = result_display(
        project_id='Time', project_num=27, mode=mode)
    mockito_top1, mockito_top3, mockito_top5, mockito_top10, mockito_top30, mockito_top50, mockito_top100, mockito_top200 = result_display(
        project_id='Mockito', project_num=38, mode=mode)
    closure_top1, closure_top3, closure_top5, closure_top10, closure_top30, closure_top50, closure_top100, closure_top200 = result_display(
        project_id='Closure', project_num=133, mode=mode)
    all_projects = 395

    all_top1 = (chart_top1 + lang_top1 + math_top1 + mockito_top1 + time_top1 + closure_top1) / all_projects
    print('all_top1_precision:{}'.format(all_top1))
    all_top3 = (chart_top3 + lang_top3 + math_top3 + mockito_top3 + time_top3 + closure_top3) / all_projects
    print('all_top3_precision:{}'.format(all_top3))
    all_top5 = (chart_top5 + lang_top5 + math_top5 + mockito_top5 + time_top5 + closure_top5) / all_projects
    print('all_top5_precision:{}'.format(all_top5))
    all_top10 = (chart_top10 + lang_top10 + math_top10 + mockito_top10 + time_top10 + closure_top10) / all_projects
    print('all_top10_precision:{}'.format(all_top10))
    all_top50 = (chart_top50 + lang_top50 + math_top50 + mockito_top50 + time_top50 + closure_top50) / all_projects
    print('all_top50_precision:{}'.format(all_top50))
    all_top100 = (
                         chart_top100 + lang_top100 + math_top100 + mockito_top100 + time_top100 + closure_top100) / all_projects
    print('all_top100_precision:{}'.format(all_top100))
    all_top200 = (
                         chart_top200 + lang_top200 + math_top200 + mockito_top200 + time_top200 + closure_top200) / all_projects
    print('all_top200_precision:{}'.format(all_top200))

    print()
    print('all_top1:{}'.format(chart_top1 + lang_top1 + math_top1 + mockito_top1 + time_top1 + closure_top1))
    print('all_top3:{}'.format(chart_top3 + lang_top3 + math_top3 + mockito_top3 + time_top3 + closure_top3))
    print('all_top5:{}'.format(chart_top5 + lang_top5 + math_top5 + mockito_top5 + time_top5 + closure_top5))
    print('all_top10:{}'.format(chart_top10 + lang_top10 + math_top10 + mockito_top10 + time_top10 + closure_top10))
    print(str(chart_top1 + lang_top1 + math_top1 + mockito_top1 + time_top1 + closure_top1) + '/' +
          str(chart_top3 + lang_top3 + math_top3 + mockito_top3 + time_top3 + closure_top3) + '/' +
          str(chart_top5 + lang_top5 + math_top5 + mockito_top5 + time_top5 + closure_top5) + '/' +
          str(chart_top10 + lang_top10 + math_top10 + mockito_top10 + time_top10 + closure_top10))

