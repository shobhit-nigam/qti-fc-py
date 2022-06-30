fa = open("two.txt", "w")
fa.write("some data into the file\n")
fa.write("some more data")

print(fa.tell())
fa.close()
