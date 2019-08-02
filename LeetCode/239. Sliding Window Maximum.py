class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        monostack = []
        for i, num in enumerate(nums):
            #add
            while len(monostack) > 0 and monostack[-1] < num:
                monostack.pop()
            monostack.append(num)

            #remove
            if i >= k and monostack[0] == nums[i - k]:
                monostack.pop(0)

            #check
            if i >= k - 1:
                res.append(monostack[0])

        return res