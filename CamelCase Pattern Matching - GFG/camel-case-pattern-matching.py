#User function Template for python3

class Solution:
    def CamelCase(self,N,D,P):
        fn=[]
        for x in D:
            ans=""
            for i in x:
                if i.isupper()==True:
                    ans+=i
                if P==ans[:len(P)]:
                    fn.append(x)
                    break
        if fn :
            return fn
        else:
            return [-1]
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Dictionary=list(map(str,input().split()))
        Pattern=input()
        ob=Solution()
        ans=ob.CamelCase(N,Dictionary,Pattern)
        ans.sort()
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends