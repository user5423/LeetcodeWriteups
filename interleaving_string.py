class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.memoization = {} ## key: (first, second), value = true/false
        return self.recurse()
        
    def recurse(self, firstIndex=0, secondIndex=0, thirdIndex=0):
        ## Base case
        if thirdIndex == len(self.s3):
            self.memoization[(firstIndex, secondIndex,)] = True
            return True
        
        ## Recursive case
        try:
            result = self.memoization.get((firstIndex+1, secondIndex,))
            if result is None:
                if self.s1[firstIndex] == self.s3[thirdIndex]:
                    result = self.recurse(firstIndex+1, secondIndex, thirdIndex+1)
                    self.memoization[(firstIndex+1, secondIndex,)] = result
            if result is True:
                return True
        except IndexError:
            pass
        
        try:
            result = self.memoization.get((firstIndex, secondIndex+1,))
            if result is None:
                if self.s2[secondIndex] == self.s3[thirdIndex]:
                    result = self.recurse(firstIndex, secondIndex+1, thirdIndex+1)
                    self.memoization[(firstIndex, secondIndex+1,)] = result
            if result is True:
                return True
        except IndexError:
            pass
        
        return False
        
        
