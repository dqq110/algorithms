class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
#前序遍历(先遍历根节点,在遍历左子树,再遍历右子树)
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

#中序遍历(先遍历左子树,再遍历根节点,再遍历右子树)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
#后序遍历(先遍历左子树,在遍历右子树,再遍历根节点)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
#测试程序
# 已知一颗二叉树的先序遍历序列为ABCDEFG，中序遍历为CDBAEGF，
# 能否唯一确定一颗二叉树？如果可以，请画出这颗二叉树。
def buildTree(preorder,inorder):
    if len(preorder) == 0:
        return None
    if len(preorder) == 1:
        return TreeNode(preorder[0])
    root = TreeNode(preorder[0])
    index = inorder.index(root.val)
    root.left = buildTree(preorder[1:index + 1],inorder[0: index])
    root.right = buildTree(preorder[index + 1:len(preorder)],inorder[index + 1 : len(inorder)])
    return root

r = buildTree('ABCDEFG','CDBAEGF')
preorder(r)
inorder(r)
postorder(r)