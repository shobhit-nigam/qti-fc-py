listy = [100, 200, 30, 67, 0, 10, 20]
listz = [200, 300, 70, 90, 10, 25]

res_m = list(map(lambda y, z: y*2 + z -20, listy, listz))
print(res_m)
res_m = list(map(lambda y, z: y if y > z else z, listy, listz))
print(res_m)

