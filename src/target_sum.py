class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.dp = {}
        self.nums = nums
        self.target = target
        return self.solutionOne()
        
    def solutionOne(self, currentIndex: int = 0, runningSum: int = 0) -> int:
        ## Base case
        if currentIndex == len(self.nums):
            return runningSum == self.target
        
        ## We select the current element and try both ways
        currentNum = self.nums[currentIndex]
        output = 0

        ## We then recurse on the plus route
        plusTuple = (currentIndex+1,runningSum+currentNum)
        out = self.dp.get(plusTuple)
        if out is None:
            out = self.solutionOne(currentIndex+1, runningSum+currentNum)
            self.dp[plusTuple] = out
        output += out

        ## And recurse on the minus route
        minusTuple = (currentIndex+1, runningSum-currentNum)
        out = self.dp.get(minusTuple)
        if out is None:
            out = self.solutionOne(currentIndex+1, runningSum-currentNum)
            self.dp[minusTuple] = out
        output += out
        
        return output
