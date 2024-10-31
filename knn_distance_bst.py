# BST method may take worst case Theta(n^2) time

class Node:
	def __init__ (self, key, distance, parent=None):
		self.key = key
		self.parent = parent
		self.left = None
		self.right = None
		self.size = 1
		self.distance = distance

class BinarySearchTree:
	def __init__(self, root: Node): # root expect type Node
		self.root = root

	def insert(self, new_key, q):
		#assume new_key is unique
		current_node = self.root
		parent = None
		new_dist = abs(new_key - q)

		# find place to insert the new node
		while current_node is not None:
			parent = current_node
			current_node.size += 1
			if current_node.distance < new_dist:
				current_node = current_node.right
			else:
				current_node = current_node.left

		# create the new node
		new_node = Node(key=new_key, distance=new_dist, parent=parent)

		# if parent is None, this is the root. Otherwise, update the
		# parent's left or right child as appropriate
		if parent is None:
			self.root = new_node
		elif parent.distance < new_dist:
			parent.right = new_node
		else: # parent > new
			parent.left = new_node

	def order_statistic(self, k, in_node=None):

		if in_node is None:
			node = self.root
		else:
			node = in_node

		if node.left is None:
			left_size = 0
		else:
			left_size = node.left.size

		order = left_size + 1

		if order == k:
			return node
		elif order < k:
			return self.order_statistic(k-order, node.right)
		else: # order > k
			return self.order_statistic(k, node.left)



def knn_distance(arr, q, k):
	"""
	In space R, find distance from query point to its kth closest neighbor

	Parameters:
		arr: list of numbers
		q: number, query point
		k: int, order statistic, minimum is k=1

	Return:
		tuple, (distance, point), of kth neighbor from q


	>>> knn_distance([3, 10, 52, 15], 19, 1)
	(4, 15)

	>>> knn_distance([3, 10, 52, 15], 19, 2)
	(9, 10)

	>>> knn_distance([3, 10, 52, 15], 19, 3)
	(16, 3)
	"""

	bst = BinarySearchTree(None)

	for i in arr:
		bst.insert(i, q)

	k_close = bst.order_statistic(k)

	return (k_close.distance, k_close.key)
