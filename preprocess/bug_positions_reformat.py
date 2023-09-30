import os
#将BugPosition.txt中行号166-170 改成: 166,167,168,169,170

def process_bug_positions(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        f.close()

    with open('E:\\defects4j\\fault-localization-data\\fault-localization.cs.washington.edu\\data\\BugPosition_.txt', 'w') as f:
        for pos in lines:
            pos = pos.replace('\n','')
            pos_l = pos.split('@')

            f.write(pos_l[0] + '#')

            pos_l_class_l = pos_l[1].split('/')
            pos_l_class = '.'.join(pos_l_class_l)#
            print(pos_l_class)
            f.write(pos_l_class + '#')

            to_file_line_list = []
            line_num_l = pos_l[2].split(',')
            for line_num in line_num_l:
                if '-' in line_num:
                    start_end = line_num.split('-')
                    for l in range(int(start_end[0]),int(start_end[1]) + 1):
                        to_file_line_list.append(str(l))
                else:
                    to_file_line_list.append(line_num)
            pos_l_lines = ','.join(to_file_line_list)
            f.write(pos_l_lines + '\n')
            print(pos_l_lines)
        f.close()




if __name__ == '__main__':
    file_path = 'E:\\defects4j\\fault-localization-data\\fault-localization.cs.washington.edu\\data\\BugPositions.txt'
    process_bug_positions(file_path)
    pass

