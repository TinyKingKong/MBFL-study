# buggy_list = ['Chart17', 'Chart22']
# buggy_list = ['Lang7', 'Lang12', 'Lang15', 'Lang34', 'Lang46', 'Lang48', 'Lang55', 'Lang57', 'Lang63']
# buggy_list = ['Closure31', 'Closure51', 'Closure62', 'Closure62', 'Closure73', 'Closure122']
# for item in buggy_list:
#     print(item)

with open('C:\\Users\\TinyKingKong214\\Desktop\\SmartFL.txt', 'r') as f:
    lines = f.readlines()
    f.close()

for l in lines:
    print(l.split(' ')[0])