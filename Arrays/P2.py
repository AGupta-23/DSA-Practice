# Array Reverse
# Reverse an array arr[]. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on.
# Examples:

# Input: arr[] = [1, 4, 3, 2, 6, 5]  
# Output:  [5, 6, 2, 3, 4, 1]
# Explanation: The first element 1 moves to last position, the second element 4 moves to second-last and so on.

# Input: arr[] = [4, 5, 1, 2]
# Output: [2, 1, 5, 4]
# Explanation: The first element 4 moves to last position, the second element 5 moves to second last and so on.

# Let's use 2 pointer approach -- TC =O(n), SC=O(0)

def func(A):
    left=0
    right=len(A)-1

    while(left<right):
        A[left],A[right]=A[right],A[left]
        left+=1
        right-=1
    return A
    
if __name__=="__main__":
    A=[1,2,3,4,5,6,7]
    print(func(A))