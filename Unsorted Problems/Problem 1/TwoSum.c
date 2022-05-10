/*  
    Date: December 27th 2018

    Leetcode Q. 1

    C Solution to finding two numbers in an array that add to a target number
*/

#include <stdio.h>
#include <stdlib.h>

/*
 * Function:  twoSum
 * --------------------
 *  Finds two numbers in an array that add to the target number
 *
 *  target: The target number
 *  nums: the array
 *  size: size of the array
 *
 *  returns: the solution array containing the indices of the solutions in the arra
y */

int* twoSum(int* nums, int size, int target) {
    int i,j;
    int* solution = (int*)malloc(sizeof(int) * 2);

    for (i = 0; i < size; i++) {
        for (j = i; j < size; j++){
            if ((nums[i]+nums[j])==target && nums[i]!=nums[j]){
                solution[0] = i;
                solution[1] = j;
                break;
            }
        }
    }
    return solution;
}

int main()
{
    int nums[]={1,2,4,7};
    int *solution = twoSum(nums, 4, 6);

    for (int i = 0; i < 2; i++) {
        printf("%d \n",solution[i]);
    }

    return 0;
}
