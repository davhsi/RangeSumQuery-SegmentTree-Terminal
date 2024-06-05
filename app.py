class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0
        self.left = None
        self.right = None
 
 
def createNode(start, end):
    return SegmentTreeNode(start, end)
 
 
def buildTree(arr, start, end):
    if start == end:
        leaf = createNode(start, end)
        leaf.sum = arr[start]
        return leaf
 
    root = createNode(start, end)
    mid = (start + end) // 2
    root.left = buildTree(arr, start, mid)
    root.right = buildTree(arr, mid + 1, end)
    root.sum = root.left.sum + root.right.sum
    return root
 
 
def rangeSumQuery(root, start, end):
    if root.start == start and root.end == end:
        return root.sum
 
    mid = (root.start + root.end) // 2
    if end <= mid:
        return rangeSumQuery(root.left, start, end)
    elif start > mid:
        return rangeSumQuery(root.right, start, end)
    else:
        return rangeSumQuery(root.left, start, mid) + rangeSumQuery(root.right, mid + 1, end)
 
 
def update(root, index, value):
    if root.start == root.end:
        root.sum = value
        return
 
    mid = (root.start + root.end) // 2
    if index <= mid:
        update(root.left, index, value)
    else:
        update(root.right, index, value)
 
    root.sum = root.left.sum + root.right.sum
 
 
if __name__ == "__main__":
    n = int(input("Enter the number of elements in the array: "))
    arr = [int(x) for x in input("Enter the elements of the array separated by space: ").split()]
    root = buildTree(arr, 0, n - 1)
 
    start, end = map(int, input("Enter the range for sum query (start and end index): ").split())
    print("Sum of elements in the range [{}, {}]: {}".format(start, end, rangeSumQuery(root, start, end)))
 
    index, value = map(int, input("Enter the index and value to update: ").split())
    update(root, index, value)
    print("Updated sum of elements in the range [{}, {}]: {}".format(start, end, rangeSumQuery(root, start, end)))