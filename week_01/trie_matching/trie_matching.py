# python3
import sys

from numpy import empty

NA = -1

def build_trie(patterns):
    tree = dict()
    tree[0] = {}
    nodeId = 0
    for pattern in patterns:
        currNode = 0
        for c in pattern:
            if(c in tree[currNode]):
                currNode = tree[currNode][c]
            else:
                nodeId += 1
                tree[currNode][c] = nodeId
                tree[nodeId] = {}
                currNode = nodeId
    return tree

class Node:
	def __init__ (self):
		self.next = [NA] * 4

def solve (text, n, patterns):
	result = []
	tree = build_trie(patterns)
	for i, c in enumerate(text):
		currNode = 0
		currChar = i
		while currChar < len(text):
			if(text[currChar] in tree[currNode]):
				currNode = tree[currNode][text[currChar]]
				currChar += 1
				if( not tree[currNode] ):
					result.append(i)
					break
			else:
				break


	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
