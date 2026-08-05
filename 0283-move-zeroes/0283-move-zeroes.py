class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        n = len(nums)  #takes len of original array
        temp = []      #creates an extra array 

        for i in range(0,n):
            if nums[i] != 0:
                temp.append(nums[i])   #0(n)--> 1 traversal
        
        n2 = len(temp)

        for i in range(0,n2):
            nums[i] = temp[i]

        for j in range(n2,n):
            nums[j] = 0

        # return nums

        