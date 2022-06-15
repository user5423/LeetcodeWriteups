class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None
	return self.backwards(nums1, m, nums2, n)

    def backwards(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        firstCounter = m - 1
        secondCounter = n - 1

        for destCounter in range(m+n-1,-1, -1):
            if firstCounter < 0 or secondCounter < 0:
                break
                
            firstNum = nums1[firstCounter]
            secondNum = nums2[secondCounter]
            
            if firstNum > secondNum:
                nums1[destCounter] = firstNum
                firstCounter -= 1
            else:
                nums1[destCounter] = secondNum
                secondCounter -= 1
        
        if firstCounter == m+n or firstCounter < 0:
            nums1[:destCounter+1] = nums2[:secondCounter+1]
            
        return nums1
