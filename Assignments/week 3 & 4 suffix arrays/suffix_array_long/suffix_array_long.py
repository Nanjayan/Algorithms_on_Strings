# python3
import sys


def SortCharacters (S):
  n = len(S)
  order = [0 for i in range(n)]
  # since we have A, C, G, T, $ characters only
  count = [0 for i in range(5)]

  # using counting sort
  for i in range(n):
    if S[i] == '$':
      val = 0
    elif S[i] == 'A':
      val = 1
    elif S[i] == 'C':
      val = 2
    elif S[i] == 'G':
      val = 3
    elif S[i] == 'T':
      val = 4
    count[val]+=1

  for j in range(1,5):
    count[j] += count[j-1]
  
  for i in range(n-1,-1,-1):
    if S[i] == '$':
      c = 0
    elif S[i] == 'A':
      c = 1
    elif S[i] == 'C':
      c = 2
    elif S[i] == 'G':
      c = 3
    elif S[i] == 'T':
      c = 4
    
    count[c] -= 1
    order[count[c]] = i
  
  return order


def ComputeCharClasses(S, order):
  n = len(S)
  Class = [0 for i in range(n)]
  Class[order[0]] = 0
  for i in range(1,n):
    if S[order[i]] != S[order[i-1]]:
      Class[order[i]] = Class[order[i-1]] + 1
    else:
      Class[order[i]] = Class[order[i-1]]
  return Class

def SortDoubled(S, L, order, Class):
  n = len(S)
  count = [0 for i in range(n)]
  newOrder = [0 for i in range(n)]
  for i in range(n):
    count[Class[i]] += 1
  for j in range(1, n):
    count[j] += count[j-1]
  for i in range(n-1,-1,-1):
    start = (order[i] - L + n) % n
    cl = Class[start]
    count[cl] -= 1
    newOrder[count[cl]] = start
  return newOrder


def UpdateClasses(newOrder, Class, L):
  n = len(newOrder)
  newClass = [0 for i in range(n)]
  newClass[newOrder[0]] = 0
  for i in range(1,n):
    cur = newOrder[i]
    prev = newOrder[i-1]
    mid = cur + L
    midPrev = (prev + L ) % n
    if (Class[cur] != Class[prev]) or Class[mid] != Class[midPrev]:
      newClass[cur] = newClass[prev] + 1
    else:
      newClass[cur] = newClass[prev]
  return newClass


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """

  order = SortCharacters(text)
  Class = ComputeCharClasses(text, order)
  L = 1
  S = len(text)
  while L < S:
    order = SortDoubled(text, L, order, Class)
    Class = UpdateClasses(order, Class, L)
    L = 2*L 

  result = order
  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
