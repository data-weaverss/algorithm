import sys

def solution(input_str):
    """
    int& a, *b, c[]; 
    ->
    int& a;
    int* b;
    int[] c;

    독립적인 선언문으로 출력
    """
    base_type, *variables = input_str.replace(",", "").replace(";", "").split()

    for var in variables:
        name = ''
        postfix = ''
    
        for ch in var:
            if ch.isalpha():
                name += ch
            else:
                if ch == ']':
                    postfix = '[]' + postfix # []는 한 쌍으로 추가
                elif ch == '[':
                    continue      
                else: # 나머지 기호 역순으로
                    postfix = ch + postfix  

        full_type = base_type + postfix
        print(f"{full_type} {name};")

if __name__ == "__main__":
    input_str = sys.stdin.readline().strip()

    solution(input_str)