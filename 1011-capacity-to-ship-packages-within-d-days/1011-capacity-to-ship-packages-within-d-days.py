class Solution:
    def isvalid(self, weights, n, days,mid):
        weightSum = 0
        d=1
        for w in weights:
            if w>mid: return False
            if weightSum + w <= mid:
                weightSum += w
            else: #when sum exceeds our value the move that weight to next day
                weightSum = w
                d+=1
        if d<=days:
            return True 
        else: False
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        n = len(weights)
        l = weights[0]
        h = sum(weights)
        while(l<=h):
            mid = (l+h)//2
            #this mid is weight 

            if self.isvalid(weights,n,days,mid):
                h = mid-1
            else: l = mid+1
        return l
        