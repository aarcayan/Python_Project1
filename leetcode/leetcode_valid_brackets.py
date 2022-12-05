def check_brackets_final(s):
    stack = []
    brackets = {"]":"[","}":"{",")":"("}

    for c in s:
        if c in brackets:
            if stack and stack[-1] == brackets[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False


def check_brackets(s):
    stack = []
    brackets = {"]":"[","}":"{",")":"("}
    s = s.replace('()',"").replace('[]',"").replace('{}',"")
    print("initial s->",s)

    for c in s:
        if c in brackets:
            if stack and stack[-1] == brackets[c]:
                print("-pop->",stack[-1],c)
                stack.pop()
            else:
                print('FALSE: not a wrong pair->',c)
                return False
        else:
            stack.append(c)
            print("add to stack->",c)

    print("Stack items:", stack)
    if stack.count(0):
        print("stack is empty")
        return True
    else:
        print("stack is not empty")
        return False



print(check_brackets_final("{}[](){"))