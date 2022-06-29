avengers = ["ironman", "captain", "wanda", "hawk eye"]
marvel = ["wolverine", "magneto"]
print("avengers =", avengers)

avengers.append(marvel)
print("after appending")
print("avengers =", avengers)

#####################
print("----------------")
avengers = ["ironman", "captain", "wanda", "hawk eye"]
marvel = ["wolverine", "magneto"]
print("avengers =", avengers)

avengers.extend(marvel)
print("after extending")
print("avengers =", avengers)
