#User function Template for python3

class Solution:
    def rotate(self, N, D):
        D=D%16
        binary_str = format(N, '016b')
        leftrot = int((binary_str[D:] + binary_str[:D]),2)
        rightrot = int((binary_str[-D:]+binary_str[:-D]),2)
        return leftrot,rightrot


        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, d = input().strip().split(" ")
        n, d = int(n), int(d)
        ob = Solution()
        ans = ob.rotate(n, d)
        print(ans[0])
        print(ans[1])
# } Driver Code Ends