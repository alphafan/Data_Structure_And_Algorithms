from .interval_tree import Interval, IntervalTree, TreeNode


def lowest_price_intervals(intervals):
    if len(intervals) <= 1:
        return intervals
    # 1) Build Interval Tree
    root = TreeNode(start=intervals[0].start, end=intervals[0].end, minPrice=intervals[0].price)
    tree = IntervalTree()
    for interval in intervals[1:]:
        root = tree.insert(root, interval)
    # 2) In-Order visit to get all lowest price intervals
    intervals = tree.inorder(root)
    # 3) Merge same price intervals.
    # i.e. (1 - 3 - 5), (3 - 4 - 5) --> (1, 4, 5)
    merged = []
    for interval in intervals:
        if not merged or interval.price != merged[-1].price or interval.start != merged[-1].end:
            merged.append(interval)
        else:
            merged[-1] = Interval(merged[-1].start, interval.end, interval.price)
    return merged
