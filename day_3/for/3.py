lista = ["aa", "bb", "tt", "dd", "aa", "tt", "xx", "ww", "aa", "nn"]

for val in lista:
    if val == "yy":
        print("found it")
        break
else:
    print("did not find it")
