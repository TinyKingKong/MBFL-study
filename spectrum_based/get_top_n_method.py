import os
import glob
import math
from tqdm import tqdm
import json
import numpy as np
from kk import *

def get_top(sbfl):
    nnn=0
    top1 = 0
    top5 = 0
    top10 = 0
    mar = []
    sbfl_files = glob.glob(os.path.join('./data/zsave', '**/%s.json'%(sbfl)), recursive=True)

    for sbfl_file in sbfl_files:
        pro = sbfl_file.split('/')[6]
        id = sbfl_file.split('/')[7]
        bug_path = './data/method-level-BugPosition/%s/%s%s.txt'%(pro,pro,id)
        with open(bug_path,'r') as ff:
            bug_pros = ff.read().strip().splitlines()
        if len(bug_pros) == 0:
            nnn+=1
            mar.append(200)
            continue
        positions = []
        for bug_pro in bug_pros:
            st = int(bug_pro.split('#')[2])
            end = int(bug_pro.split('#')[3])
            for i in range(st,end + 1):
                func_name = bug_pros[0].split('.')[-1].split('#')[0]
                positions.append(func_name+'#'+ str(i))
            
        with open(sbfl_file,'r') as f1:
            sbfl_rank = json.load(f1)
        rank1,rank5,rank10,rank200 = get_rank(sbfl_rank)
        if len(rank1) > 0:
            for position in positions:
                if position== sbfl_rank[0]['line']:
                    top1 += 1
                    break

        for position in positions:
            is_ok = False
            for jj in rank5:
                if jj['line'] == position:
                    top5 += 1
                    is_ok = True
                    break
            if is_ok:
                break
        for position in positions:
            is_ok = False

            for kk in rank10:
                if kk['line'] == position:
                    top10 += 1
                    is_ok = True
                    break
            if is_ok:
                break
        good_mar = []
        for position in positions:
            find = False

            for num,mm in enumerate(rank200):
                if position == mm['line']:
                    good_mar.append(num + 1)
                    find = True
                    break
            if find == False:
                good_mar.append(200)
        mar.append(min(good_mar))
    Mar = np.mean(mar)
    #print(nnn)
    mtop1,mtop5,mtop10 = top1 / math.sqrt(9916),top5 / math.sqrt(9916),top10 / math.sqrt(9916)
    mmar = Mar*math.sqrt(9916)
    print(f"{sbfl}\t{top1}\t{top5}\t{top10}\t{Mar:.1f}\t{mtop1:.2f}\t{mtop5:.2f}\t{mtop10:.2f}\t{mmar:.2f}")

sbfl_f=[ample,anderberg,arithmetic_mean,barinel,cohen,dice,dstar2,euclid,geometric_mean,goodman,hamann,harmonic_mean,jaccard,kulczynskil1,kulczynskil2,m1,m2,ochiai,op2,rogers_tanimoto,russell_rao,s_rensen_dice,simple_matching,sokal,tarantula,zoltar]

# get_top(anderberg.__name__)

for sbfln in sbfl_f:
    get_top(sbfln.__name__)
