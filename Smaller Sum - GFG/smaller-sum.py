from typing import List
import bisect

class Solution:
    def smallerSum(self, n : int, arr : List[int]) -> List[int]:
        sum = [0] * n
        temp = arr.copy()
        temp.sort()
        sum[0] = temp[0]
        for i in range(1, n):
            sum[i] = sum[i-1] + temp[i]
    
        ans = [0] * n
        for i in range(n):
            ind = bisect.bisect_left(temp, arr[i])
            if ind != 0:
                ans[i] = sum[ind-1]
    
        return ans
            
        # code here
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.smallerSum(n, arr)
        
        IntArray().Print(res)
        

# } Driver Code Ends