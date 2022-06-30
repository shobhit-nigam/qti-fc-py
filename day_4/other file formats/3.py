import json

with open("example_2.json", "r") as objf:
    data = json.load(objf)

def read_dict(d):
    for k, v in d.items():
        if type(v) is dict:
            read_dict(v)
        else:
            print(k)
            print(v)
        print("--------")

data = [30, 20, 40]

try:
    read_dict(data)
except AttributeError:
    print("should have passed a dictionary")
except:
    print("handles everything")

print("code continues ...")
