'''
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

 

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
'''

class Solution:
    def largestAltitude(self, gain) :
        curr_alt = 0
        max_alt = 0
        for v in gain:
            curr_alt += v
            if curr_alt > max_alt:
                max_alt = curr_alt
        return max_alt

gain =  [-4,-3,-2,-1,4,3,2]
sol = Solution()
print(sol.largestAltitude(gain))
