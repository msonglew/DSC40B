import dsc40graph
import dsf

# Test print statements
TEST = False

def slc(graph, d, k):
	"""
	Perform single linkage clustering using Kruskal's algorithm

	Parameters:
		graph: 
			instance of dsc40graph.UndirectedGraph
		d: 
			function of one argument: tuple containing a pair of nodes. 
			returns distance (dissimilarity between them)
		k: 
			positive integer describing number of clusters which should be found

	Return:
		frozenset of k frozensets, each representing cluster of graph

	>>> g = dsc40graph.UndirectedGraph()
	>>> edges = [('a', 'b'), ('a', 'c'), ('c', 'd'), ('b', 'd')]
	>>> for edge in edges: g.add_edge(*edge)
	>>> def d(edge):
	...		u, v = sorted(edge)
	...		return {
	...			('a', 'b'): 1,
	...			('a', 'c'): 4,
	...			('b', 'd'): 3,
	...			('c', 'd'): 2,
	...		}[(u, v)]
	>>> slc(g, d, 2)
	frozenset({frozenset({'a', 'b'}), frozenset({'c', 'd'})})
	
	>>> slc(g, d, 4)
	frozenset({frozenset({'a'}), frozenset({'b'}), frozenset({'c'}), frozenset({'d'})})

	>>> slc(g, d, 3)
	frozenset({frozenset({'a', 'b'}), frozenset({'c'}), frozenset({'d'})})

	>>> slc(g, d, 1)
	frozenset({frozenset({'a', 'b', 'c', 'd'})})
	"""

	# implement rudimentary Disjoint Set structure
	def fs_find(sets, element):
		for s in sets:
			if element in s:
				return s
		return None

	def fs_union(sets, a, b):

		set_a = fs_find(sets, a)
		set_b = fs_find(sets, b)

		sets.remove(set_a)
		sets.remove(set_b)

		sets.add(set_a.union(set_b))

	# kruskals and terminate early when number of components is k
	# make frozenset structure for disjoint sets similar.

	fs = set([])
	for node in graph.nodes:
		fs = fs.union([frozenset([node])])

	if len(fs) == k: # when k is number of nodes
		return fs

	if TEST == True:
		print(fs)

	components = dsf.DisjointSetForest(graph.nodes)
	sorted_edges = sorted(graph.edges, key=d)

	for (u, v) in sorted_edges:
		if not components.in_same_set(u, v):
			components.union(u, v)
			fs_union(fs, u, v)
			
			if TEST == True:
				print(fs)

			if len(fs) == k:
				break

	return frozenset(fs)