
OPERATORS  = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "%": 2,
    "^": 3
}

PARENTHESIS = set(["(", ")"])


def infix_to_postfix(infix):
    stack = []
    postfix = []

    for c in infix:
        if c in OPERATORS:

            if stack:
                top = stack[-1]

                while top in OPERATORS and OPERATORS[top] >= OPERATORS[c]:
                    postfix.append(stack.pop())

                    if stack:
                        top = stack[-1]
                    else:
                        break

            stack.append(c)

        elif c in PARENTHESIS:

            if c == ")":
                try:
                    while stack[-1] != "(":
                        postfix.append(stack.pop())
                except IndexError:
                    raise ValueError("'(' not found when popping")

                stack.pop()  # Removes ( from the top of the stack
            else:
                stack.append(c)  # c == '('
        else:

            postfix.append(c)

        #print("Stack:", stack)
        #print("Postfix:", postfix)

    postfix.extend(token for token in reversed(stack) if token in OPERATORS)

    return postfix