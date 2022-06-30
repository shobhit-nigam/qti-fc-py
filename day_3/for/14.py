lista = ["aa", "bb", "tt", "dd", "aa", "tt", "xx", "ww", "aa", "nn"]

aa_count = [ ]

for i in range(len(lista)):
    if lista[i] == "aa":
        aa_count.append(i)

print(aa_count)
    
