print("This is used to fetch the details of the person in the dictionary")
person = {"name" : "John",  "gender" : "Male", "address" : "Somewhere", "Phone_number" : "12345"}
key = input("What would you like to know(name,gender,address,Phone_number): ").lower()
print(person.get("key","invalid property"))
