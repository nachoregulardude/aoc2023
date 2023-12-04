from collections import defaultdict
with open('input', 'r') as f:
    input = f.read()

result = []
ans = defaultdict(int)
for line in input.splitlines():
    card_no, data = line.split(':')
    card_no = int(card_no.replace('Card ', ''))
    ans[card_no] += 1
    winning, have = data.split('|')
    winning = {int(x.strip()) for x in winning.split()}
    have = {int(x.strip()) for x in have.split()}
    win_num = winning.intersection(have)
    for x in range(len(win_num)):
        ans[card_no + 1 + x] += ans[card_no]

print(sum(ans.values()))
