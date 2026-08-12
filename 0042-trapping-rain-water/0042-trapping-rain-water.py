class Solution:
    def trap(self, height):
        n = len(height)
        water = 0

        left=0
        right=n-1

        left_max=height[0]
        right_max=height[n-1]

        while(left<right):
            if left_max<=right_max:
                left+=1
                left_max=max(left_max,height[left])
                water += left_max - height[left]
            else:
                right-=1
                right_max = max(right_max,height[right])
                water += right_max - height[right]
        return water