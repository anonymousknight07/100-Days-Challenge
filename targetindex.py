# 2089. Find Target Indices After Sorting Array

# You are given a 0-indexed integer array nums and a target element target.

# A target index is an index i such that nums[i] == target.

# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

# Example 1:

# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.
# Example 2:

# Input: nums = [1,2,5,2,3], target = 3
# Output: [3]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 3 is 3.
# Example 3:

# Input: nums = [1,2,5,2,3], target = 5
# Output: [4]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 5 is 4.

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        # start=0
        # lis1=[]
        # n=len(nums)
        # end=n-1
        # while(start<=end):
        #     mid=(start+end)//2
        #     if(nums[mid]==target):
        #         lis1.append(mid)
        #         if(nums[mid-1]==target):
        #             lis1+=((mid-1),mid)
        #             break
        #         elif(nums[mid+1]==target):
        #             lis1+=(mid,(mid+1))
        #         elif(nums[mid-1]==target,nums[mid+1]==target):
        #             lis1+=((mid-1),mid,(mid+1))
        #     elif(nums[mid-1]==target):
        #         lis1.append(mid-1)
        #     elif(nums[mid+1]==target):
        #         lis1.append(mid+1)
        #     elif(nums[mid]>target):
        #         start=mid+1
        #     else:
        #         end=mid-1
        # return lis1
        lis1=[]
        nums.sort()
        for i in range(len(nums)):
            if(nums[i]==target):
                lis1.append(i)
        return lis1


        
        