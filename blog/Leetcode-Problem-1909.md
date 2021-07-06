---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults

date: 2021-07-03 18:47:07 UTC
has_math: true
title: Leetcode Problem 1909
slug: Leetcode-Problem-1909
tags: problems
category: 
link: 
description: 
type: text
---
## Description

Given a 0-indexed integer array `nums`, return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array is already strictly increasing, return true.

The array `nums` is strictly increasing if `nums[i - 1] < nums[i]` for each index `(1 <= i < nums.length)`.


We need to see if it is possible to make the given array strictly increasing by removing no more than 1 number. 
Removing one number means there is one violation in the strictly increasing array. So once we see this violation we
just need to verify that after removing the violation we get a strictly increasing array.

Lets consider an example:

```
[1,2,10,5,7]
```
The violation here will be caught at index 3 when we compare 10 and 5. In this case we are better off dropping the 10 but how do we know this?
Consider this example:

```
[10,20,7]
```
Here we are better off dropping `i` instead of `i-1` in the previous example. We can avoid having to make this decision
if we just test both cases, the array without `i` and the array without `i-1`. Here we will just check if either of the resulting
arrays is strictly increasing and if it is we return `true` else `false`. 

```cpp

class Solution {
public:
    bool isStrictInc(const vector<int>& nums){
        int prev=0;
        for(int i=1;i<nums.size();i++){
            
            if (nums[i]==-1){
                continue;
            } 
            
            if (nums[prev]>=nums[i]){
                return false;
            }
            
            prev=i;
        }
        return true;
    }
    
    bool canBeIncreasing(vector<int>& nums) {
        // find first violation in the array
        for(int i=1;i<nums.size();i++){
            if(nums[i-1]>=nums[i]){
                // we have a problem
                //remove either or
                int tmp=nums[i];
                nums[i]=-1;
                if (isStrictInc(nums)){
                    return true;
                }
                nums[i]=tmp;
                tmp=nums[i-1];
                nums[i-1]=-1;
                if (isStrictInc(nums)){
                    return true;
                }
                nums[i-1]=tmp;
                return false;
            }
        }
        return true;
        
    }
};
```

## Time complexity

$ O(n) $

This is because we traverse the whole array no more than three times. Once to find the first violation and then twice to check the resulting array
after we find the first violation and remove `i` and then if we remove `i-1`.

## Space complexity 

$ O(1) $

It is constant because we modify our array by putting -1 in the place of the value we want to remove. Then we pass by reference to
`isStrictInc` where we check if it is strictly increasing skipping over -1. Again once we see a violation we do this for `i` and `i-1`.

