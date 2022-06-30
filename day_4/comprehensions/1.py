listy = [100, 200, 30, 67, 0, 10, 20]
listz = [200, 300, 70, 90, 10, 25]

res = []
for x in listy:
    if x%10 ==0:
        res.append(x)

res_m = [x for x in listy if x%10 ==0]
