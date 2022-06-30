with open("three.txt", "r") as fa:
    stra = fa.read()

lista = stra.splitlines()

list_col_2 = []

for line in lista:
    list_col_2.append(int(line.split()[1]))

print(list_col_2)
