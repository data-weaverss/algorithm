def solution(s):
    """
    주어진 문자열 s가 올바른 괄호 문자열인지 확인하는 함수.

    :param s: '('와 ')'로 이루어진 문자열
    :return: 올바른 괄호 문자열이면 True, 그렇지 않으면 False
    """
    stack = []  # 괄호를 저장할 스택

    for parenthesis in s:
        # 스택이 비어있거나, 마지막 열린 괄호와 닫힌 괄호가 짝을 이루지 않는 경우
        if not stack or (stack[-1], parenthesis) != ("(", ")"):
            stack.append(parenthesis)
        else:
            stack.pop()

    return not stack  # 스택이 비어있으면 올바른 괄호 문자열


if __name__ == "__main__":
    s = "(()("
    sol = solution(s)
    print(sol)
