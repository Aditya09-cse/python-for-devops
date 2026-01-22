def op_of_num() : # function defination
    env = input("Enter the Environment :" )
    print("The user input is : " , env)
    if env == "production": # conditional statement , 
        for i in range(4) : # loop ,  if conditon == true , then loop execute 4 times
            num1 = int(input("Enter num1 : " ))
            num2 = int(input("Enter num2 : " ))
            sum = num1 + num2
            print("The sum of num1 + num2 : " , sum)
    #elif env == "staging":
    #    num1 = int(input("Enter num1 : " ))
    #    num2 = int(input("Enter num2 : " ))
    #    Subtract  = num1 - num2
    #    print("Subtarction of num 1 - num2 = " , Subtract)
op_of_num() # function calling