lista = ["aa", "bb", "tt", "dd", "aa", "tt", "xx", "ww", "aa", "nn"]

dicta = {"tt":2, "yy":6, "ee":8, "qq":10}

for i in dicta:
    print("i =", i)
    
print("-----")

for i in dicta.values():
    print("i =", i)
    
print("-----")

for k, v in dicta.items():
    print("k =", k, "v =", v)
    
