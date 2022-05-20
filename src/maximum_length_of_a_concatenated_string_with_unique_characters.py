class Solution:
    def maxLength(self, arr: List[str]) -> int:
        return self.solution1(arr)

    def solution1(self, arr: List[str]) -> int:
        ## We preprocess the array to remove duplicates, and cast the str into sets
        self.arr = [set(substr) for substr in arr if len(substr) == len(set(substr))]
        
        ## If every string in arr has at least one internal common char, then we exit
        if len(self.arr) == 0:
            return 0
        
        self.bestLength = len(self.arr[0])
        self.bestSolution = self.arr[0]
        
        self._backtrackSolution()
        return self.bestLength
        
    
    def _backtrackSolution(self, currentSolution: Optional[set] = None, currentLength: int = 0, startIndex: int = 0) -> None:
        ## Setup the currentSolution set object for the first level call for "_backtrackSolution()"
        if currentSolution is None:
            currentSolution = set()
        
        ## base-case
        if startIndex >= len(self.arr):
            return None
        
        ## Main body
        charStrUsed = "".join(currentSolution)
        charSetUsed = set(charStrUsed)
        for i in range(startIndex, len(self.arr)):
            newSolution = charSetUsed | self.arr[i]
            uniqueLength = len(newSolution)
            commonLength = len(charSetUsed) + len(self.arr[i])
            
            if commonLength == uniqueLength:
                ## Check if the new length is better than previous backtrack calls
                if uniqueLength > self.bestLength:
                    self.bestLength = uniqueLength
                    self.bestSolution = newSolution

                self._backtrackSolution(newSolution, uniqueLength, i+1)
