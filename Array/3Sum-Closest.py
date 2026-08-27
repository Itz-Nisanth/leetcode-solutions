'''
Q16. 3Sum Closest
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        # starget = float('inf')
        # ans = 0
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             a = nums[i]
        #             b = nums[j]
        #             c = nums[k]
        #             s = a + b + c

        #             d = abs(s - target)
        #             if(d < starget):
        #                 starget = d
        #                 ans = s
        # return ans
        nums.sort()

        starget = float('inf')
        ans = 0

        for i in range(0, len(nums)):

            l = i + 1
            r = len(nums) - 1

            while l < r:

                c = nums[i] + nums[l] + nums[r]
                d = abs(c - target)

                if d < starget:
                    starget = d
                    ans = c

                if c == target:
                    return c

                elif c < target:
                    l += 1

                else:
                    r -= 1

        return ans
    
s = Solution()
print(s.threeSumClosest([-1,2,1,-4], 1)) #output: 2
print(s.threeSumClosest([0,0,0], 1)) #output: 0