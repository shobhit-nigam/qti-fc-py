listy = [100, 203, 30, 67, 11, 10, 20]
listz = [200, 300, 77, 90, 10, 25]

def funca(y):
    return y%10 == 0


res_m = list(filter(funca, listy))
print(res_m)
