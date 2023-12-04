with open('input', 'r') as f:
    input = f.read()

# only 12 red cubes, 13 green cubes, and 14 blue cubes
result = []
lines = input.splitlines()
max_w = len(lines)
max_h = len(lines[0])

for i, line in enumerate(lines):
    curr_char = ''
    has_part = False
    # for j, char in enumerate(line):
    for j in range(len(line) + 1):
        if j < max_h and line[j].isdigit():
            char = line[j]
            # print(curr_char)
            curr_char += char
            for outer in range(-1, 2):
                for inner in range(-1, 2):
                    if 0 <= i + outer < max_w and 0 <= j + inner < max_h:
                        check = lines[i + outer][j + inner]
                        if not check.isdigit() and check != '.':
                            print(curr_char)
                            has_part = True
        elif len(curr_char) > 0:
            # print(curr_char)
            if has_part:
                result.append(int(curr_char))
            has_part = False
            curr_char = ''

print(sum(result))
