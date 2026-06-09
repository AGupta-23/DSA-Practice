# Maximum and minimum of an array using minimum number of comparisons
# Given an array of integers arr[], the task is to find the maximum and minimum elements in the array using the minimum number of comparisons.

# Examples:

# Input: arr[] = [3, 5, 4, 1, 9]
# Output: [1, 9]
# Explanation: The minimum element is 1, and the maximum element is 9.

# Input: arr[] = [22, 14, 8, 17, 35, 3]
# Output: [3, 35] 
# Explanation: The minimum element is 3, and the maximum element is 35.

# Optimal approach --> TC=O(n), SC=O(1)

A=[34,26,1,76,8,9,12]
n=len(A)
i=0

if n==1:
    min1=A[0]
    max1=A[0]

if n%2==0:
    #Even - 2 pairs each 
    if A[0]>A[1]:
        max1=A[0]
        min1=A[1]
    else:
        max1=A[1]
        min1=A[0]
    i+=2
else:
    #Odd number of literals
    min1=A[0]
    max1=A[0]
    i+=1

while(i<n-1):
    if A[i]>A[i+1]:
        if A[i]>max1:
            max1=A[i]
        if A[i+1]<min1:
            min1=A[i+1]
    else:
        if A[i+1]>max1:
            max1=A[i+1]
        if A[i]<min1:
            min1=A[i]
    i+=2

print([max1,min1])
