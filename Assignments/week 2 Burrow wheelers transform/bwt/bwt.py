# python3
import sys

def BWT(text):
    n = len(text)
    text_mod = text
    matrix = []
    for i in range(n):
        text_mod = text_mod[-1] + text_mod[:-1]
        matrix.append(text_mod)
    
    res = ""
    for word in sorted(matrix):
        res+=word[-1]
    return res

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))