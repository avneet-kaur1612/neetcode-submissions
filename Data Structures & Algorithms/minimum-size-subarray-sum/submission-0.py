class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        smallest = float('inf')
        current_sum = left = 0
        for right in range(len(nums)):
            current_sum +=nums[right]
            while current_sum>=target:
                smallest = min(smallest, right-left+1)
                current_sum -=nums[left]
                left+=1
        return smallest if smallest != float('inf') else 0
        