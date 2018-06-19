"""
This module represents trees implementation.
"""


class BinaryTreeElement:
    """
    This class describes a binary tree element
    """
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def set_value(self, data):
        self.data = data

    def get_value(self):
        return self.data

    def set_left(self, left):
        self.left = left

    def get_left(self):
        return self.left

    def set_right(self, right):
        self.right = right

    def get_right(self):
        return self.right

    def __str__(self):
        return str(self.data)


class BinaryTree:
    """
    This class describes a binary tree
    """
    def __init__(self):
        self.root = None


class BinarySearchTree:
    """
    This class describes a binary search tree
    """
    def __init__(self):
        self.root = None

    def __str__(self):
        """
        This method performs in-order traversal and
        prints the nodes of the tree.
        :return:
        """
        self.print_inorder(self.root)

    def get_root(self):
        return self.root

    def insert(self, data):
        """
        Inserts the object into the sorted binary tree.
        :param data:
        :return:
        """
        new_element = BinaryTreeElement(data)

        # Consider a special case for empty tree
        if self.root is None:
            self.root = new_element
        else:
            # Determine the palce for the node
            current_node = self.root
            while True:
                if data < current_node.data:
                    # If the value is less then the data has to be
                    # placed in the left branch
                    if not current_node.left:
                        current_node.left = new_element
                        break
                    else:
                        current_node = current_node.left
                else:
                    # If the data is more than current node,
                    #  place it into the right branch
                    if not current_node.right:
                        current_node.right = new_element
                        break
                    else:
                        current_node = current_node.right
        return

    def print_inorder(self, node):
        """
        Prints the tree inorder:
        > all_left -> middle -> all right
        :return:
        """
        if node:
            self.print_inorder(node.left)
            print(node.data)
            self.print_inorder(node.right)


    def print_preorder(self, node):
        """
        Prints the tree preorder:
        > root > left > right
        :return:
        """
        if node:
            print(node.data)
            self.print_preorder(node.left)
            self.print_preorder(node.right)

    def print_postorder(self, node):
        """
        Prints the tree preorder:
        > root > left > right
        :return:
        """
        if node:
            self.print_postorder(node.left)
            self.print_postorder(node.right)
            print(node.data)

    def print_preorder_iterative(self, node):
        """
        Prints the tree preorder:
        > left > right > root
        :return:
        """
        if node is None:
            return
        else:
            queue = []
            queue.append(node)

            while len(queue):
                node = queue.pop(-1)
                print (node.get_value())
                if node.get_right():
                    queue.append(node.get_right())
                if node.get_left():
                    queue.append(node.get_left())

    def get_max_depth(self, node):
        """
        This method calculates the tree depth.
        :param node:
        :return:
        """
        if node:
            return 1 + max(self.get_max_depth(node.left),
                           self.get_max_depth(node.right))
        else:
            return 0


    def find_lowest_common_ancestor(self, root, data1, data2):
        """
        This task implies that you are given two values of the
        nodes that exist in the tree and you need to find a lowest
        common ancestor. Knowing the property of the BST the lowest
        common ancestor will be a value that is in between data1
        and data 2
        :param root:
        :param data1:
        :param data2:
        :return:
        """
        node = root
        while node:
            # Return is the tree is empty or values don't exist
            if node is None:
                return None

            if node.get_value() < data1 and node.get_value() < data2:
                node = node.get_right()
            elif node.get_value() > data1 and node.get_value() > data2:
                node = node.get_left()
            else:
                return node

    def get_balance_factor(self, root):
        """
        This method calculates the balance factor of the tree of
        the subtree for the specified root.
        :return:
        """
        if root is None:
            return None
        else:
            return self.get_max_depth(root.get_right()) - self.get_max_depth(root.get_left())

    def rotate_right(self, node):
        """
        This method rotates the tree to the right.
        :param node:
        :return:
        """
        new_root = node.get_right()
        node.set_right(new_root.get_left())
        new_root.set_left(node)
        return new_root

    def rotate_left(self, node):
        """
        This method rotates the tree to the left.
        :param node:
        :return:
        """
        new_root = node.get_left()
        node.set_left(new_root.get_right())
        new_root.set_right(node)
        return new_root

    def traverse_tree(self):
        """
        This method traverses the tree
        :return:
        """
        pass

    def balance_tree(self, node):
        """
        This method re-balances the tree by applying tree rotations
        :return:
        """
        if node is None:
            return

        b = self.get_balance_factor(node)
        if b > 0:
            node = self.rotate_right(node)
        elif b < 0:
            node = self.rotate_left(node)

        # Recursively balance for all children
        self.balance_tree(node.get_left())
        self.balance_tree(node.get_right())



if __name__=="__main__":
    # Test binary tree
    a = [10, 2, 45, 12, 6, 4, 5, 1, 3, 25, 55]
    t = BinarySearchTree()
    for aa in a:
        t.insert(aa)

    print("\nDepth:")
    print(t.get_max_depth(t.get_root()))

    print("\nPreorder:")
    t.print_preorder_iterative(t.get_root())
    print ("Balance factor = {0}".format(t.get_balance_factor(t.get_root())))

    print("\nRebalance the tree:")
    t.balance_tree(t.get_root())
    print("\nPreorder:")
    t.print_preorder_iterative(t.get_root())
    print ("Balance factor = {0}".format(t.get_balance_factor(t.get_root())))
