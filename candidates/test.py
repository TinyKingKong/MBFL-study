import numpy as np
import os
import sys

print('#####: ', os.getcwd())  # 获取当前工作目录路径
print('#####: ', os.path.abspath('.'))  # 获取当前工作目录路径
print('#####: ', os.path.abspath('..'))  # 获取当前工作的父目录
print('#####: ', os.path.abspath('../..'))  # 获取当前工作的父目录的父目录


if __name__ == '__main__':
    # path_name = 'E:\\defects4j\\fault-localization-data\\fault-localization.cs.washington.edu\\data\\Lang\\12'
    # print(determine_dir(path_name))

    # all_top1 = 0.035443037974683546
    # all_top3 = 0.0759493670886076
    # all_top5 = 0.1291139240506329
    # all_top10 = 0.17468354430379746
    # all_top50 = 0.37468354430379747
    # all_top100 = 0.4430379746835443
    # all_top200 = 0.5265822784810127
    #
    # aall_top1 = 0.08354430379746836
    # aall_top3 = 0.14177215189873418
    # aall_top5 = 0.21265822784810126
    # aall_top10 = 0.27341772151898736
    # aall_top50 = 0.48860759493670886
    # aall_top100 = 0.5443037974683544
    # aall_top200 = 0.5949367088607594
    #
    # print(aall_top1 - all_top1)
    # print(aall_top3 - all_top3)
    # print(aall_top5 - all_top5)
    # print(aall_top10 - all_top10)
    # print(aall_top50 - all_top50)

    # list1 =['Closure9', 'Closure31', 'Closure38', 'Closure46', 'Closure51', 'Closure59', 'Closure62', 'Closure62', 'Closure66', 'Closure73', 'Closure122']
    #
    # for l in list1:
    #     print(l,end="")
    #     print(',',end=" ")


    a = np.array([1,2,3])
    b = np.array([4,5,6])
    c = 10 - np.array([1,2,3])
    min_a = np.min(a)
    min_b = np.min(b)
    min_c = np.min(c)
    print(np.min([min_a,min_b,min_c]))
