'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        last = len(nums) - 1
        while i <= last:
            if nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i]
                last -= 1
            else:
                i += 1
        return i

'''
This problem is really tricky. The output requirement actually checks 2 things:
1. Our output: the length of the removed list. (However, since we are asked to remove "in-place", we can't literally just use 'len' function in python)
2. the removed list elements should be shown in the former part of the list.

For example:

when nums = [2, 4, 5, 7, 4, 2, 6, 8] and val = 4
we are expecting to
1. return 6 (since there are two '4' in the list, after removing it the length of the new list will therefore become 6)
and at the same time we need to
2. rearrange the list to become something like [2, 5, 7, 2, 6, 8, 4, 4], and it doesn't matter if the first 6 elements are following in the same order as they were in the old list, as long as these 6 elements are being contained in the first 6 elements of the list.

After doing some research, I realized that it is actually asking you to use a 'two-pointer' technique to solve this. Basically, what we need to do is that whenever our pointer points toward a number that is equal to the 'val', we "throw" this number to the end of the list by SWAPPING this number with the last number.

So, at first we have to set up a pointer 0 in the beginning as an index. Same for the other side of the array, but since index starts from 0, we have to subtract the len(nums) by 1 to show the actual pointer location.

We then need to create a while loop so that the two pointers could stop moving when we have iterated all the list.

Inside the while loop, if the number we point on equals to 'val', then we SWAP it with the last number. Since we are sure that the last number is now 'val', we have to move the 'last' pointer forward. That's why we have to subtract 'last' by 1. Then, for the "else" part, since the nubmer that 'i' pointer is pointing is not 'val' anymore, we will have to add 'i' by 1 to move forward.

Noted that it is important to make sure the condition in the while loop is "i <= last" instead of "i < last", this is because we need to make sure we are also checking the situation of both 'i' and 'last' pointers are pointing same position. Otherwise, there will be a gap that we are not screening at.

At the end of the day, we will end this whole checking process at the "else" part because otherwise if we are still doing the "if" part, it means that we have not yet finished checking the array. As a result, 'i' pointer will end up being a step further than its final position. But since the index is 1 less than actual length of the list, we can just return 'i' as the length of the list. 



