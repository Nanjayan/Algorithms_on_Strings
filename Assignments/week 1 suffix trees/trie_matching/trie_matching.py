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
    	for c in pattern:
    		if c not in tree[currentNode]:
    			tree[currentNode][c] = nodeNumber
    			tree[nodeNumber] = {}
    			nodeNumber += 1
    		currentNode = tree[currentNode][c]
    
    return tree


def prefix_match(text, trie):
	v =  0
	for symbol in text:
		if symbol in trie[v]:
			v = trie[v][symbol]
			if trie[v]=={}:
				return True
		else:
			return False


def solve (text,trie):
	result = []
	n=len(text)
	for i in range(n):
		texts=text[i:n]
		bool_result = prefix_match(texts,trie)
		if bool_result:
			result.append(i)
	
	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

trie = build_trie(patterns)
ans = solve (text, trie)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
