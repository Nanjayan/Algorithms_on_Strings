# python3
import sys

def InverseBWT(bwt):
    A, C, G , T = 1, 1, 1, 1
    lastColumn = []
    for c in bwt:
    	if c == '$':
    		lastColumn.append(('$', 0))
    	elif c == 'A':
    		lastColumn.append(('A', A))
    		A += 1
    	elif c == 'C':
    		lastColumn.append(('C', C))
    		C += 1
    	elif c == 'G':
    		lastColumn.append(('G', G))
    		G += 1
    	else:
    		lastColumn.append(('T', T))
    		T += 1
    
    firstColumn = sorted(lastColumn)
    
    firstToLast = {}
    for i in range(len(firstColumn)):
    	firstToLast[firstColumn[i]] = lastColumn[i]
    
    result = ""
    nextChar = ('$', 0)
    while len(result) < len(firstColumn):
    	result += nextChar[0]
    	nextChar = firstToLast[nextChar]
    result = result[::-1]
    return result


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))