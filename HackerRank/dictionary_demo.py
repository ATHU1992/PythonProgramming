customer = {
    "name": "Atharva Kekare",
    "age": 28,
    "is_programmer": True
}

print(customer.get("name"))
print(customer.get("age"))
print(customer)

customer["birthdate"] = "Aug 13th 1992"
print(customer)
