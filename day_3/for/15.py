lista = ["aa", "bb", "tt", "dd", "aa", "tt", "xx", "ww", "aa", "nn"]

# {"aa":3, "bb":1    ....}

letter_count = { }

for val in lista:
    if val not in letter_count:
        letter_count[val] = 1
    else:
        letter_count[val] = letter_count[val] + 1

print(letter_count)
    
