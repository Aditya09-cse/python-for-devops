# set does not allow repetation of elements
# set is written inside {}

days = {"Saturay","Sunday", "Saturay","Sunday" }
print(days) 
print(type(days)) # output -> class 'set'

nums = [1,2,3,4,1,2,1,3,2,1,-4,4.6] # list
nums = list(set(nums)) # Deduplicate nums: convert to set to drop duplicates, then back to list
print(nums) # output -> no repetation of numbers