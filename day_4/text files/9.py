def funca(name, new_name, sw):
    with open(name, "r") as fa:
        lista = fa.readlines()

    fb = open(new_name, "w")
    counter = 0
    for line in lista:
        if line.startswith(sw):
            fb.write(line)
            counter = counter + 1
    fb.close()
    print(f"finished updating, written {counter} lines\nchechk {new_name} for data")


