'''
Q4. 4Sum
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 
Constraints:
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''



class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        # arr = []
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             for l in range(k+1, len(nums)):
        #                 if((nums[i] + nums[j] + nums[k] + nums[l]) == target):
        #                     arr += [[nums[i], nums[j], nums[k], nums[l]]]

        # unqarr = [list(x) for x in set(tuple(x) for x in arr)]
        # return unqarr
        
        arr = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                left = j+1
                right = len(nums)-1
                while(left < right):
                    c = (nums[left]+nums[right]+nums[j]+nums[i])
                    if(c == target):
                        arr += [[nums[left], nums[right], nums[i], nums[j]]]
                        left += 1
                        right -= 1
                    elif(c < target):
                        left+=1
                    elif(c > target):
                        right-=1
        
        unqarr = [list(x) for x in set(tuple(x) for x in arr)]
        return unqarr
    
s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0)) #output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(s.fourSum([2,2,2,2,2], 8)) #output: [[2,2,2,2]]