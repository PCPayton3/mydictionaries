person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

# The name of the second child
print(person.get('children')[1])
print(person["children"][1])

# The name of the cat
print(type(person["pets"]))
print(person["pets"]["cat"])

# use a for loop to list each child
for i in person["children"]:
    print(i)

for i, j in person['pets'].items():
    print(f"Type of pet: {i} bame of pet: {j}")
