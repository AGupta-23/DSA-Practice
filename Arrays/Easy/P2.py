# Find the 2nd largest element in an array without sorting

nums = [55,32,97,-55,45,32,88,21,97,89] 

largest = float("-inf")
s_largest = float("-inf")

for i in range (0,len(nums)):

    if nums[i]>largest:
        s_largest=largest
        largest=nums[i]

    elif (nums[i] != largest and nums[i]> s_largest):
        s_largest= nums[i]

print(s_largest)