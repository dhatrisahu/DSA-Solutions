#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,N):
        if N == 0:
            return 0

        position = 1
        while N > 0:
        # Check if the least significant bit is set (i.e., it's 1)
            if N & 1:
                return position
        # Right shift N to check the next bit
            N >>= 1
            position += 1
    
        return 0
        
        #Your code here

#{ 
 # Driver Code Starts.
    
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        
        print(ob.getFirstSetBit(n))
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
# } Driver Code Ends