'''
Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.

 

Example 1:

Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.
'''



class Solution:
    def xorOperation(self, n, start):
        ans = 0
        nums = [start + n * 2 for n in range(n)]
        
        for n in nums:
            ans = ans ^ n
        return ans 

n = 5
start = 0
sol = Solution()
print(sol.xorOperation(n, start))