#User function Template for python3

class Solution:
    def findLargest(self, N, S):
        if N == 1 and S == 0:
            return "0"
        
        if N > 1 and S == 0:
            return "-1"
        
        ans = ""
        while N > 0:
            if S >= 9:
                ans += "9"
                S -= 9
            else:
                ans += str(S)
                S -= S
            N -= 1
        
        if S == 0:
            return ans
        
        return "-1"
            
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, S = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.findLargest(N, S))
# } Driver Code Ends