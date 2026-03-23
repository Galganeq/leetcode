def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    if (len(s) % 2) != 0:
        return False
    open_and_close = {"{": "}","(": ")","[": "]"}
    stack = []
    for current in s:
        if current in open_and_close.keys():
            stack.append(current)
        elif ((len(stack) != 0) and (open_and_close[(stack.pop())] == current)):

            continue
        else:
            return False
    if (len(stack) != 0):
        return False
    return True
        

s = "]"
print(isValid(s))