# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque()
        q.append(root)
        res = ""
        if not root:
            return "" 

        while q: 
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    res += "None,"
                    continue
                
                q.append(node.left) if node.left else q.append(None)
                q.append(node.right) if node.right else q.append(None)

                res += str(node.val) + ","
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        values = data.split(",")

        root = TreeNode(int(values[0]))
        q = deque([root])
        index = 1

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                # left child
                if values[index] != "None":
                    node.left = TreeNode(int(values[index]))
                    q.append(node.left)
                index += 1

                # right child
                if values[index] != "None":
                    node.right = TreeNode(int(values[index]))
                    q.append(node.right)
                index += 1

        return root


        