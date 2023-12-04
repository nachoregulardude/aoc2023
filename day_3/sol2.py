from collections import defaultdict

with open('input2', 'r') as f:
    input = f.read()

# only 12 red cubes, 13 green cubes, and 14 blue cubes
result = []
lines = input.splitlines()
max_w = len(lines)
max_h = len(lines[0])

gear_nums = defaultdict(list)
for i, line in enumerate(lines):
    curr_char = ''
    has_part = False
    gears = set()
    # for j, char in enumerate(line):
    for j in range(len(line) + 1):
        if j < max_h and line[j].isdigit():
            char = line[j]
            curr_char += char
            # print(curr_char)
            for outer in range(-1, 2):
                for inner in range(-1, 2):
                    if 0 <= i + outer < max_w and 0 <= j + inner < max_h:
                        check = lines[i + outer][j + inner]
                        if not check.isdigit() and check != '.':
                            print(curr_char)
                            has_part = True
                        if check == '*':
                            gears.add((i + outer, j + inner))
        elif curr_char:
            for gear in gears:
                gear_nums[gear].append(int(curr_char))
            if has_part:
                result.append(int(curr_char))
            gears = set()
            has_part = False
            curr_char = ''

# print(sum(result))
ans = 0
for k, v in gear_nums.items():
    if len(v) == 2:
        print(ans)
        ans += v[0] * v[1]
print(ans)
