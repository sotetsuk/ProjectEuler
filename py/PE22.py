path_to_txt = 'txt/22.txt'

s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

names = []
for line in open(path_to_txt):
    names += [x[1:-1] for x in line.split(",")]

names.sort()

score = 0
for i, name in enumerate(names):
    tmp = 0
    for c in name:
        tmp += s.find(c)+1
    score += (i + 1) * tmp

print score
