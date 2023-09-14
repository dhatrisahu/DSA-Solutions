#User function Template for python3
class Solution:
    def perfectSum(self, arr, n, total):
        mod = 10**9 + 7

        def f(i, total, memo):
            if i == n:
                if total == 0:
                    return 1
                else:
                    return 0

            if memo[i][total] != -1:
                return memo[i][total]

            pick = 0
            notPick = 0

            if arr[i] <= total:
                pick = f(i + 1, total - arr[i], memo)

            notPick = f(i + 1, total, memo)

            memo[i][total] = (pick % mod + notPick % mod) % mod
            return memo[i][total]

        memo = [[-1 for _ in range(total + 1)] for _ in range(n)]
        return f(0, total, memo)





    
	    
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends