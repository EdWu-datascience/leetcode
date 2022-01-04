class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums,reverse=True)
        print(nums)
        return nums[k-1]