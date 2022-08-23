# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4
		self.patternEnd = False
		
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


def solve (text, n, patterns):
	result = set()
	tree = build_trie(patterns)
	for i, c in enumerate(text):
		currNode = 0
		currChar = i
		while currChar < len(text):
			if(text[currChar] in tree[currNode]):
				currNode = tree[currNode][text[currChar]]
				currChar += 1
				if('$' in tree[currNode] ):
					result.add(i)
					break
			else:
				break
	result = list(result)
	result.sort()
	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip () + '$']

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
