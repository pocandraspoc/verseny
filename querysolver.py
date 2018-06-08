import webhandler
from rpnevaluator import RpnEvaluator
from infix_to_rpn import infix_to_postfix

class QuerySolver(object):
    def __init__(self):
        pass

    def answer_query(self, query):
        """Answer a query"""
        print(query)
        tokens = query.split(' ')
        postfix = infix_to_postfix(tokens)
        return RpnEvaluator().evaluate_rpn(' '.join(postfix))
