// 75. Sort Colors
// Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
// We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
// You must solve this problem without using the library's sort function.

// Example 1:

// Input: nums = [2,0,2,1,1,0]
// Output: [0,0,1,1,2,2]
// Example 2:

// Input: nums = [2,0,1]
// Output: [0,1,2]

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int count1=0;
        int count2=0;
        int count3=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==0){
                count1+=1;
            }
            else if(nums[i]==1){
                count2+=1;
            }
            else{
                count3+=1;
            }

        }
        int i=0;
        
        for(;i<count1;i++){
            nums[i]=0;

        }
        for(;i<count1+count2;i++){
            nums[i]=1;

        }
         for(;i<count1+count2+count3;i++){
            nums[i]=2;

        }
        



        
    }
};