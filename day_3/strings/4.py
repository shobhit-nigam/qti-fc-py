def funca(la, lb):
    """the function does.....
    pass two arguments
    does not return anything"""
    print("la =", la)
    print("lb =", lb)

def funcb(la):
    print("la =", la)
    pass

funca.__doc__ = "its an useless function"
print(funca.__doc__)
