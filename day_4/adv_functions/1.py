listy = [100, 200, 30, 67, 0, 10, 20]
listz = [200, 300, 70, 90, 10, 25]

def funca(y, z):
    return y*2 + z -20

res = []

if len(listy) < len(listz):
    for i in range(len(listy)):
        res.append(funca(listy[i], listz[i]))
else:
    for i in range(len(listz)):
        res.append(funca(listy[i], listz[i]))

print(res)

res_m = list(map(funca, listy, listz))
print(res_m)
