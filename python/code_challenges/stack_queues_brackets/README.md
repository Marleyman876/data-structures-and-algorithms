# Bracket Validation

## Problem Domain

Write a function called validate brackets
Arguments: string
Return: boolean
representing whether or not the brackets in the string are balanced

## Edge Cases

Bracket is open and not closed
An int is given

## Input/Output

{}                            TRUE
{}(){}                        TRUE
()[[Extra Characters]]        TRUE
(){}[[]]                      TRUE
{}{Code}[Fellows](())         TRUE
[({}]                         FALSE
(](                           FALSE
{(})                          FALSE

## Visual

{ False
) False
[} False

## Big O

Time: O(n)
Space: O(1)

## Algorithm

Push each opening bracket in the stack.
pop the last inserted opening bracket when a closing bracket is encountered if brackets match return TRUE
If the closing bracket does not correspond to the opening bracket, then we stop and say that the brackets are not balanced and return FALSE

## Code

```py
def Brackets(string):
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_par = set(["(", "[", "{"])
    stack = []
    for i in string:
        if i in open_par:
            stack.append(i)
        elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
        else:
            return False
    if len(stack)== 0:
        return True
    else:
        return False

```

## [White Board]()
