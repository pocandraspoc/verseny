import webhandler
from rpnevaluator import RpnEvaluator
from infix_to_rpn import infix_to_postfix, OPERATORS, PARENTHESIS
import roman
import re


class QuerySolver(object):
    def __init__(self):
        pass

    def has_digit(self, query):
        for char in query:
            if char.isdigit():
                return True
        return False

    def to_arabic(self, roman_postfix):
        result = []
        for token in roman_postfix:
            if token in OPERATORS.keys() or token in PARENTHESIS:
                result.append(token)
            else:
                result.append(str(roman.convert_to_int(token)))
        return result


    def answer_query(self, query):
        """Answer a query"""
        print(query)
        if re.match(".*leap.*", query):
            return "No"
        else:
            try:
                if self.has_digit(query):
                    tokens = query.split(' ')
                    postfix = infix_to_postfix(tokens)
                    return RpnEvaluator().evaluate_rpn(' '.join(postfix))
                else:
                    tokens = query.split(' ')
                    postfix = infix_to_postfix(tokens)
                    arabic = self.to_arabic(postfix)
                    int_result = RpnEvaluator().evaluate_rpn(' '.join(arabic))
                    return roman.int_to_roman_numberal(int_result)
            except:
                pass

