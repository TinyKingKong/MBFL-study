import os

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            line_count = len(lines)
            return line_count
    except FileNotFoundError:
        return 0
    except Exception as e:
        return 0


def determine_path(base_folder):
    target_folder_name = "killmaps-unoptimized"
    # 获取指定文件夹中的所有子文件夹
    subfolders = [f.name for f in os.scandir(base_folder) if f.is_dir()]
    # 检查目标文件夹名是否在子文件夹列表中
    if target_folder_name in subfolders:
        return "killmaps-unoptimized"
    else:
        return "killmaps"


def count(root_path, info_list):
    all_mutants_count = []
    for info in info_list:
        for i in range(1, info[1] + 1):
            tmp_path = os.path.join(root_path, info[0], str(i))
            mutants_log_path = os.path.join(tmp_path, determine_path(tmp_path), info[0], str(i), "mutants.log")
            mutants_num = count_lines_in_file(mutants_log_path)
            all_mutants_count.append(mutants_num)
    print(len(all_mutants_count))
    return all_mutants_count

if __name__ == "__main__":
    # root_path1 = "E:/defects4j/fault-localization-data/fault-localization.cs.washington.edu/data"
    # root_path2 = "G://"
    # info_list1 = [["Chart", 26], ["Lang", 65], ["Math", 106], ["Mockito", 38], ["Time", 27]]
    # info_list2 = [['Closure', 133]]
    # m1 = count(root_path1, info_list1)
    # m2 = count(root_path2, info_list2)
    # print(sum(m1) + sum(m2))

    root_path1 = "E:/defects4j/fault-localization-data/fault-localization.cs.washington.edu/data"
    root_path2 = "G://"
    # info_list1 = [["Chart", 26], ["Lang", 65], ["Math", 106], ["Mockito", 38], ["Time", 27]]
    info_list2 = [['Closure', 133]]
    #info_list1 = [["Time", 27]]
    m1 = count(root_path2, info_list2)

    print(sum(m1) / 133)



