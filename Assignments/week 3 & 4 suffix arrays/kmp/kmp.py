# python3
import sys



def computePrefixFunction(text):
  P = len(text)
  S = [0 for i in range(P)]
  border = 0
  
  

  for i in range(1,P):
    while (border > 0) and (text[i] != text[border]):
      border = S[border-1]
    
    if text[i] == text[border]:
      border += 1
    else:
      border = 0
    S[i] = border
  
  return S

def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  result = []
  # Using Knuth Morris Pratt Algorithm

  string = pattern + '$' + text
  s = computePrefixFunction(string)
  P = len(pattern)
  S = len(string)

  for i in range(P+1,S):
    if s[i] == P:
      result.append(i- 2*P)

  return result


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

