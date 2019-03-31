/* 

Date: December 11th 2018

Leetcode Q.283

Move zeroes to end of array

*/

#include <stdio.h>


void swap_zeroes (int *x, int *y);
void MoveZeroes (int *nums, int size);

int main()
{
    int nums[]={1,2,0,4,0,5};

    MoveZeroes(nums, 6);

    for (int i = 0; i < 6; i++) {
        printf("%d",nums[i]);
    }

    return 0;
}

/*
 * Function:  MoveZeroes
 * --------------------
 *  moves all zeroes in an array to the back of the array
 *
 *  nums: The array passed to function
 *  size: THe size of the array
 *
 *  returns: nothing. Modifies array in place
 */

void MoveZeroes (int *nums, int size) {
    int i,j;

    for (i = 0; i < size; i++) {
    	if (nums[i]==0){
    		for (j = i+1; j < size; j++) {
    			if (nums[j]!=0){
    				SwapZeroes(nums+i,nums+j);
    				break;
    			}
    		}
    	}
    }
}

/*
 * Function:  SwapZeroes
 * --------------------
 *  swaps a zero number and a nonzero number, placing the zero number further back in the array
 *
 *  x: the zero number
 *	y: nonzero number
 *
 *  returns: nothing. Modifies numbers in place
 */

void SwapZeroes (int *x, int *y) {
	// x is a zero, y is not
	*x = *y;
	*y = 0;
}
