# python3
import sys

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

def build_suffix_tree(text):
  strings = []
  for i in range(len(text)):
    strings.append(text[i:])
  
  trie = build_trie(strings)
  """
  Build a suffix tree of the string text and return a list
  with all of the labels of its edges (the corresponding 
  substrings of the text) in any order.
  """
  result = []

  def printEdge(node,s):
    if not trie[node]:
      result.append(s)
    elif len(trie[node]) == 1:
      new_node = list(trie[node].values())
      new_s = list(trie[node].keys())
      printEdge(new_node[0],s+new_s[0])
    else:
      result.append(s)
      for key, value in trie[node].items():
        printEdge(value,key)


  for key, value in trie[0].items():
    printEdge(value,key)

  # Implement this function yourself
  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))