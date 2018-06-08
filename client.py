"""This is the main module"""
import random
import webhandler
import querysolver
import rpnevaluator
import traceback

def main():
    """Run client"""
    if not webhandler.API_KEY:
        raise ValueError("Set your API_KEY in webhandler.py! Find it on https://devrecruitmentchallenge.com/account")

    rpn_evaluator = rpnevaluator.RpnEvaluator()
    query_solver = querysolver.QuerySolver()

    print("Getting challenge list")
    challenge_list = webhandler.get_challenge_list()
    print("There are {} challenges".format(len(challenge_list)))

    for info in challenge_list:
        print("Solving challenge {} - {}".format(info.cid, info.challenge_type))
        challenge = webhandler.get_challenge(info.cid)

        if info.challenge_type == "rpn":
            try:
                handle_rpn(challenge, rpn_evaluator)
            except Exception as ex:
                traceback.print_exc()
        elif info.challenge_type == "query":
            try:
                handle_query(challenge, query_solver)
            except Exception as ex:
                print(ex)
                traceback.print_exc()
        else:
            print("Unrecognised challenge type '{}'".format(info.challenge_type))

def handle_rpn(challenge, rpn_evaluator):
    """Handle an RPN challenge"""
    answers = {}
    for question in challenge.questions:
        answer = rpn_evaluator.evaluate_rpn(question.question)
        answers[question.tid] = answer
    submission = {'challengeId': challenge.info.cid, 'answers': answers}
    result = webhandler.post_standard_submission(submission)
    print("Mark = {}%".format(result.mark))

def handle_query(challenge, solver):
    """Handle a general query challenge"""
    answers = {}
    for question in challenge.questions:
        answer = solver.answer_query(question.question)
        answers[question.tid] = answer
    submission = {'challengeId': challenge.info.cid, 'answers': answers}
    result = webhandler.post_standard_submission(submission)
    print("Mark = {}%".format(result.mark))


if __name__ == "__main__":
    main()
