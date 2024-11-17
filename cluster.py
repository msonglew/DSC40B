import dsc40graph

def cluster(graph, weights, level):
	"""
	Given a weighted, undirected graph G = (V,E,w), 
	edge weights represent similarity.

	Given number (gamma), say clusters of G are connected components of 
	graph after all edges whose weight is less than (gamma) have been removed.

	Parameters:
		graph: instance of dsc40graph.UndirectedGraph
		weights(u, v): function returning weight of edge (u, v)
		level: int represent level at which to find the clusters

	Return:
		a frozenset containing frozensets
			inner frozensets should contain notes in a cluster

	# general case
	>>> edges = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a')]
	>>> graph = dsc40graph.UndirectedGraph()
	>>> for edge in edges: graph.add_edge(*edge)
	>>> def weights(x, y):
	... x, y = (x, y) if x < y else (y, x)
	... return {("a", "b"): 1, ("b", "c"): .3, ("c", "d"): .9, ("a", "d"): .2}[(x, y)]
	>>> cluster(graph, weights, 0.4)
	frozenset([frozenset(['a', 'b']), frozenset(['c', 'd'])])

	# weight makes unconnected graph
	>>> cluster(graph, weights, 1)
	frozenset([frozenset(['a', 'b']), frozenset(['c']), frozenset(['d'])])

	# unconnected graph
	>>> graph.add_edge('e', 'f')
	>>> def weights(x, y):
	... x, y = (x, y) if x < y else (y, x)
	... return {("a", "b"): 1, ("b", "c"): .3, ("c", "d"): .9, ("a", "d"): .2, ("e", "f"): .5}[(x, y)]
	>>> cluster(graph, weights, 0.4)
	frozenset([frozenset(['a', 'b']), frozenset(['c', 'd']), frozenset(['e', 'f'])])
	
	"""

	# implement a modified full bfs/dfs with with a guard case
	# i.e. continue only if edge weight is valid

	


