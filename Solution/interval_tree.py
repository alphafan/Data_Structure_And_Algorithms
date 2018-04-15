from collections import namedtuple


Interval = namedtuple('Interval', 'start end price')


class TreeNode(object):

    def __init__(self, start, end, minPrice):
        self.left = None
        self.right = None
        self.start = start
        self.end = end
        self.minPrice = minPrice

    def __repr__(self):
        return '({}-{}-{})'.format(self.start, self.end, self.minPrice)


class IntervalTree(object):

    # -------------------------------------------------------------------
    # Insert an interval to tree
    # -------------------------------------------------------------------

    def insert(self, root: TreeNode, interval: Interval):
        """ Insert a new interval to tree.

        This function aims at building an interval tree by inserting
        intervals one by one to the root of tree.

        Each tree node contains 3 information: start, end time and minPrice.

        The interval tree is a binary search tree where the order
        is maintained by the start & end time, meaning that left child's
        end time is always earlier than the root's start time and, the right
        child's start time is always later than the root's end time.

        While inserting a new interval, the minPrice saved in the node is also
        updated by comparing with the price of new interval inserted.

        Examples of one node insertion:

        1) Root is (start: 2, end: 7, price: 10), insert a new node
            (start: 3, end: 8, price: 6).

                Before Insertion             After Insertion

                             Insert (3 - 8 - 6)
                2 - 7 - 10          -->         2 - 3 - 7
                                                        \
                                                     3 - 8 - 6

        Since the new interval ends at 8, it is located at right of current
        root, so we will insert a new node at its right child.

        By comparing the prices (new interval's price is smaller than the root's
        minPrice), we will change the data saved at root node and insert a new
        interval at its right.

        2) Root is (start: 2, end: 7, price: 10), new interval is (1 - 5 -7)

                Before Insertion                After Insertion

                            Insert (1 - 5 - 7)
                2 - 7 - 10          -->          5 - 7 - 10
                                                 /
                                            1 - 5 - 7

        3)
                Before Insertion                After Insertion

                            Insert (8 - 9 - 7)
                2 - 7 - 10          -->         2 - 7 - 10
                                                        \
                                                        8 - 9 - 7

        4)
                Before Insertion                After Insertion

                            Insert (0 - 1 - 7)
                2 - 7 - 10          -->         2 - 7 - 10
                                                /
                                        0 - 1 - 7

        5)
                Before Insertion                After Insertion

                            Insert (4 - 6 - 7)
                2 - 7 - 10          -->         4 - 6 - 7
                                              /            \
                                        2 - 4 - 10      6 - 7 - 10

        6)
                Before Insertion                After Insertion

                            Insert (1 - 10 - 7)
                2 - 7 - 10          -->         2 - 7 - 7
                                               /          \
                                        1 - 2 - 7       7 - 10 - 7

        ...

        Example of insert multi nodes.
        If we have multiple intervals (3, 5, 8), (1, 4, 6), (4, 6, 4), (1, 7, 5)

        Step 1):

                Before Insertion                After Insertion

                            Insert (1 - 4 - 6)
                3 - 5 - 8          -->         4 - 5 - 8
                                               /
                                        1 - 4 - 6

        Step 2):

                Before Insertion                After Insertion

                            Insert (4 - 6 - 4)
                4 - 5 - 8           -->             4 - 5 - 4
                /                                     /     \
            1 - 4 - 6                          1 - 4 - 6    5 - 6 - 4

        Step 3):

            3.1. Insert at root, the interval (1 - 7 - 5) is split into 3
            (1 - 4 - 5), (4 - 5 - 4), (5 - 7 - 5)

                Before Insertion                    After Insertion

                            Insert (1 - 7 - 5) at root
                4 - 5 - 4                                 4 - 5 - 4
                /         \                             /           \
            1 - 4 - 6    5 - 6 - 4      (1 - 4 - 5) + 1 - 4 - 6      5 - 6 - 4  + (5 - 7 - 5)

            3.2 Recursively insert at left child and right child

            Before Insertion                                                After Insertion

                                 Insert (1 - 4 - 5), (5 - 7 - 5) at left, right

                                4 - 5 - 4                                       4 - 5 - 4
                            /               \                                    /       \
            (1 - 4 - 5) + 1 - 4 - 6     5 - 6 - 4  + (5 - 7 - 5)           1 - 4 - 5     5 - 6 - 4
                                                                                             \
                                                                                             6 - 7 - 5

        Final tree structure of intervals (3, 5, 8), (1, 4, 6), (4, 6, 4), (1, 7, 5) is:

                4 - 5 - 4
                /       \
            1 - 4 - 5   4 - 6 - 4
                            \
                            6 - 7 - 5
        """
        if interval.start >= interval.end:
            return root
        if root is None:
            root = TreeNode(interval.start, interval.end, interval.price)
            return root
        if interval.end <= root.start:
            root.left = self.insert(root.left, interval)
        elif root.start < interval.end < root.end:
            if interval.start < root.start:
                if interval.price < root.minPrice:
                    root.start = interval.end
                    root.left = self.insert(root.left, interval)
                else:
                    root.left = self.insert(root.left, Interval(interval.start, root.start, interval.price))
            elif interval.start == root.start:
                if interval.price < root.minPrice:
                    root.start = interval.end
                    root.left = self.insert(root.left, interval)
            else:
                # Interval.start > root.start
                if interval.price < root.minPrice:
                    root.left = self.insert(root.left, Interval(root.start, interval.start, root.minPrice))
                    root.right = self.insert(root.right, Interval(interval.end, root.end, root.minPrice))
                    root.start, root.end, root.minPrice = interval.start, interval.end, interval.price
        elif interval.end == root.end:
            if interval.start < root.start:
                if interval.price < root.minPrice:
                    root.minPrice = interval.price
                root.left = self.insert(root.left, Interval(interval.start, root.start, interval.price))
            elif interval.start == root.start:
                root.minPrice = min(root.minPrice, interval.price)
            else:
                if interval.price < root.minPrice:
                    root.end = interval.start
                    root.right = self.insert(root.right, interval)
        elif interval.end > root.end:
            if interval.start < root.start:
                root.minPrice = min(root.minPrice, interval.price)
                root.left = self.insert(root.left, Interval(interval.start, root.start, interval.price))
                root.right = self.insert(root.right, Interval(root.end, interval.end, interval.price))
            elif interval.start == root.start:
                root.minPrice = min(root.minPrice, interval.price)
                root.right = self.insert(root.right, Interval(root.end, interval.end, interval.price))
            elif root.start < interval.start < root.end:
                if root.minPrice > interval.price:
                    root.end = interval.start
                    root.right = self.insert(root.right, interval)
                else:
                    root.right = self.insert(root.right, Interval(root.end, interval.end, interval.price))
            else:
                root.right = self.insert(root.right, interval)
        else:
            root.right = self.insert(root.right, interval)
        return root

    # -------------------------------------------------------------------
    # In-Order visit to get all lowest price intervals
    # -------------------------------------------------------------------

    _intervals = None

    def inorder(self, root: TreeNode):
        self._intervals = []
        self.inorderRec(root)
        return self._intervals

    def inorderRec(self, root: TreeNode):
        if root:
            self.inorderRec(root.left)
            self._intervals.append(Interval(root.start, root.end, root.minPrice))
            self.inorderRec(root.right)
