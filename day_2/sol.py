with open('input', 'r') as f:
    input = f.read()

# only 12 red cubes, 13 green cubes, and 14 blue cubes
MAX_COUNT = {'red': 12, 'green': 13, 'blue': 14}
result = []
for line in input.splitlines():
    game_id, line = line.split(':')
    sets = line.split(';')
    valid = True
    for game_set in sets:
        colors_count_dict = {
            color.split()[1]: int(color.split()[0])
            for color in game_set.split(',')
        }
        invalid_sets = {
            color: int(count)
            for color, count in colors_count_dict.items()
            if MAX_COUNT[color.strip()] < count
        }
        if invalid_sets:
            valid = False
            break
    if valid:
        result.append(int(game_id.replace('Game ', '')))
print(sum(result))
