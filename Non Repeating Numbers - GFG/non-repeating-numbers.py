#User function Template for python3

class Solution:
	def singleNumber(self, nums):
	    xor_result = 0
        for num in nums:
            xor_result ^= num
        
        differing_bit = 1
        while (differing_bit & xor_result) == 0:
            differing_bit <<= 1
        
        num1, num2 = 0, 0
        for num in nums:
            if num & differing_bit:
                num1 ^= num
            else:
                num2 ^= num
        
        return [min(num1, num2), max(num1, num2)]
	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends