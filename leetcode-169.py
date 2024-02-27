"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?

"""



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Majority vote Algorithm runs in O(1) SPACE 

        vote  = 0
        majority_candidate = nums[0]

        for candidate in nums:
        
            if candidate == majority_candidate:
                vote = vote + 1
            else:
                if vote != 0:
                    vote = vote - 1
                elif vote == 0:
                    majority_candidate = candidate
                    vote = 1 
        return majority_candidate 
                                     