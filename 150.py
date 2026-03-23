def evalRPN(tokens):
        
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            
            if i == "+":
                  stack.append((int(stack.pop(-2)) + int(stack.pop(-1))))
                  continue
            if i == "-":
                  stack.append((int(stack.pop(-2)) - int(stack.pop(-1))))
                  continue
            if i == "*":
                  stack.append((int(stack.pop(-2)) * int(stack.pop(-1))))
                  continue
            if i == "/":
                  stack.append(int(int(stack.pop(-2)) / int(stack.pop(-1))))
                  continue
            stack.append(i)
        
        return stack[-1]

tokens = ["4","13","5","/","+"]
print(evalRPN(tokens))



        # stack = []
        # for i in tokens:
            
        #     if i == "+":
        #           stack.append((int(stack[-2]) + int(stack[-1])))
        #           continue
        #     if i == "-":
        #           stack.append((int(stack[-2]) - int(stack[-1])))
        #           continue
        #     if i == "*":
        #           stack.append((int(stack[-2]) * int(stack[-1])))
        #           continue
        #     if i == "/":
        #           stack.append((int(stack[-2]) / int(stack[-1])))
        #           continue
        #     stack.append(i)
        # return stack[-1]