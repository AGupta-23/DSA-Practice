class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        maxi=0
        right,left=0,0
        count={}

        for right in range(0,n):
            count[fruits[right]]=count.get(fruits[right],0) + 1

            if len(count)>2:
                while len(count)>2:
                    count[fruits[left]]-=1
                    if count[fruits[left]]==0:
                        del count[fruits[left]]
                    left+=1
            if len(count)<=2:
                maxi=max(maxi, right-left+1)

        return maxi

                
        