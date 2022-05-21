class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ## We have an array
        ## - ascending order
        
        ## We need to
        ## - remove duplicates in-place
        ## - such that each unique element appears at most twice
        ## - reliatve order of elements should be the same
        # return self.solution1(nums)
        return self.solution2(nums)

        
    def solution1(self, nums: List[int]) -> int:
        ## Perform two passes
        ## Pass 1:
        ## - we keep a counter of the previous elements
        ## - if it surpasses 2 then we set it to None
        ## - if a new element is found we set the counter to 0
        previousValue = None
        previousCounter = 0
        for i in range(len(nums)):
            currentValue = nums[i]
            if currentValue != previousValue:
                previousValue = currentValue
                previousCounter = 1
            elif currentValue == previousValue:
                previousCounter += 1
                
            if previousCounter > 2:
                nums[i] = None
                
        ## Pass 2:
        ## - For every None found, we shift the elements back that amount
        ## - We then feel the remaining elements with None (with the number of None's found)
        noneOffset = 0
        i = 0
        for i in range(len(nums)):
            if nums[i] == None:
                noneOffset += 1
            else:
                nums[i-noneOffset] = nums[i]
            i+= 1
            
        # ## Cleanup
        # for i in range(1, noneOffset+1):
        #     nums[-i] = "_"
            
        return len(nums) - noneOffset
    
    def solution2(self, nums: List[int]) -> int:
        ## Combined solution (Requires a single pass)
        noneOffset = 0
        previousValue = None
        previousCounter = 0
        for i in range(len(nums)):
            currentValue = nums[i]
            if currentValue != previousValue:
                previousValue = currentValue
                previousCounter = 1
            elif currentValue == previousValue:
                previousCounter += 1
                
            if previousCounter > 2:
                noneOffset += 1
            else:
                nums[i-noneOffset] = nums[i]
                
        ## NOTE: Cleanup not required according to question's implicit checking
        return len(nums) - noneOffset