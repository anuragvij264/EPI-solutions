from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:

    def compare(leftSub,rightSub):

        if leftSub==None and rightSub==None: return True

        # elif (leftSub.data != rightSub.data): return False

        elif ( leftSub and rightSub):

           return compare(leftSub.left,rightSub.right) and compare(leftSub.right,rightSub.left)  and leftSub.data==rightSub.data
        else:
            return False

    if tree==None: return True

    return compare(tree.left,tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
