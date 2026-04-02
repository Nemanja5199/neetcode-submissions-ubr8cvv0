class Solution:
    def trap(self, height: List[int]) -> int:


        l = 0
        r = len(height)-1
        
        max_left=[0] * len(height)
        max_right= [0] * len(height)

        maxLeftValue=0
        for i,num in enumerate(height):

            if num > maxLeftValue:
             maxLeftValue = num
             max_left[i]= maxLeftValue
            else:
                max_left[i]= maxLeftValue
        
        maxRightValue=0
        for i in range(len(height)-1, -1, -1):
            
            num = height[i]

            if num >= maxRightValue:
             max_right[i]= num
             maxRightValue = num
            else:
                max_right[i]=maxRightValue
        
        total =0

        for i in range(len(height)):
             value= min(max_left[i],max_right[i]) - height[i]
             if value > 0:
                total+=value
            
           
        
        return total





      









        