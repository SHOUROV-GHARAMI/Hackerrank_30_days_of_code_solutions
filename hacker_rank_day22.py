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

    def getHeight(self,root):
        #Write your code here
        leftHeight = 0
        rightHeight = 0
        if root == None:
            return 0
        if root.left !=None:
            leftHeight = 1+ self.getHeight(root.left)
        if root.right != None:
            rightHeight = 1 + self.getHeight(root.right)
        return max(leftHeight,rightHeight)
            
            

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       