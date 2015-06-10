'''
"St Cys" is coordinates 72966 East 98880 North  units are 1m

St MArtins is at 73560, 96111

St James is at 75676, 98108

The target location is

1596 m closer to St Martin’s than it is to St Cyr’s
2233 m closer to St James’ than it is to St Cyr’s.
'''
from random import randint

cyr = (72966, 98880)
mart = (73560, 96111)
james = (75676, 98108)

points = (cyr, mart, james)


def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

max_x = max(p[0] for p in points)
min_x = min(p[0] for p in points)
max_y = max(p[1] for p in points)
min_y = min(p[1] for p in points)

error = None
point = cyr


for x in range(100000):
    p = (point[0] + randint(-1, 1), point[1] + randint(-1, 1))
    dist_cyr = dist(p, cyr)
    dist_mart = dist(p, mart)
    dist_james = dist(p, james)
    err1 = dist_cyr - dist_mart - 1596
    err2 = dist_cyr - dist_james - 2233
    err = err1 ** 2 + err2 ** 2
    print("looking at point", p, "err", err, "point", point)
    if error is None or err < error:
        print("error", error)
        error = err
        point = p

'''
for x in range(10000001):
    p = (randint(min_x, max_x), randint(min_y, max_y))
    # print("looking at point", p)
    dist_cyr = dist(p, cyr)
    dist_mart = dist(p, mart)
    dist_james = dist(p, james)
    err1 = dist_cyr - dist_mart - 1596
    err2 = dist_cyr - dist_james - 2233
    err = err1 ** 2 + err2 ** 2
    if err < error:
        print("error", error)
        error = err
        best_point = p
'''
print("best point", point)
