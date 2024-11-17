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

	>>> edges = [(1, 2), (1, 3), (2, 4), (2, 5), (4, 8), (4, 9), (3, 6), (3, 7)]
	>>> g = dsc40graph.DirectedGraph()
	>>> for edge in edges: g.add_edge(*edge)
	value = {1: 2, 2: 1, 3: 4, 4: 8, 5: 5, 6: 2, 7: 10, 8: 3, 9: 9}
	>>> biggest_descendent(g, 1, value)
	{1: 10, 2: 9, 3: 10, 4: 9, 5: 5, 6: 2, 7: 10, 8: 3, 9: 9}
	"""

	# use dfs implementation