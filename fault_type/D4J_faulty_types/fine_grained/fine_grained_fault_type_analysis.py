import json


with open('E:\\defects4j\\fault-localization\\fault_type\\D4J_faulty_types\\fine_grained\\defects4j-bugs.json', 'r',
          encoding='utf-8') as f:
    json_file = json.load(f)


for bug_project in json_file:
    print(bug_project)
