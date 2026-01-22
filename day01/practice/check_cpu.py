# aapko kaam karo hai user se cpu threshold lo
# current cpu usage pata karo
# Email to user if cpu threshold is less than cpu usage 
# 3 baar chalao

import psutil # import psutil from pypi
def check_cpu_threshold() : # function defination
    for i in range(3) :     # to execute this function 3 times 
        user_cpu_threshold= int(input("Enter The CPU Threshold : " ))
        current_cpu = psutil.cpu_percent(interval=1)
        print("Current cpu % : " , current_cpu)
        if user_cpu_threshold < current_cpu : # condition
            print("CPU Alert Email sent ...")
        else :
            print("CPU in safe state ")
check_cpu_threshold()