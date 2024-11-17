import dsc40graph

def biggest_descendent(graph, root, value):
	"""
	Define biggest descendent value of node to be largest value of any node 
	which is descendent of u in the tree (consider u to be descendent of itself)


	Parameters:
		graph: instance of dsc40graph.DirectedGraph(), tree
			node: 
				value: value for each node
	accepts graph, label of root node, dictionary of values

	Returns:
		dictionary mapping each node in graph to its biggest descendent value

	# general case
	>>> edges = [(1, 2), (1, 3), (2, 4), (2, 5), (4, 8), (4, 9), (3, 6), (3, 7)]
	>>> g = dsc40graph.DirectedGraph()
	>>> for edge in edges: g.add_edge(*edge)
	>>> value = {1: 2, 2: 1, 3: 4, 4: 8, 5: 5, 6: 2, 7: 10, 8: 3, 9: 9}
	>>> biggest_descendent(g, 1, value)
	{1: 10, 2: 9, 3: 10, 4: 9, 5: 5, 6: 2, 7: 10, 8: 3, 9: 9}

	# largest at top
	>>> edges = [(1, 2), (1, 3), (2, 4), (2, 5), (4, 8), (4, 9), (3, 6), (3, 7)]
	>>> g = dsc40graph.DirectedGraph()
	>>> for edge in edges: g.add_edge(*edge)
	>>> value = {1: 100, 2: 1, 3: 4, 4: 8, 5: 5, 6: 2, 7: 10, 8: 3, 9: 9}
	>>> biggest_descendent(g, 1, value)
	{1: 100, 2: 9, 3: 10, 4: 9, 5: 5, 6: 2, 7: 10, 8: 3, 9: 9}

	# largest in middle
	>>> edges = [(1, 2), (1, 3), (2, 4), (2, 5), (4, 8), (4, 9), (3, 6), (3, 7)]
	>>> g = dsc40graph.DirectedGraph()
	>>> for edge in edges: g.add_edge(*edge)
	>>> value = {1: 2, 2: 100, 3: 4, 4: 8, 5: 5, 6: 2, 7: 10, 8: 3, 9: 9}
	>>> biggest_descendent(g, 1, value)
	{1: 100, 2: 100, 3: 10, 4: 9, 5: 5, 6: 2, 7: 10, 8: 3, 9: 9}

	# more than one child
	>>> edges = [(1, 2), (1, 3), (1, 4)]
	>>> g = dsc40graph.DirectedGraph()
	>>> for edge in edges: g.add_edge(*edge)
	>>> value = {1: 2, 2: 1, 3: 4, 4: 8}
	>>> biggest_descendent(g, 1, value)
	{1: 8, 2: 1, 3: 4, 4: 8}

	"""

	# use dfs implementation

	def dfs(graph, u, value, status=None):
		"""Start a DFS at 'u'."""
		# initialize status if it was not passed
		if status is None:
			status = {node: 'undiscovered' for node in graph.nodes}

		status[u] = 'pending'
		child_values = list()
		child_values.append(value[u])

		for v in graph.neighbors(u): # explore edge (u, v)
			if status[v] == 'undiscovered':
				
				dfs(graph, v, value, status)
				child_values.append(value[v])

		value[u] = max(child_values)

		# print("call to dfs -----------")
		# print("child_values: "+str(child_values))
		# print("max: "+str(max(child_values)))


	dfs(graph, root, value)

	return value