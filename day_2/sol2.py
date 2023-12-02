from collections import defaultdict
with open('input2', 'r') as f:
    input = f.read()

# only 12 red cubes, 13 green cubes, and 14 blue cubes
MAX_COUNT = {'red': 12, 'green': 13, 'blue': 14}
result = []
for line in input.splitlines():
    game_id, line = line.split(':')
    sets = line.split(';')
    valid = True
    max_color_count = defaultdict(int)
    for game_set in sets:
        colors_count_dict = {
            color.split()[1]: int(color.split()[0])
            for color in game_set.split(',')
        }
        for color, count in colors_count_dict.items():
            if max_color_count[color] < count:
                max_color_count[color] = count
    values = list(max_color_count.values())
    if values:
        ans = 1
        for value in values:
            ans *= value
        result.append(ans)
print(sum(result))
