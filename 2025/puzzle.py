from itertools import permutations


conditions_str = [
    "J x H = P + R",
    "W - K = N",
    "S + J = P - Y",
    "O + X = V",
    "K x R = M",
    "Q > T",
    "O > I",
    "G + L = E + Z",
    "S x K = Z + E",
    "D + U = Z + E",
    "A x A = L + G",
    "D + U = R + P",
    "G x F = D + U",
    "E x C = Z x B",
    "C x C = U",
]


def find_heads(heads, conditions_str):
    cond_str = conditions_str.pop()
    python_str = cond_str.replace("x", "*").replace("=", "==")
    cond = compile(python_str, "<string>", "eval")
    new_heads = []
    print(len(heads), cond_str)
    for head in heads:
        letters = {c for c in cond_str if 65 <= ord(c) <= 90 if c not in head}
        numbers = [i for i in range(1, 27) if i not in head.values()]
        for n in permutations(numbers, len(letters)):
            locs = {k: v for k, v in zip(letters, n)}
            locs.update(head)
            if eval(cond, locals=locs):
                new_heads.append(locs)

    if len(conditions_str) == 0:
        return new_heads
    else:
        return find_heads(new_heads, conditions_str)


print(find_heads(({},), conditions_str))
