varx = 11
vary = 99
varz = "hello"
print("id of varx=", id(varx))
print("id of vary=", id(vary))
print("id of varz=", id(varz))
# some code

varx = 33
varw = 99
print("after value changes")
print("id of varx=", id(varx))
print("id of vary=", id(vary))
print("id of varz=", id(varz))
print("id of varw=", id(varw))



