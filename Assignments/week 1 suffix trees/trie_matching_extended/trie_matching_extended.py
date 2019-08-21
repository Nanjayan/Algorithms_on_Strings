# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4


def build_trie(patterns):
    tree = dict()
    # Trie building using dictionary of dictionaries
    tree[0] = {}
    nodeNumber = 1
    for pattern in patterns:
    	currentNode = 0
    	n1=len(pattern)
    	ct=0
    	for c in pattern:
    		ct+=1
    		if ct == n1:
    			val = True
    		else:
    			val = False
    		if c not in tree[currentNode]:
    			tree[currentNode][c] = [nodeNumber,val]
    			tree[nodeNumber] = {}
    			nodeNumber += 1
    		if ct == n1:
    			tree[currentNode][c][1] = val 
    		currentNode = tree[currentNode][c][0]
    return tree


def prefix_match(text, trie,patterns):
	v =  0
	
	for symbol in text:
		if symbol in trie[v]:
			if trie[v][symbol][1]:
				return True
			v = trie[v][symbol][0]
		else:
			return False


def solve (text,trie,patterns):
	result = []
	n=len(text)
	for i in range(n):
		texts=text[i:n]
		bool_result = prefix_match(texts,trie,patterns)
		if bool_result:
			result.append(i)
	
	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

trie = build_trie(patterns)
ans = solve (text, trie,patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
