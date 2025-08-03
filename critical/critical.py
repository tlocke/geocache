from itertools import permutations


def sum_word(pdict, word):
    return sum(pdict[c] for c in word)


word_totals = (
    ("niagara", 39),
    ("track", 21),
    ("chalk", 16),
    ("king", 19),
    ("grin", 27),
    ("chain", 26),
    ("cart", 20),
    ("grant", 30),
    ("halt", 12),
)
start = set("criticalthinking")
print(start)
for perm in permutations(start):
    print(perm)
    pdict = {c: i for i, c in enumerate(perm)}
    if all(sum_word(pdict, word) == total for word, total in word_totals):
        print(f"found perm {pdict}")
        break
