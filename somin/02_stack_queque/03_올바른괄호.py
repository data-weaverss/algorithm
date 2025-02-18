# 문자열 s가 올바른 괄호이면 true, 아니면 false return
def solution(s):
    stack = []
    for char in s:
        # 짝이 맞는 괄호가 들어오면 pop
        if stack and stack[-1] == "(" and char == ")":
            stack.pop()
        else:
            stack.append(char)

    # 스택에 남아있는 괄호가 있다면 False return        
    if len(stack) != 0:
        return False
               
    return True

if __name__ == "__main__":
    s = ")()("
    sol = solution(s)
    print(sol)