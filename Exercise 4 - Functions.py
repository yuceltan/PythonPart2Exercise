def greet(name, surname):
    print(f"Hello {name} {surname}!")

family_name=["John", "Tristram", "Baldwin", "Wally"]
family_surname=["Doe", "Mcbride", "Preston", "Collins"]

output = "\n".join(greet(x,y) for x,y in zip(family_name, family_surname))

print(output)