with open('input', 'r') as f:
    input = f.read()

DIGITS = 'one, two, three, four, five, six, seven, eight, nine'.split(', ')
result = []
MAPPING = {digit: str(i) for i, digit in enumerate(DIGITS, 1)}
DIGITS.sort(key=len, reverse=True)
MAPPING = {digit: MAPPING[digit] for digit in DIGITS}
for line in input.splitlines():
    first_word = ""
    for char in line:
        if char.isdigit():
            first = char
            break
        else:
            first_word += char
        got = False
        for d in DIGITS:
            if d in first_word:
                first = MAPPING[d]
                got = True
                break
        if got:
            break
    last_word = ""
    for char in line[::-1]:
        if char.isdigit():
            last = char
            break
        else:
            last_word = char + last_word
        got = False
        for d in DIGITS:
            # if any(d in last_word for d in DIGITS):
            if d in last_word:
                last = MAPPING[d]
                got = True
                break
        if got:
            break
    ans = f"{first}{last}"
    print(ans)
    result.append(int(ans))

print(sum(result))
