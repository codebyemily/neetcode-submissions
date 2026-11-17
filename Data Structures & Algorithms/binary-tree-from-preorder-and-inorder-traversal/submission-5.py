# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inordermap = {}
        self.preorder_index = 0 

        for i in range(len(inorder)):
            inordermap[inorder[i]] = i

        def build(l, r):

            # There are no inorder elements in this range, so this subtree does not exist.
            if l > r:
                return None 
                
            root = TreeNode(preorder[self.preorder_index])
            self.preorder_index += 1
            
            root.left = build(l, inordermap[root.val] - 1)
            root.right = build(inordermap[root.val] + 1, r)

            return root
        return build(0, len(preorder) - 1)
