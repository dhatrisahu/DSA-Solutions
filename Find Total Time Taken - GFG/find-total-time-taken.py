from typing import List


class Solution:
    def totalTime(self, n : int, arr : List[int], time : List[int]) -> int:
        last_pick_time = {}
        total_time = 0
    
        for i in range(n):
            if arr[i] not in last_pick_time:
                total_time += 1
                last_pick_time[arr[i]] = i
            else:
                total_time += time[arr[i]-1]
                last_pick_time[arr[i]] = i
    
        return total_time - 1
            
        
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
        
        
        time=IntArray().Input(n)
        
        obj = Solution()
        res = obj.totalTime(n, arr, time)
        
        print(res)
        

# } Driver Code Ends