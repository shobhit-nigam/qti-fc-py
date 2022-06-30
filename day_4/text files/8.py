def funca(name, col=0):
    with open(name, "r") as fa:
        stra = fa.read()
    lista = stra.splitlines()
    list_col = []

    for line in lista:
        list_col.append(line.split()[col-1])

    return list_col


