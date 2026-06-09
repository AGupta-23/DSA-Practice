# You are given a number n. You need to find the count of digits in n.

# For example, if n = 1234, the number of digits in 1234 is 4, so the answer would be 4.

# BRUTE - 
# class Solution:
def countDigits(n: int):
    count = 0 
    while(n>0):
        last_digit=n%10
        count+=1
        n=n//10
    return count
    
print(countDigits(1234))

#OPTIMAL
# from math import log10

# class Solution:
#     def countDigits(self, n: int) -> int:
#         return int(log10(n) + 1)