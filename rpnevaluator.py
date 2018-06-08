import webhandler

class RpnEvaluator(object):
    def __init__(self):
        pass

    def evaluate_rpn(self, rpn):
        """Evaluate RPN"""
        operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }

        elements = rpn.split()
        pile = []
        while elements:
            e = elements.pop(0)
            if e in operators:
                b = pile.pop()
                a = pile.pop()
                pile.append(operators[e](a, b))
            else:
                pile.append(int(e))
        return int(pile[0])
