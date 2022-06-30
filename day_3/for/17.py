lista = ["aa", "bb", "tt", "dd", "aa", "tt", "xx", "ww", "aa", "nn"]

# {"aa":[0, 4, 8], "bb":[1]    ....}

# dictionary 
letter_count = { }

for i in range(len(lista)):
    if lista[i] not in letter_count:
        letter_count[lista[i]] = [i]        
    else:
        letter_count[lista[i]].append(i)

print(letter_count)

