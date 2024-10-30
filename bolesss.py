# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthLargestLevelSum(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        mp = {}  
        gr = -1  

        def tk(r, level):
            if r is None:
                return
            if level not in mp:
                mp[level] = [r.val]
            else:
                mp[level].append(r.val)
            tk(r.left, level + 1)
            tk(r.right, level + 1)
        
        tk(root, 1)
        
        level_sums = []
        for level in mp:
            level_sums.append(sum(mp[level]))
        
        level_sums.sort(reverse=True)
        
        if len(level_sums) < k:
            return -1
        else:
            return level_sums[k - 1]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        Determina si un árbol binario es un árbol de búsqueda binario (BST) válido.

        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.prev = None  # Variable para mantener el valor del nodo anterior en el recorrido inorden
        return self._inorder(root)  # Llamada al método auxiliar _inorder

    def _inorder(self, node):
        if not node:
            return True

        # Recorrer el subárbol izquierdo
        if not self._inorder(node.left):
            return False

        # Verificar si el valor actual es mayor que el valor previo
        if self.prev is not None and node.val <= self.prev:
            return False
        self.prev = node.val  # Actualizar el valor previo

        # Recorrer el subárbol derecho
        return self._inorder(node.right)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.left is None and root.right is None:
            return targetSum == root.val
        remainingSum = targetSum - root.val
        return (self.hasPathSum(root.left, remainingSum) or self.hasPathSum(root.right, remainingSum))
    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        arr = []
        def pos(r):
            if r is None:
                return
            pos(r.left)
            pos(r.right)
            arr.append(r.val)
        pos(root)
        return arr

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        arr = []
        def pre(r):
            if r is None:
                return
            else:
                arr.append(r.val)
            pre(r.left)
            pre(r.right)
        
        pre(root)
        return arr

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        arrP = []
        def trP(root):
            if root is None:
                arrP.append(None)
                return
            arrP.append(root.val)
            trP(root.left)
            trP(root.right)
        trP(root)

        arrQ = []
        def trQ(root):
            if root is None:
                arrQ.append(None)
                return
            arrQ.append(root.val)
            trQ(root.right)
            trQ(root.left)
        trQ(root)

        return arrP == arrQ
    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        arr = []
        def parce(r):
            if r is None:
                return
            parce(r.left)
            arr.append(r.val)
            parce(r.right)
        parce(root)
        return arr
    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        arrP = []
        def trP(root):
            if root is None:
                arrP.append(None)
                return
            arrP.append(root.val)
            trP(root.left)
            trP(root.right)
        trP(p)

        arrQ = []
        def trQ(root):
            if root is None:
                arrQ.append(None)
                return
            arrQ.append(root.val)
            trQ(root.right)
            trQ(root.left)
        trQ(q)

        return arrP == arrQ