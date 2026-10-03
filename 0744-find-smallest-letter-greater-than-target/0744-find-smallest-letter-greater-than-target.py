class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        n = len(letters)
        low = 0
        high = n-1
        ub = 0

        while(low<=high):
            mid = (low+high)//2

            if ord(letters[mid]) > ord(target):
                ub = mid
                high = mid - 1
            else:
                low = mid+1
        return letters[ub]



        