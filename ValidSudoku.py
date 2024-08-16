class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        def dfs(node):
            if not node:
                return "#"
            return f"{node.val},{dfs(node.left)},{dfs(node.right)}"
        
        return dfs(root)

    def deserialize(self, data):
        def dfs(nodes):
            val = next(nodes)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = dfs(nodes)
            node.right = dfs(nodes)
            return node

        return dfs(iter(data.split(',')))

# Example usage
# Assuming TreeNode class is already defined
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
codec = Codec()
data = codec.serialize(root)
print(data)  # Serialized output
root = codec.deserialize(data)
# Reconstructing and verifying tree structure
def inorder(node):
    return inorder(node.left) + [node.val] + inorder(node.right) if node else []
print(inorder(root))  # Output: [2, 1, 4, 3, 5]
