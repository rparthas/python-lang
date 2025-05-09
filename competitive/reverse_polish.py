def solve(tokens):
    stack = []
    operators = {
        "+": lambda a,b: a+b,
        "-":lambda a,b: a-b,
        "*": lambda a,b: a*b,
        "/": lambda a,b: int(a/b)
    }
    for token in tokens:
        if token in operators:
            if  len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                result = operators[token](b,a)
                stack.append(result)
            else:
                pass
        else:
            stack.append(int(token))

    if len(stack) > 0:
        return stack[0]
    else:
        return 0


if __name__ == "__main__":
    print(solve(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    print(solve(["4","13","5","/","+"]))
    print(solve(["2","1","+","3","*"]))
