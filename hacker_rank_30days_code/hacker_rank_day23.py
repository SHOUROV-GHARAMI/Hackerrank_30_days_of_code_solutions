import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        if root == None:
            return
        queue = []
        queue.append(root)
        while len(queue) != 0:
            node = queue.pop(0)
            print(node.data, end=' ')
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
# End of code snippet
# The code above is a solution to a problem on HackerRank, specifically Day 23 of the 30 Days of Code challenge.