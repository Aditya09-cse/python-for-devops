# list -> data structure which can hold the multiple values of multiple type
list_of_sem = ["sem3" , "sem4"]
print("list :" ,list_of_sem)

list_of_sem.append("sem5") # add item at the end of list
print("insert element at last of list :" , list_of_sem)

list_of_sem.insert(1,"sem2") # add item at any specific location
print("insert element at 1th index :" ,list_of_sem)

print(len(list_of_sem)) # to know the lenght of our list

# insert at 0th index
list_of_sem.insert(0, "sem1")
print("insert element at 0th index :" , list_of_sem)


# iteration of list
for sem in list_of_sem :
    print(sem)






'''
# condition for sem's
for sem in list_of_sem :
    if sem == "sem1" :
        print("pass first sem without backlog")
    elif sem == "sem2" :
       print("pass second sem without backlog")
    elif sem == "sem3" :
        print("pass third sem without backlog")
    elif sem == "sem4" :
       print("pass fourth sem without backlog")
    elif sem == "sem5"  :
       print("Result not declared")
    else :
       print("sem6 to be started soon")
'''