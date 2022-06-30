ga = 100

def funca():
    global ga
    ga = 33
    print("inside ga =", ga)

print("outside ga =", ga)
funca()
print("outside ga =", ga)


