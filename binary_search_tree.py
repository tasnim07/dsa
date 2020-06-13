class BinarySearchTreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.data)
        in_order_traversal(root.right)


# find
# recrusive
def find(root, k):
    if not root:
        return None
    if root.data == k:
        return root
    if k < root.data:
        return find(root.left, k)
    else:
        return find(root.right, k)


def find_non_recursive(root, k):
    if not root:
        return None

    while root:
        if root.data == k:
            return root
        elif k < root.data:
            root = root.left
        else:
            root = root.right


# insert
def insert(root, k):
    '''Insert at the leaf node. Find and then insert'''
    new_node = BinarySearchTreeNode(data=k)
    # find
    if not root:
        root = new_node
        return root

    last_root = None

    temp = root

    while temp:
        if k == temp.data:
            return 'already present'
        elif k < temp.data:
            if temp:
                last_root = temp
            temp = temp.left
        else:
            if temp:
                last_root = temp
            temp = temp.right

    # insert
    if last_root:
        if k < last_root.data:
            last_root.left = new_node
        else:
            last_root.right = new_node

    return root


def find_minimum(root):
    if not root:
        return

    if root.left:
        root = find_minimum(root.left)

    return root


def find_minimum_non_recursive(root):
    if not root:
        return

    while root.left:
        root = root.left

    return root


def find_maximum(root):
    if not root:
        return

    if root.right:
        root = find_maximum(root.right)

    return root


def find_maximum_non_recursive(root):
    if not root:
        return

    while root.right:
        root = root.right

    return root


def delete(root, k):
    if not root:
        return

    # If the key to be deleted is smaller than the root's
    # key then it lies in left subtree
    if k < root.data:
        root.left = delete(root.left, k)
    # If the key to be deleted is greater than the root's key
    # then it lies in right subtree
    elif k > root.data:
        root.right = delete(root.right, k)
    # If key is same as root's key, then this is the node
    # to be deleted
    else:
        # Node with two children: Get the inorder predecessor
        # (maximum in the left subtree)
        if root.left and root.right:
            temp = find_maximum(root.left)
            # Copy the inorder predecessor's content to this node
            root.data = temp.data
            # Delete the inorder predecessor
            root.left = delete(root.left, root.data)
        else:
            # Node with only one child or no child
            temp = root
            if root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left

            del(temp)

    return root


def lowest_common_ancestor(root, k1, k2):
    '''Find Lowest Common Ancestor
    k1 and k2 are the data of 2 nodes.
    if k1 and k2 is less than the root, then LCA will be in left
    else LCA will be in right
    if root value is between k1 and k2, then root will be the LCA
    '''
    if not root:
        return

    if k1 >= k2:
        raise ValueError('k1 must be smaller than k2')

    if k1 < root.data and k2 > root.data:
        return root

    if k1 < root.data and k2 < root.data:
        return lowest_common_ancestor(root.left, k1, k2)

    else:
        return lowest_common_ancestor(root.right, k1, k2)


def find_shortest_path_bw_2_nodes(root, k1, k2):
    # It’s nothing but finding the LCA of two nodes in BST.
    return lowest_common_ancestor(root, k1, k2)
