import os
import time
import math
from tqdm import tqdm
import json
def ample(exef,exep,nexef,nexep):
    return exef / (exef + nexef + exep)
def anderberg(exef,exep,nexef,nexep):
    return exef / (exef + 2*(nexef + exep))
def arithmetic_mean(exef,exep,nexef,nexep):
    numerator = 2 * exef * nexep - 2 * nexef *exep
    denominator = (exef + exep)*(nexep + nexef) + (exef + nexef)*(exep + nexep)
    return numerator / denominator
def barinel(exef,exep,nexef,nexep):
    return 1 - exep / (exep + exef)
def cohen(exef,exep,nexef,nexep):
    numerator = 2 * (exef * nexep - nexep * exep)
    denominator = (exef + exep)*(nexep+exep)+(exef+nexef)*(nexef+nexep)
    return numerator / denominator
def dice(exef,exep,nexef,nexep):
    return (2*exef)/(exef+2*(nexef+exep))
def dstar2(exef,exep,nexef,nexep):
    return (exef*exef)/(exep+nexef)
def euclid(exef,exep,nexef,nexep):
    return math.sqrt(exef+nexep)
def geometric_mean(exef,exep,nexef,nexep):
    numerator = exef*nexep - nexef*exep
    denominator = (exef+exep)*(nexep+nexef)*(exef+nexef)*(exep+nexep)
    return numerator/denominator
def goodman(exef,exep,nexef,nexep):
    return (2*exef - nexef -exep) / (2*exef + nexef +exep)
def hamann(exef,exep,nexef,nexep):
    numerator = exef + nexep -nexef -exep
    denominator = exef + nexef + exep + nexep
    return numerator / denominator
def harmonic_mean(exef,exep,nexef,nexep):
    numerator = (exef*nexep-nexef*exep)*(exef+exep)*(nexep+nexef)+(exef+nexef)*(exep+nexep)
    denominator = (exef+exep)*(nexep+nexef) + (exef+nexef)*(exep+nexep)
    return numerator / denominator
def jaccard(exef,exep,nexef,nexep):
    return exef / (2*exef + nexef)
def kulczynskil1(exef,exep,nexef,nexep):
    return exef / (nexef + exep)
def kulczynskil2(exef,exep,nexef,nexep):
    return 0.5*(exef/(exef+nexef) + exef/(exef+exep))
def m1(exef,exep,nexef,nexep):
    return (exef+nexep) / (nexef+exep)
def m2(exef,exep,nexef,nexep):
    return exef / (exef+nexep+2*(nexef+exep))
def ochiai(exef,exep,nexef,nexep):
    return exef / math.sqrt((exef+nexef) * (exef+exep))
def op2(exef,exep,nexef,nexep):
    return (exef-exep) / (exep + exef +1)
def rogers_tanimoto(exef,exep,nexef,nexep):
    return (exef+nexep)/((exef+nexep+2*(nexef+exep)))
def russell_rao(exef,exep,nexef,nexep):
    return(exef)/(exef+nexef+exep+nexep)
def s_rensen_dice(exef,exep,nexef,nexep):
    return (2*exef)/(2*exef+nexef+exep)
def simple_matching(exef,exep,nexef,nexep):
    return (exef+nexep)/(exef+nexef+exep+nexep)
def sokal(exef,exep,nexef,nexep):
    numerator = 2*(exef + nexep)
    denominator = (2*(exef+nexep) + nexef + exep)
    return numerator / denominator
def tarantula(exef,exep,nexef,nexep):
    numerator = exef/(exef+nexef)
    denominator = exef/(exef+nexef) + exep/(exep+nexep)
    return numerator / denominator
def zoltar(exef,exep,nexef,nexep):
    return exef / (exef+nexef+exep+10000*nexef*exep/exef)


def get_rank(sbfl_rank):
    new_rank = []
    rank1,rank5,rank10,rank200 = [],[],[],[]
    flag = False
    equal = 1
    for i in range(len(sbfl_rank) - 1):
        if(sbfl_rank[i]['score'] == sbfl_rank[i+1]['score']):
            flag = True
            equal += 1
        else:
            if flag:
                sum_rank = 0
                for ee in range(equal):
                    sum_rank += i + 1 - ee
                for ee in range(equal):
                    dict = {}
                    dict['line'] = sbfl_rank[i - ee]['line']
                    dict['score'] = sbfl_rank[i - ee]['score']
                    dict['rank'] = (sum_rank / equal)
                    new_rank.append(dict)
                flag = False
                equal = 1
            else:
                dict = {}
                dict['line'] = sbfl_rank[i]['line']
                dict['score'] = sbfl_rank[i]['score']
                dict['rank'] = i + 1
                new_rank.append(dict)
    for rank in new_rank:
        if rank['rank'] == 1:
            rank1.append(rank)
        if rank['rank'] <= 5:
            rank5.append(rank)
        if rank['rank'] <= 10:
            rank10.append(rank)
        if rank['rank'] <= 200:
            rank200.append(rank)
        
    
    # print('ok')
    return rank1,rank5,rank10,rank200

# with open('/data/cmd/fault-localization.cs.washington.edu/data/zsave/Time/4/ochiai.json','r') as f1:
#     sbfl_rank = json.load(f1)
# get_rank(sbfl_rank)
def sbfl(pro,pro_id):
    sbfl_f=[ample,anderberg,arithmetic_mean,barinel,cohen,dice,dstar2,euclid,geometric_mean,goodman,hamann,harmonic_mean,jaccard,kulczynskil1,kulczynskil2,m1,m2,ochiai,op2,rogers_tanimoto,russell_rao,s_rensen_dice,simple_matching,sokal,tarantula,zoltar]
    sbfl_dict = {
        'list1':[],
        'list2':[],
        'list3':[],
        'list4':[],
        'list5':[],
        'list6':[],
        'list7':[],
        'list8':[],
        'list9':[],
        'list10':[],
        'list11':[],
        'list12':[],
        'list13':[],
        'list14':[],
        'list15':[],
        'list16':[],
        'list17':[],
        'list18':[],
        'list19':[],
        'list20':[],
        'list21':[],
        'list22':[],
        'list23':[],
        'list24':[],
        'list25':[],
        'list26':[],
    }
    print(pro,pro_id)
    matrix_path = '/data/cmd/fault-localization.cs.washington.edu/data/%s/%s/gzoltar-files/gzoltars/%s/%s/matrix'%(pro,pro_id,pro,pro_id)

    spectra_path = '/data/cmd/fault-localization.cs.washington.edu/data/%s/%s/gzoltar-files/gzoltars/%s/%s/spectra'%(pro,pro_id,pro,pro_id)
    with open(matrix_path,'r') as f:
        matrix = f.read().strip().splitlines()
    with open(spectra_path,'r') as f:
        spectra = f.read().strip().splitlines()
    
    myspectra = []
    for sp in spectra:
        my_line = sp.split('.')[-1]
        myspectra.append(my_line)
    mymatrix = []
    for cov in matrix:
        lines = cov.split(' ')
        mymatrix.append(lines)

    for i in tqdm(range(len(mymatrix[0]) - 1)):#i是文件的代码行数
        exef = 0
        exep = 0
        nexef = 0
        nexep = 0
        for j in range(len(mymatrix)):
            if  mymatrix[j][-1] == '-':
                if mymatrix[j][i] == '0':
                    nexef += 1
                elif mymatrix[j][i] == '1':
                    exef += 1
            if  mymatrix[j][-1] == '+':
                if mymatrix[j][i] == '0':
                    nexep += 1
                elif mymatrix[j][i] == '1':
                    exep += 1
        for ii,func in enumerate(sbfl_f):
            dict = {}
            dict['line'] = myspectra[i]
            try:
                dict['score'] = func(exef,exep,nexef,nexep)
                sbfl_dict['list%s'%(ii+1)].append(dict)
            except Exception as e:
                dict['score'] = -50
                sbfl_dict['list%s'%(ii+1)].append(dict)

    savepath='/data/cmd/fault-localization.cs.washington.edu/data/zsave/%s/%s'%(pro,pro_id)
    if not os.path.exists(savepath):
        os.makedirs(savepath)

    for i,func in enumerate(sbfl_f):
        sbfl_dict['list%s'%(i+1)] = sorted(sbfl_dict['list%s'%(i+1)], key=lambda x: x['score'], reverse=True)
     
        path = savepath + '/%s.json'%(func.__name__)
        with open(path, 'w', encoding='utf-8') as file1:
            json.dump(sbfl_dict['list%s'%(i+1)][0:500], file1, ensure_ascii=False,indent=4)
    
# sbfl('Math',5)
# for i in range(26):
#     sbfl('Chart',i+1)
# for i in range(27):
#     sbfl('Time',i+1)
# for i in range(65):
#     sbfl('Lang',i+1)
# for i in range(38):
#     sbfl('Mockito',i+1)
# for i in range(106):
#     sbfl('Math',i+1)
# for i in range(133):
#     sbfl('Closure',i+1)

