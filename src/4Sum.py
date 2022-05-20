class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.solutionOne(nums, target)
        
    def solutionOne(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        output = set()
        
        if len(nums) < 4:
            return output
        
        for left in range(len(nums) - 3):
            for right in range(left+3, len(nums)):
                ## The left and right bounds are fixed and will be used in the sum
                cumulativeSum = nums[left] + nums[right]

                ## Stops redundant operations
                if cumulativeSum > target and nums[left] >= 0:
                    break

                remainderTarget = target - cumulativeSum
                ## perform two pointer on nums[left+1] to nums[right-1]
                l = left+1
                r = right-1

                while l < r:
                    tpSum = nums[l] + nums[r]
                    if tpSum < remainderTarget:
                        l += 1
                    elif tpSum > remainderTarget:
                        r -= 1
                    else:
                        output.add((nums[left], nums[l], nums[r], nums[right]))
                        l += 1
        return output
    
    