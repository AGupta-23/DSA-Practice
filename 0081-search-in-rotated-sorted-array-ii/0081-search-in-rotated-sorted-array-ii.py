class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        l,h=0, len(nums)-1

        while(l<=h):
            mid = (l+h)//2

            if nums[mid] == target: return True

            if nums[l] == nums[mid] == nums[h]:
                l+=1
                h-=1
                continue
            
            elif (nums[l] <= nums[mid]):
                # means left side is sorted
                if (nums[l]<= target < nums[mid]):
                    # target lies here in left part which is sorted
                    h = mid - 1
                else:
                    #target not found in sorted half
                    l = mid + 1
            
            else:
                # right half is sorted
                if (nums[mid]<target<=nums[h]):
                    l = mid+1
                else: 
                    h = mid - 1

        return False
                
