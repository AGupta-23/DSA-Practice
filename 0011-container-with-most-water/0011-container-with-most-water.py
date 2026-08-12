class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l=0
        r=n-1
        maxArea=0

        while(l<r):
            h = min(height[r], height[l])
            w = r-l
            area = h*w
            maxArea=max(area, maxArea)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxArea
