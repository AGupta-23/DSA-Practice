#Extraction of digits using loops
# 54321

n=54321

while(n>0):
    last_digit=n%10
    print(last_digit, end =" ")
    n=n//10
