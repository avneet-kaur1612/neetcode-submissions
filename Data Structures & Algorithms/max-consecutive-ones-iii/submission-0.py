class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        longest = zero_count = left = 0
        for right in range(len(nums)):
            if nums[right]==0:
                zero_count +=1
            while zero_count>k:
                if nums[left]==0:
                    zero_count-=1
                left+=1
            longest = max(longest, right-left+1)
        return longest
        