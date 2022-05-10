/* 

Leetcode Q. 344
C program to Reverse String
    
*/

#include <stdio.h>

void swap (char *x, char *y);
void ReverseCharacters (char *n, int size);

int main()
{
    char hello[6]={"hello"};

    printf("The string reads: %s \n", hello);

    ReverseCharacters(hello, 5);

    printf("The reversed string reads: %s", hello);

    return 0;
}

/*
 * Function:  ReverseCharacters
 * --------------------
 *  reverses characters in a string
 *
 *  n: the char array
 *  size: THe size of the string
 *
 *  returns: nothing. Modifies string in place
 */

void ReverseCharacters (char *n, int size) {
    int i,j;
    char temp;

    for (i = 0,j = size-1;i<j; i++,j--) {
        temp = *(n+i);
        Swap((n+i),(n+j));
    }
}

/*
 * Function:  Swap
 * --------------------
 *  swaps two characters using pointers
 *
 *  x: the first char
 *  y: second char
 *
 *  returns: nothing. Modifies characters in place
 */

void Swap (char *x, char *y) {
    // x is a zero, y is not
    char temp;
    temp = *x;

    *x = *y;
    *y = temp;
}
