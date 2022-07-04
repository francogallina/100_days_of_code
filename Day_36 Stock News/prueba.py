d = {1:2, 3:4, 5:6, 7:8}
l = [0,2]
n = {key: d[key] for key in d.keys() & l}
print(n)