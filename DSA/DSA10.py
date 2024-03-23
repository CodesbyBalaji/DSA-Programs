class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.val, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=' ')

def insert_node(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.val:
            root.left = insert_node(root.left, key)
        else:
            root.right = insert_node(root.right, key)
    return root

def build_bst():
    root = None
    n = int(input("Enter the number of elements in the BST: "))
    for _ in range(n):
        key = int(input("Enter element: "))
        root = insert_node(root, key)
    return root

if __name__ == "__main__":
    root = build_bst()

    print("Inorder Traversal:")
    inorder_traversal(root)
    print("\n")
 
    print("Preorder Traversal:")
    preorder_traversal(root)
    print("\n")

    print("Postorder Traversal:")
    postorder_traversal(root)
    print("\n")