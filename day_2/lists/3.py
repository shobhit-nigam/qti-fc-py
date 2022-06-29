avengers = ["ironman", "captain", "wanda", "hawk eye"]
marvel = ["wolverine", "magneto", avengers.copy()]
print("avengers =", avengers)
print("marvel =", marvel)

avengers.insert(2, "thor")
avengers.append("hulk")
print("after changes to avengers")
print("avengers =", avengers)
print("marvel =", marvel)

