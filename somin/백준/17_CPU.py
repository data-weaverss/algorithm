import sys

def solution(N):
    """N개의 각 줄에 어셈블리어 코드를 기계어 코드로 번역하여 출력"""

    opcode_map = {
        "ADD":   "00000", "ADDC":  "00001",
        "SUB":   "00010", "SUBC":  "00011",
        "MOV":   "00100", "MOVC":  "00101",
        "AND":   "00110", "ANDC":  "00111",
        "OR":    "01000", "ORC":   "01001",
        "NOT":   "01010", "NOTC":  "01011",
        "MULT":  "01100", "MULTC": "01101",
        "LSFTL": "01110", "LSFTLC":"01111",
        "LSFTR": "10000", "LSFTRC":"10001",
        "ASFTR": "10010", "ASFTRC":"10011",
        "RL":    "10100", "RLC":   "10101",
        "RR":    "10110", "RRC":   "10111",
    }

    def to_bin(n, bits):
        return format(int(n), f'0{bits}b')

    for _ in range(N):
        parts = sys.stdin.readline().split()
        opcode = parts[0]
        rD = to_bin(parts[1], 3)
        rA = to_bin(parts[2], 3)

        isC = opcode_map[opcode][4] == '1'
        if isC:
            c = to_bin(parts[3], 4)
            result = opcode_map[opcode] + '0' + rD + rA + c
        else:
            rB = to_bin(parts[3], 3)
            result = opcode_map[opcode] + '0' + rD + rA + rB + '0'
        
        print(result)

if __name__ == "__main__":
    N = int(sys.stdin.readline())

    solution(N)