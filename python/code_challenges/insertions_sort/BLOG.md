# Selection Sort

## Challenge Summary

Given a list of integers, create a function that loops through the list and re sorts the list from the smallest integer to the largest integer.

Trace
Sample Array: [8,4,23,42,16,15] (isn't this the numbers from that TV SHOW LOST??? if it is that definately how I felt through mos)

## Efficency

Time: O(n^2)
The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times…concluding the algorithm to be n squared.

Space: O(1)
No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).

## Algorithm Steps

1. create a function.

2. using a for loop using the index and the value you can enumarate throught the entire list(Found this on stack overflow).

3. nest a while loop where you can check the integers in the list of the for loop where if the value in the for loop is greater than the value in the for loop move it to the right (think i need a temp varable or maybe some sort of count for this. ).

4. the loop will run until it sorts all the nnumbers in the list.
