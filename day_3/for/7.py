lista = ["aa", "bb", "tt", "dd", "aa", "tt", "xx", "ww", "aa", "nn"]

dicta = {"tt":[10, 30, 50], "yy":6, "ee":[8, 9], "qq":10}

for k, v in dicta.items():
    print("k =", k)
    if type(v) is list:
        for val in v:
            print("\tvalue is", val)
    else:
        print("\tvalue is", v)
    
    
