#User function Template for python3

class Solution:
	def pushZerosToEnd(self,nums, n):
	    j=0
	    for i in range(n):
	        if nums[i]!=0:
	            nums[j], nums[i] = nums[i], nums[j]
	            j+=1
	    
    	# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends