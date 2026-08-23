'''
Q15. 3SUM
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

class Solution(object):
    def threeSum(self, nums):

        # arr = []

        # for i in range(0, len(nums)):
        #     for j in range(0, len(nums)):
        #         for k in range(0, len(nums)):
        #             if(i != j and i != k and j != k):
        #                 if(nums[i] + nums[j] + nums[k] == 0):
        #                     arr = arr +  [[nums[i], nums[j], nums[k]]]

        # unique_array = list(dict.fromkeys(tuple(sorted(x)) for x in arr))
        # return [list(x) for x in unique_array]

        nums.sort()
        arr = []

        for i in range(len(nums)):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                s = nums[i] + nums[left] + nums[right]

                if s < 0:
                    left += 1

                elif s > 0:
                    right -= 1

                else:
                    arr += [[nums[i], nums[left], nums[right]]]
                    left += 1
                    right -= 1

        unique_array = list(dict.fromkeys(tuple(sorted(x)) for x in arr))
        return [list(x) for x in unique_array]

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4])) 
print(s.threeSum([0,1,1]))
print(s.threeSum([0,0,0]))