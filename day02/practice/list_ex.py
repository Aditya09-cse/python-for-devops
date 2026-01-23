clouds = ['aws','gcp', 'alibaba', 'ibm', 'utho'] # first way of creating a list
print(clouds)


#clouds = list()  # second way of creating a list
#print(type(clouds))

# use append to item at last of list
clouds.append("salesforce")
print(clouds)

# access item of list using negative indexing
print(clouds[-1])

# insert item at any specific location
clouds.insert(2,"azure")
print(clouds)

# len() to get length of list
print("The lengh of list is :",len(clouds))

#The .count() method is used to find out how many times a specific value appears in a list
print(clouds.count('aws'))

# dir() -> to see the directory of list , what operations we perform on list
print(dir(clouds))

# __doc__-> to access the documentation string
print(clouds.append.__doc__)
print(clouds.insert.__doc__)

# using for loop print items of list
#for clouds in clouds:
 #   print(clouds)

# using for loop and conditional statement
for cloud in clouds:
    if cloud == "aws":
        print("Worlds largest cloud provider :", cloud)
    elif cloud == "utho":
        print("india's their own cloud :", cloud)
    elif cloud == "gcp" or cloud == 'azure' or cloud == 'ibm' or cloud == 'salesforce' or cloud == 'alibaba' :
        print("Other cloud provider")
    else :
        print("Error")