class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        mavontelia = nums

        max_left = mavontelia[0]
        ans = max_left + mavontelia[k]

        for j in range(k, len(mavontelia)):
            max_left = max(max_left, mavontelia[j - k])
            ans = max(ans, max_left + mavontelia[j])

        return ans
        
