#User function Template for python3
import sys
class Solution:
    def minimumNumber(self, n, arr):
        min_value = sys.maxsize

        for i in range(n):
            if arr[i] % 2 != 0:
                return 1
            min_value = min(min_value, arr[i])

        return min_value
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        arr=[int(i) for i in input().split()]
        obj=Solution()
        print(obj.minimumNumber(n,arr))
# } Driver Code Ends