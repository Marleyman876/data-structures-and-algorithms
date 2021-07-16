
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

