# Code Challenege 16

## Problem Domain:

Write the following method for the Binary Tree class
find maximum value
Arguments: none
Returns: number
Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

## Edge Cases

1. Tree Cannot be blank
2. Tree cannot be a string

## Input/Output

Input = 1, 5, 10, 25, 15

output = 25

## Algorithm

write a function to find max value
set value where if root is empty return string root cannot be empty
use post order as a helper function from previous tree
since a list of all the values from the tree will be returned with the helper function
we can just loop through the list and compare all values in the list to return the max value

## Code

```py
 def find_max_value(self):
        if (self.root == None):
            return 'root value cannot be empty'

        all_values = self.post_order()
        max_value = all_values[0]

        for i in all_values:
            if i > max_value:
                max_value = i

        return max_value
