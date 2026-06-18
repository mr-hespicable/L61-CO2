import re
from collections import deque

def greater_precedence(op1, op2):
    precedence = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2}

    a = precedence[op1]
    b = precedence[op2]

    if a > b:
        return True
    elif op1 != "^" and a == b:
        return True
    else:
        return False

def tokenize(raw_infix: str):
    tokens = deque()
    regx = r"(\d+)(([\+\-\*\/])|([\(\)]))*"

    m = re.findall(regx, raw_infix)
    print(m)

tokenize("6+7*(1+2)/23")
exit()


def shunting_yard_algorithm(infix: str):
    # we are assuming here that the infix expression is valid.
    output_queue = deque()
    operator_stack = deque()

    valid_operators = "^+-/*"

    infix = infix.replace(" ", "")

    for token in infix:
        if token.isnumeric():  # number
            output_queue.appendleft(token)

        elif token in valid_operators:  # operator
            while (
                operator_stack
                and operator_stack[-1] != "("
                and greater_precedence(operator_stack[-1], token)
            ):
                output_queue.appendleft(operator_stack.pop())

            operator_stack.append(token)

        elif token == "(":
            operator_stack.append(token)

        elif token == ")":
            while operator_stack and operator_stack[-1] != "(":
                output_queue.appendleft(operator_stack.pop())
            operator_stack.pop()  # pop left paren

    while operator_stack:
        output_queue.appendleft(operator_stack.pop())

    return "".join(output_queue)[::-1]


def evaluate_rpn(rpn: str):
    # we are assuming here that rpn expression is valid
    output_stack = deque()
    print(rpn)

    for item in rpn:
        print(output_stack)
        if item.isnumeric():
            output_stack.append(item)
        else:  # operator
            if output_stack:
                right = float(output_stack.pop())
                left = float(output_stack.pop())

                match item:
                    case "+":
                        o = left + right
                    case "-":
                        o = left - right
                    case "*":
                        o = left * right
                    case "/":
                        o = left / right
                    case "^":
                        o = left**right

                output_stack.append(str(o))
    result = float(output_stack[0])
    print(result)
    print(int(result))
    if result == int(result):
        return int(result)
    else:
        return result


r_string = input("input math expression: ")

if re.fullmatch(
    r"((\(|\))*(\d+)\s?(\(|\))*\s?([+\-\/*^]?\s?))+\d(\(|\))*".replace(" ", ""),
    r_string,
) and r_string.count("(") == r_string.count(")"):
    print("That expression is valid")
    print("Calcluating...")
    result = evaluate_rpn(shunting_yard_algorithm(r_string))
    print(result)

else:
    print("That expression is INVALID.")
