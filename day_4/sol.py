with open('input', 'r') as f:
    input = f.read()

result = []
for line in input.splitlines():
    data = line.split(':')[1]
    winning, have = data.split('|')
    winning = {int(x.strip()) for x in winning.split()}
    have = {int(x.strip()) for x in have.split()}
    win_num = winning.intersection(have)

    ans = 1
    for win in list(win_num)[1:]:
        ans = ans * 2
    if win_num:
        result.append(ans)

print(result)
print(sum(result))
