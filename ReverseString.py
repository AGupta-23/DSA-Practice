def reverseArr(arr):

    #Brute approach
    # n= len(arr)
    # temp=[0]* n
    # for i in range(n):
    #     temp[i]=arr[n-1-i]
    # for i in range(n):
    #     arr[i]=temp[i]

    # 2 POINTER SWAP
    L=0
    R=len(arr)-1

    while L<R:
        arr[L],arr[R]=arr[R],arr[L]
        L=L+1
        R=R-1

    # TEMP SWAP -- Traverse only till n//2
    # n=len(arr)
    # for i in range(n//2):
    #     temp=arr[i]
    #     arr[i]=arr[n-1-i]
    #     arr[n-1-i]=temp

    # in build method
    # arr.reverse()

if __name__=="__main__":

    arr=[1,2,3,4,5]

    reverseArr(arr)

    for i in range (len(arr)):
        print(arr[i], end=" ")


