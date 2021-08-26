results = []
for x in range(2000):
    a = 2803 + x / 5
    b = 2655 - x
    s = sum(int(c) for c in f"{a}{b}".replace(".", ""))
    if s == 19:
        results.append(x)

print(results)
