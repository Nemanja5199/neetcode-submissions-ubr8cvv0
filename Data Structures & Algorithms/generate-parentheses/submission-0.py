class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        leftCount = n
        rightCount = n

        res = []
        def dfs(left,right,curr):

            if left == 0 and right ==0:
                res.append(curr)
                return
            
            if left > 0 : 
                dfs(left-1,right,curr + '(')
            
            if right > left:
    
                dfs(left,right-1,curr + ')')

        dfs(n,n,"")  
        return res

            

            





        
        