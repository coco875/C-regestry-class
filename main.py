import re

class_reg = r"class\( *(\w+) *, *(\w+)"
function_reg = r"(\w+) +([\w_]+)\(([\w_, *]*)\)"

def transform_file(file:str):
    with open(file, 'r') as f:
        lines = f.readlines()
    parenthies = 0
    name = ''
    parent = ''
    line_to_del = []
    for i in range(len(lines)):
        if re.search(class_reg, lines[i]):
            name, parent = re.search(class_reg, lines[i]).groups()
            line_to_del.append(i)
        parenthies += lines[i].count('(') - lines[i].count(')')
        if parenthies > 0:
            lines[i] = re.sub(function_reg, rf'\1 {name}_{parent}_\2(\3)', lines[i])
        if parenthies == 0 and parent != '':
            line_to_del.append(i)
            name = ''
            parent = ''
    with open("result_"+file, 'w') as f:
        for i in range(len(lines)):
            if i not in line_to_del:
                f.write(lines[i])

transform_file('test.c')