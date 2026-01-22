# Condition Statement , simple if else
env = input("Enter the environemnt  : ")
print("The environment is :" , env)
if env == "Production" :
    print("Don't Deploy on Friday")
elif env == "Staging" :
    print("Take Backupb & Test well")
else :
    print("Safe to Deploy any Day ")