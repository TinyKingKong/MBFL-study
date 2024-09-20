import os
import glob
import math
from tqdm import tqdm
import json
import numpy as np
from kk import *


def get_top(sbfl):
    top1 = 0
    top5 = 0
    top10 = 0
    mar = []
    sbfl_files = glob.glob(os.path.join('./data/zsave', '**/%s.json'%(sbfl)), recursive=True)

    with open('BugPositions.txt','r') as f:
        bug_p = f.read().strip().splitlines()
    for sbfl_file in sbfl_files:
        pro = sbfl_file.split('/')[6]
        id = sbfl_file.split('/')[7]
        pro_id = pro + '_' +id
        bug_pro =''
        for ii in bug_p:
            if pro_id in ii:
                bug_pro = ii
                break
        
        func_name = bug_pro.split('/')[-1].split('.')[0]
        positions = []
        pos = bug_pro.split('@')[-1].split(',')
        for po in pos:
            if '-' in po:
                st = int(po.split('-')[0])
                end = int(po.split('-')[1])
                for i in range(st,end + 1):
                    positions.append(str(i))
            else:
                if len(po) > 0:
                    positions.append(po)
        with open(sbfl_file,'r') as f1:
            sbfl_rank = json.load(f1)
        rank1,rank5,rank10,rank200 = get_rank(sbfl_rank)

        if len(rank1) > 0:
            for position in positions:
                func_line = func_name + '#' + position
                if func_line == rank1[0]['line']:
                    top1 += 1
                    break

        for position in positions:
            is_ok = False
            func_line = func_name + '#' + position
            for jj in rank5:
                if jj['line'] == func_line:
                    top5 += 1
                    is_ok = True
                    break
            if is_ok:
                break
        for position in positions:
            is_ok = False
            func_line = func_name + '#' + position
            for kk in rank10:
                if kk['line'] == func_line:
                    top10 += 1
                    is_ok = True
                    break
            if is_ok:
                break
        good_mar = []
        for position in positions:
            find = False
            func_line = func_name + '#' + position
            for num,mm in enumerate(rank200):
                if func_line == mm['line']:
                    good_mar.append(num + 1)
                    find = True
                    break
            if find == False:
                good_mar.append(200)
        mar.append(min(good_mar))
    Mar = np.mean(mar)
    mtop1,mtop5,mtop10 = top1 / math.sqrt(9916),top5 / math.sqrt(9916),top10 / math.sqrt(9916)
    mmar = Mar*math.sqrt(9916)
    #print(sbfl,': ',top1,top5,top10,Mar,Mar*math.sqrt(9916))

    print(f"{sbfl}\t{top1}\t{top5}\t{top10}\t{Mar:.1f}\t{mtop1:.2f}\t{mtop5:.2f}\t{mtop10:.2f}\t{mmar:.2f}")

sbfl_f=[ample,anderberg,arithmetic_mean,barinel,cohen,dice,dstar2,euclid,geometric_mean,goodman,hamann,harmonic_mean,jaccard,kulczynskil1,kulczynskil2,m1,m2,ochiai,op2,rogers_tanimoto,russell_rao,s_rensen_dice,simple_matching,sokal,tarantula,zoltar]

#print('    sbfl\t','Top1\t','Top5\t','Top10\t','MAR\t','                  Mtop1','                  Mtop5','                  Mtop10','                  MMAR\t')
#print('sbfl\tTop1\tTop5\tTop10\tMAR\tMtop1\tMtop5\tMtop10\tMMAR\t')
# get_top(anderberg.__name__)

for sbfln in sbfl_f:
    get_top(sbfln.__name__)
