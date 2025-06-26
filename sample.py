class Family:
    lastname = "김"

a = Family()
print(a.lastname)
print(Family.lastname)

Family.lastname = "박"
print(a.lastname)
print(Family.lastname)
