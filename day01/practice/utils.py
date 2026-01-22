import os # import a library into code

# to check the disk space in system
#print(os.system('df -h'))
print(os.system('wmic logicaldisk get size,freespace,caption'))
print(os.system("wmic computersystem get totalphysicalmemory"))
#print(os.system("(Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime"))