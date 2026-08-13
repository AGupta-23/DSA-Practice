class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        count0,count1,count2=0,0,0
        #traversal
        for i in range(0,n):
            if nums[i]==0: count0+=1
            elif nums[i]==1: count1+=1
            else: count2+=1

        inx=0

        for i in range(0,count0):
            nums[inx]=0
            inx+=1
        for i in range(0,count1):
            nums[inx]=1
            inx+=1
        for i in range(0,count2):
            nums[inx]=2
            inx+=1

