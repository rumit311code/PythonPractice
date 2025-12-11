"""
Binary Search Tree Structure:

├── 15
│   ├── 10
│   │   └── 12
│   │       ├── 11
│   └── 20
│       ├── 18
│       │   ├── 16
│       │   └── 19

Preorder: [15, 10, 12, 11, 20, 18, 16, 19]
Postorder: [11, 12, 10, 16, 19, 18, 20, 15]

insert(): Builds BST maintaining left < root < right property
preorder(): Root → Left → Right traversal
postorder(): Left → Right → Root traversal
print_tree(): Visual tree representation

"""
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    elif key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def preorder(root, path=[]):
    if root:
        path.append(root.val)
        preorder(root.left, path)
        preorder(root.right, path)
    return path

def postorder(root, path=[]):
    if root:
        postorder(root.left, path)
        postorder(root.right, path)
        path.append(root.val)
    return path

def print_tree(node, prefix="", is_left=True):
    if node:
        print(prefix + ("├── " if is_left else "└── ") + str(node.val))
        new_prefix = prefix + ("│   " if is_left else "    ")
        print_tree(node.left, new_prefix, True)
        print_tree(node.right, new_prefix, False)

# Build BST with given inputs
inputs = [15, 10, 12, 11, 20, 18, 16, 19]
root = None
for val in inputs:
    root = insert(root, val)

print("Binary Search Tree Structure:")
print_tree(root)
print("\nPreorder:", preorder(root, []))
print("Postorder:", postorder(root, []))