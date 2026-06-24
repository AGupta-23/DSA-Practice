# Check if array is sorted or not?

nums=[1,2,3,4,5,6,7]
n= len(nums)
for i in range(0,n-1):
    if nums[i]>nums[i+1]:
        print("False")
else:
 print("True")

nums=[1,2,6,4,5,6,7]
n= len(nums)
for i in range(0,n-1):
    if nums[i]>nums[i+1]:
        print("False")
        break
else:
 print("True")

#  Run the else block only if the for loop finishes normally (without break)