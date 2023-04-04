with open('names.txt', 'r') as f:
    lines = f.readlines()

with open('names.txt', 'w') as f:
    for line in lines:
        modified_line = '"' + line.strip() + '",\n'
        f.write(modified_line)
