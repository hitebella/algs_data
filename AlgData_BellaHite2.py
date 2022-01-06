def balanced(expr):
    #using a sequential array to implement the stack
    stack = []

    for char in expr:
        if char in ["{", "[", "("]:
            #push
            stack.append(char)
        else:
            if not stack:
                return False
            #pop
            char2 = stack.pop()
            if char2 == "{":
                if char != "}":
                    return False
            if char2 == "[":
                if char != "]":
                    return False
            if char2 == "(":
                if char != ")":
                    return False
    return True


par = ["{()}", "[]([]{})", "(){}]["]

for i in par:
    if balanced(i):
        print("The parentheses are balanced!\n", i)
    else:
        print("The parentheses are not balanced :(\n", i)