import sys

def cal_values(arr):
    stack = []

    for a in arr:
        if a == '(' or a == '[':
            stack.append(a)
            
        elif a == ')':
            temp = 0
            while stack:
                top = stack.pop()
                if top == '(':
                    temp = 2 if temp == 0 else temp * 2
                    break
                elif isinstance(top, int):
                    temp += top
                else: # 짝이 맞지 않는 경우
                    return 0 
            else: # 짝이 없는 경우
                return 0
            stack.append(temp)

        elif a == ']':
            temp = 0
            while stack:
                top = stack.pop()
                if top == '[':
                    temp = 3 if temp == 0 else temp * 3
                    break
                elif isinstance(top, int):
                    temp += top
                else: # 짝이 맞지 않는 경우
                    return 0   
            else: # 짝이 없는 경우
                return 0        
            stack.append(temp)

        else:
            return 0
        
    # 계산 후에도 괄호 남아 있으면 잘못된 표현식
    result = 0
    for i in stack:
        if not isinstance(i, int):
            return 0
        result += i

    return result

if __name__ == "__main__":
    arr = list(sys.stdin.readline().strip())
    print(cal_values(arr))