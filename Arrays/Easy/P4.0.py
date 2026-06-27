# Remove duplicates from sorted array (in place)

# Brute Force

nums= [1,1,1,2,3,44,7,9,9,9,10]

n= len(nums)
freq_map={}

for i in range(0,n):
    freq_map[nums[i]]=0

j=0
for key in freq_map:
    nums[j]=key
    j+=1

print(j)