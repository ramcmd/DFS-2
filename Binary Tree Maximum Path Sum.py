# TC: O(n)
# SC: O(log n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = float("-inf")
        self.dfs(root)
        return self.max
    
    def dfs(self, root):
        if root == None:
            return 0
        
        leftSum = max(self.dfs(root.left), 0)
        rightSum = max(self.dfs(root.right), 0)
        
        rootmax = leftSum + rightSum + root.val
        
        if self.max < rootmax:
            self.max = rootmax
            
        return root.val + max(leftSum, rightSum)
        
        
        
        