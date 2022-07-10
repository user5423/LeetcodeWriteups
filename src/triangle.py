class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        if len(triangle) == 1:
            return triangle[0][0]
        
        solutions = triangle[-1]
        newSolutions = []
        
        for rowIndex in range(len(triangle)-2, -1, -1):
            ## find the best row
            for colIndex in range(rowIndex+1):
                newSolutions.append(triangle[rowIndex][colIndex] + min(solutions[colIndex], solutions[min(rowIndex+1, colIndex+1)]))
                
            solutions = newSolutions
            newSolutions = []
            
        return solutions[0]
