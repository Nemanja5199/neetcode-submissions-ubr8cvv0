class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:




        for row in matrix:

            if target > max(row):
                continue
            elif target == max(row) or target == min(row):
                return True
            else:
                l=0
                r= len(row)-1
                
                while l<= r:

                    mid = l+ (r-l) //2

                    if row[mid]== target:
                        return True
                    elif target < row[mid]:
                        r= mid -1
                    elif target > row[mid]:
                        l= mid + 1
        return False


            


        