listx = ["aa", "bb", "dd", "tt", "ss"]

try:
    i = int(input("\n"))
    print(listx[i])
except IndexError:
    print("should have passed a valid index, defaulting it to zero")
else:
    print('else block')
finally:
    print("finally block always executes")

print("code continues ...")
