sols = []


def langford(remain, sofar):
    try:
        c = sofar[-1]
        idx = sofar[:-1].index(c)
        if len(sofar) - idx - 2 != c:
            return
    except ValueError:
        pass
    except IndexError:
        pass
    if sum(remain.values()) == 0:
        sols.append(sofar)
        print("found sol", sofar)
    else:
        for k, v in remain.items():
            if v != 0:
                remain_i = remain.copy()
                remain_i[k] -= 1
                langford(remain_i, sofar + (k,))

n = 8
remain = dict((i, 2) for i in range(1, n + 1))

langford(remain, ())

for sol in sols:
    print(sol, '\n')
print(len(sols), '\n')
