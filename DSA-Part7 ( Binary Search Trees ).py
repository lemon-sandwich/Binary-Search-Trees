# Binary Search Tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def Insert(root,node):
    if root is None:
        root = node
    else:
        if root.data == node.data:
            return
        if node.data < root.data:
            if root.left:
                Insert(root.left,node)
            else:
                root.left = node
        elif node.data > root.data:
            if root.right:
                Insert(root.right,node)
            else:
                root.right = node

def InOrder(node):
    if not node:
        return
    if node.left:
        InOrder(node.left)
    print(node.data, end = " ")
    if node.right:
        InOrder(node.right)

def PreOrder(node):
    if not node:
        return
    print(node.data, end = " ")
    if node.left:
        PreOrder(node.left)
    if node.right:
        PreOrder(node.right)

def PostOrder(node):
    if not node:
        return
    if node.left:
        PostOrder(node.left)
    if node.right:
        PostOrder(node.right)
    print(node.data, end = " ")

def Search(data,node):
    if node is None or data == node.data:
        return node
    if data < node.data:
        return Search(data,node.left)
    if data > node.data:
        return Search(data,node.right)

def find_min(node):
    if not node:
        return node
    if node.left is None:
        return node
    return find_min(node.left)

def find_max(node):
    if not node:
        return node
    if node.right is None:
        return node
    return find_max(node.right)

def calculate_sum(node):
    if node == None:
        return 0
    return ( node.data + calculate_sum(node.left) + calculate_sum(node.right) )

def delete(node,data):
    if node is None:
        return node
    elif data < node.data:
        node.left = delete(node.left,data)
    elif data > node.data:
        node.right = delete(node.right,data)
    else:
        if node.left and not node.right:
            temp = node
            node = node.right
            del temp
            return node
        elif node.right and not node.left:
            temp = node
            node = node.left
            del temp
            return node
        elif not node.left and not node.right:
            node = None
            return node
        else:
            temp = node.right
            while temp.left:
                temp = temp.left
            temp.left = node.left
            temp = node
            node = node.right
            del temp
            return node

if __name__ == "__main__":
    counter = 0
    root = None
    while True:
        op = "\0"
        print("1. Insert Value\n")
        print("2. Calculate Sum\n")
        print("3. InOrder Traversal\n")
        print("4. PreOrder Traversal\n")
        print("5. PostOrder Traversal\n")
        print("6. Search\n")
        print("7. Find Max\n")
        print("8. Find Min\n")
        print("9. Delete Value\n")
        print("Press Any Other Button To Exit The Program\n")
        op = input("Choose: ")
        print("\n")
        if op == '1':
            if root is None:
                root = Node(int(input(">> ")))
            else:
                n = Node(int(input(">> ")))
                Insert(root,n)
        elif op == '2':
            print("Sum:",calculate_sum(root))
        elif op == '3':
            print("InOrder Traversal\n")
            InOrder(root)
        elif op == '4':
            print("PreOrder Traversal\n")
            PreOrder(root)
        elif op == '5':
            print("PostOrder Traversal\n")
            PostOrder(root)
        elif op == '6':
            n = Search(int(input(">> ")),root)
            if n is None:
                print("Search Staus:",False)
            else:
                print("Search Status:", True)
        elif op == '7':
            n = find_max(root)
            if n is None:
                print("Max:",n)
            else:
                print("Max:",n.data)
        elif op == '8':
            n = find_min(root)
            if n is None:
                print("Min:",n)
            else:
                print("Min:",n.data)
        elif op == '9':
            root = delete(root,int(input(">> ")))
            print("Data deleted\n")
        else:
            break
        print("\n")


