# Time Complexity : O(n + k), n is no of nodes in the tree, and k is the width of the tree (reversing)
# Space Complexity : O(n), because the queue can store all leaf nodes at max in the worst case
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : NA 

# Your code here along with comments explaining your approach:
# we are using a queue to do level order traversal of a binary tree
# we maintain a boolean variable, and based on that we reverse the list after we complete a level
# we put the root of the tree in the queue
# since we need to differentiate between the levels of the tree, we need to use the size variable
# while the queue is not empty, we do the following operations:
# first, we take size of the queue
# then we start another loop that goes on for size no of times
# then we remove a node from it
# then we add the value of this node to a list, that we initialize for every level
# for every node, we check, if left and right children are valid, we add them to the queue
# at the end of the size loop, we revert the list based on direction, and then reset the value of direction
# at the end we can return the final result list

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        result = []
    
        q = deque([root])
        # boolean variable to reverse direction
        direction = 0 # L to R, 1 = R to L
        
        # BFS
        while q:
            size = len(q)
            # list for level
            level = []
            for i in range(size):
                curr = q.popleft()
                level.append(curr.val)
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)

            if direction:
                # reverse the list
                level.reverse()
            
            # and then revert the value of direction for alternate levels
            if direction == 0:
                direction = 1
            else:
                direction = 0
            
            # result is a lis of lists of level traversals
            result.append(level)
        
        return result
            


            

            
                
