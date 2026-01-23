info = {
    "name" : "Aditya Tomar", #string
    "city" : "Gwalior", # string
    "age" : 21, # int
    "married" : False , # bool
    "weight" : 62.400 # float
}
print(info)

# .update() -> to update the dictonary
info.update({"gender" : "male"})
print(info)

print("I live in " ,info["city"])
print("my age ", info.get("Age")) # output == my age none
print("my age ", info.get("Age", "Not found")) # output == my age not found 

# iterarte
for i in info:
    print(i) # output == only keys

for i in info.items():
    print(i) # output == key and value