# Find the Largest in the array 

nums= [1,2,3,4,5,6,9]

largest= float("-inf")

for i in range(0,len(nums)):
    largest = max (largest, nums[i])
print(largest)