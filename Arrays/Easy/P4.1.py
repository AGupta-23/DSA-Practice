# Remove duplicates from sorted array (in place)

# Optimal Approach --> 2 pointer

nums= [1,1,1,2,3,44,7,9,9,9,10]

n= len(nums)

if n==1:
    print("1")

i=0
j=i+1
while j<n:
    if nums[j]!=nums[i]:
        i+=1
    #swap
        nums[i],nums[j]=nums[j],nums[i]
    j+=1

print(i+1)

