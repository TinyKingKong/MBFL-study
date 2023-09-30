

with open('E:\\defects4j\\fault-localization\\fault_type\\D4J_faulty_types\\coarse_grained\\Assignment.txt', 'r') as file:
    assignment_lines = file.readlines()
    file.close()

with open('E:\\defects4j\\fault-localization\\fault_type\\D4J_faulty_types\\coarse_grained\\Conditional.txt', 'r') as file:
    conditional_lines = file.readlines()
    file.close()

with open('E:\\defects4j\\fault-localization\\fault_type\\D4J_faulty_types\\coarse_grained\\Exception.txt', 'r') as file:
    exception_lines = file.readlines()
    file.close()

with open('E:\\defects4j\\fault-localization\\fault_type\\D4J_faulty_types\\coarse_grained\\Loop.txt', 'r') as file:
    loop_lines = file.readlines()
    file.close()

with open('E:\\defects4j\\fault-localization\\fault_type\\D4J_faulty_types\\coarse_grained\\MethodCall.txt', 'r') as file:
    method_call_lines = file.readlines()
    file.close()

with open('E:\\defects4j\\fault-localization\\fault_type\\D4J_faulty_types\\coarse_grained\\MethodDefinition.txt', 'r') as file:
    method_definition_lines = file.readlines()
    file.close()

with open('E:\\defects4j\\fault-localization\\fault_type\\D4J_faulty_types\\coarse_grained\\ObjectInstantiation.txt', 'r') as file:
    object_instantiation_lines = file.readlines()
    file.close()

with open('E:\\defects4j\\fault-localization\\fault_type\\D4J_faulty_types\\coarse_grained\\Return.txt', 'r') as file:
    return_lines = file.readlines()
    file.close()

with open('E:\\defects4j\\fault-localization\\fault_type\\D4J_faulty_types\\coarse_grained\\Type.txt', 'r') as file:
    type_lines = file.readlines()
    file.close()

with open('E:\\defects4j\\fault-localization\\fault_type\\D4J_faulty_types\\coarse_grained\\Variable.txt', 'r') as file:
    variable_lines = file.readlines()
    file.close()

assignment_related_bugs = []
for line in assignment_lines:
    line = line.split('\t')
    project_id = line[0].split(' ')[0] + line[0].split(' ')[1]
    assignment_related_bugs.append(project_id)

conditional_related_bugs = []
for line in conditional_lines:
    line = line.split('\t')
    project_id = line[0].split(' ')[0] + line[0].split(' ')[1]
    conditional_related_bugs.append(project_id)

exception_related_bugs = []
for line in exception_lines:
    line = line.split('\t')
    project_id = line[0].split(' ')[0] + line[0].split(' ')[1]
    exception_related_bugs.append(project_id)

loop_related_bugs = []
for line in loop_lines:
    line = line.split('\t')
    project_id = line[0].split(' ')[0] + line[0].split(' ')[1]
    loop_related_bugs.append(project_id)

method_call_related_bugs = []
for line in method_call_lines:
    line = line.split('\t')
    project_id = line[0].split(' ')[0] + line[0].split(' ')[1]
    method_call_related_bugs.append(project_id)

method_definition_related_bugs = []
for line in method_definition_lines:
    line = line.split('\t')
    project_id = line[0].split(' ')[0] + line[0].split(' ')[1]
    method_definition_related_bugs.append(project_id)

method_definition_related_bugs = []
for line in method_definition_lines:
    line = line.split('\t')
    project_id = line[0].split(' ')[0] + line[0].split(' ')[1]
    method_definition_related_bugs.append(project_id)

object_instantiation_related_bugs = []
for line in object_instantiation_lines:
    line = line.split('\t')
    project_id = line[0].split(' ')[0] + line[0].split(' ')[1]
    object_instantiation_related_bugs.append(project_id)

return_related_bugs = []
for line in return_lines:
    line = line.split('\t')
    project_id = line[0].split(' ')[0] + line[0].split(' ')[1]
    return_related_bugs.append(project_id)

type_related_bugs = []
for line in type_lines:
    line = line.split('\t')
    project_id = line[0].split(' ')[0] + line[0].split(' ')[1]
    type_related_bugs.append(project_id)

variable_related_bugs = []
for line in variable_lines:
    line = line.split('\t')
    project_id = line[0].split(' ')[0] + line[0].split(' ')[1]
    variable_related_bugs.append(project_id)

print(assignment_related_bugs)
print(conditional_related_bugs)
print(exception_related_bugs)
print(loop_related_bugs)
print(method_call_related_bugs)
print(method_definition_related_bugs)
print(object_instantiation_related_bugs)
print(return_related_bugs)
print(type_related_bugs)
print(variable_related_bugs)

chart_faulty_type = []
for i in range(26):
    faulty_types = []
    if 'Chart' + str(i + 1) in assignment_related_bugs:
        faulty_types.append('assignment')
    if 'Chart' + str(i + 1) in conditional_related_bugs:
        faulty_types.append('conditional')
    if 'Chart' + str(i + 1) in exception_related_bugs:
        faulty_types.append('exception')
    if 'Chart' + str(i + 1) in loop_related_bugs:
        faulty_types.append('loop')
    if 'Chart' + str(i + 1) in method_call_related_bugs:
        faulty_types.append('method_call')
    if 'Chart' + str(i + 1) in method_definition_related_bugs:
        faulty_types.append('method_definition')
    if 'Chart' + str(i + 1) in object_instantiation_related_bugs:
        faulty_types.append('object_instantiation')
    if 'Chart' + str(i + 1) in return_related_bugs:
        faulty_types.append('return')
    if 'Chart' + str(i + 1) in type_related_bugs:
        faulty_types.append('type')
    if 'Chart' + str(i + 1) in variable_related_bugs:
        faulty_types.append('variable')
    chart_faulty_type.append(faulty_types)

lang_faulty_type = []
for i in range(65):
    faulty_types = []
    if 'Lang' + str(i + 1) in assignment_related_bugs:
        faulty_types.append('assignment')
    if 'Lang' + str(i + 1) in conditional_related_bugs:
        faulty_types.append('conditional')
    if 'Lang' + str(i + 1) in exception_related_bugs:
        faulty_types.append('exception')
    if 'Lang' + str(i + 1) in loop_related_bugs:
        faulty_types.append('loop')
    if 'Lang' + str(i + 1) in method_call_related_bugs:
        faulty_types.append('method_call')
    if 'Lang' + str(i + 1) in method_definition_related_bugs:
        faulty_types.append('method_definition')
    if 'Lang' + str(i + 1) in object_instantiation_related_bugs:
        faulty_types.append('object_instantiation')
    if 'Lang' + str(i + 1) in return_related_bugs:
        faulty_types.append('return')
    if 'Lang' + str(i + 1) in type_related_bugs:
        faulty_types.append('type')
    if 'Lang' + str(i + 1) in variable_related_bugs:
        faulty_types.append('variable')
    lang_faulty_type.append(faulty_types)


math_faulty_type = []
for i in range(106):
    faulty_types = []
    if 'Math' + str(i + 1) in assignment_related_bugs:
        faulty_types.append('assignment')
    if 'Math' + str(i + 1) in conditional_related_bugs:
        faulty_types.append('conditional')
    if 'Math' + str(i + 1) in exception_related_bugs:
        faulty_types.append('exception')
    if 'Math' + str(i + 1) in loop_related_bugs:
        faulty_types.append('loop')
    if 'Math' + str(i + 1) in method_call_related_bugs:
        faulty_types.append('method_call')
    if 'Math' + str(i + 1) in method_definition_related_bugs:
        faulty_types.append('method_definition')
    if 'Math' + str(i + 1) in object_instantiation_related_bugs:
        faulty_types.append('object_instantiation')
    if 'Math' + str(i + 1) in return_related_bugs:
        faulty_types.append('return')
    if 'Math' + str(i + 1) in type_related_bugs:
        faulty_types.append('type')
    if 'Math' + str(i + 1) in variable_related_bugs:
        faulty_types.append('variable')
    math_faulty_type.append(faulty_types)

time_faulty_type = []
for i in range(27):
    faulty_types = []
    if 'Time' + str(i + 1) in assignment_related_bugs:
        faulty_types.append('assignment')
    if 'Time' + str(i + 1) in conditional_related_bugs:
        faulty_types.append('conditional')
    if 'Time' + str(i + 1) in exception_related_bugs:
        faulty_types.append('exception')
    if 'Time' + str(i + 1) in loop_related_bugs:
        faulty_types.append('loop')
    if 'Time' + str(i + 1) in method_call_related_bugs:
        faulty_types.append('method_call')
    if 'Time' + str(i + 1) in method_definition_related_bugs:
        faulty_types.append('method_definition')
    if 'Time' + str(i + 1) in object_instantiation_related_bugs:
        faulty_types.append('object_instantiation')
    if 'Time' + str(i + 1) in return_related_bugs:
        faulty_types.append('return')
    if 'Time' + str(i + 1) in type_related_bugs:
        faulty_types.append('type')
    if 'Time' + str(i + 1) in variable_related_bugs:
        faulty_types.append('variable')
    time_faulty_type.append(faulty_types)


mockito_faulty_type = []
for i in range(38):
    faulty_types = []
    if 'Mockito' + str(i + 1) in assignment_related_bugs:
        faulty_types.append('assignment')
    if 'Mockito' + str(i + 1) in conditional_related_bugs:
        faulty_types.append('conditional')
    if 'Mockito' + str(i + 1) in exception_related_bugs:
        faulty_types.append('exception')
    if 'Mockito' + str(i + 1) in loop_related_bugs:
        faulty_types.append('loop')
    if 'Mockito' + str(i + 1) in method_call_related_bugs:
        faulty_types.append('method_call')
    if 'Mockito' + str(i + 1) in method_definition_related_bugs:
        faulty_types.append('method_definition')
    if 'Mockito' + str(i + 1) in object_instantiation_related_bugs:
        faulty_types.append('object_instantiation')
    if 'Mockito' + str(i + 1) in return_related_bugs:
        faulty_types.append('return')
    if 'Mockito' + str(i + 1) in type_related_bugs:
        faulty_types.append('type')
    if 'Mockito' + str(i + 1) in variable_related_bugs:
        faulty_types.append('variable')
    mockito_faulty_type.append(faulty_types)


closure_faulty_type = []
for i in range(133):
    faulty_types = []
    if 'Closure' + str(i + 1) in assignment_related_bugs:
        faulty_types.append('assignment')
    if 'Closure' + str(i + 1) in conditional_related_bugs:
        faulty_types.append('conditional')
    if 'Closure' + str(i + 1) in exception_related_bugs:
        faulty_types.append('exception')
    if 'Closure' + str(i + 1) in loop_related_bugs:
        faulty_types.append('loop')
    if 'Closure' + str(i + 1) in method_call_related_bugs:
        faulty_types.append('method_call')
    if 'Closure' + str(i + 1) in method_definition_related_bugs:
        faulty_types.append('method_definition')
    if 'Closure' + str(i + 1) in object_instantiation_related_bugs:
        faulty_types.append('object_instantiation')
    if 'Closure' + str(i + 1) in return_related_bugs:
        faulty_types.append('return')
    if 'Closure' + str(i + 1) in type_related_bugs:
        faulty_types.append('type')
    if 'Closure' + str(i + 1) in variable_related_bugs:
        faulty_types.append('variable')
    closure_faulty_type.append(faulty_types)

for i in range(26):
    print('Chart' + str(i + 1) + ':', end='')
    print(chart_faulty_type[i])

for i in range(65):
    print('Lang' + str(i + 1) + ':', end='')
    print(lang_faulty_type[i])

for i in range(106):
    print('Math' + str(i + 1) + ':', end='')
    print(math_faulty_type[i])

for i in range(27):
    print('Time' + str(i + 1) + ':', end='')
    print(time_faulty_type[i])

for i in range(38):
    print('Mockito' + str(i + 1) + ':', end='')
    print(mockito_faulty_type[i])

for i in range(133):
    print('Closure' + str(i + 1) + ':', end='')
    print(closure_faulty_type[i])
