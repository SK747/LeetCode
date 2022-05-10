/*
December 8th 2018

Leetcode Q.26

C implementation of Remove Duplicate in an array

#############
*/

#include <stdio.h>

int removeDuplicates (int *nums, int size);

int main()
{
    int nums[]={0,0,1,2,3};
    
    int len = removeDuplicates(nums, 5);
    
    for (int i = 0; i < len; i++) {
        printf("%d",nums[i]);
    }

    return 0;
}

/*
 * Function:  removeDuplicates
 * --------------------
 *  removes Duplicates from a sorted array
 *
 *  nums: The array being modified
 *  size: THe size of the array
 *
 *  returns: the new length of the array, to be used when printing out the contents from the main function
 */

int removeDuplicates (int *nums, int size) {
    
    int i,j;
    int len = 1;

    for (i = 0; i < size; i++) { 
        for (j = 0; j < len; j++){ 
            if (nums[i] == nums[j]) {
                break;
            }
        }
        if (j==len){
            nums[len]=nums[i];
            
            len++;
        }
    }
    
    return len;
}
