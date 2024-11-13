import dsc40graph
from collections import deque
	

def bfs(graph, source, status=None):
	""" Start a BFS at 'source'."""
	if status is None:
		status = {node: 'undiscovered' for node in graph.nodes}

	status[source] = 'good'
	pending = deque([source])

	# while there are still pending nodes
	while pending:
		u = pending.popleft()

		for v in graph.neighbors(u):
			# explore edge (u,v)

			if status[u] == status[v]:
				return None # IMPORTANT LINE----------------
			elif status[v] == 'undiscovered':
				if status[u] == 'good':
					status[v] = 'evil'
				else:
					status[v] = 'good'
				# append to right
				pending.append(v)

	return True

def assign_good_and_evil(graph):
	"""
	determines if possible to label each university as either "good" or "evil" 
	s.t. every rivalry is between a "good" school and an "evil" school

	Parameter:
		graph: type UndirectedGraph from dsc40graph package

	Return
	If the determinance of good/evil is possible, 
		return dictionary mapping each node to a string, 'good' or 'evil'
	If not determined, 
		return None

	# general case
	>>> example_graph = dsc40graph.UndirectedGraph()
	>>> example_graph.add_edge('Michigan', 'OSU')
	>>> example_graph.add_edge('USC', 'OSU')
	>>> example_graph.add_edge('USC', 'UCB')
	>>> example_graph.add_node('UCSD')
	>>> assign_good_and_evil(example_graph)
	{
		'OSU':'good',
		'Michigan', 'evil',
		'USC': 'evil',
		'UCB': 'good',
		'UCSD': 'good'
	}

	# labels undertermined
	>>> example_graph.add_edge('Michigan', 'USC')
	>>> assign_good_and_evil(example_graph)


	# graph of only unconnected nodes
	>>> example_graph2 = dsc40graph.UndirectedGraph()
	>>> example_graph2.add_node('UCB')
	>>> example_graph2.add_node('UCSD')
	>>> assign_good_and_evil(example_graph2)


	# graph of one node
	>>> example_graph3 = dsc40graph.UndirectedGraph()
	>>> example_graph3.add_node('UCSD')
	>>> assign_good_and_evil(example_graph3)


	# graph with two connected components
	>>> example_graph = dsc40graph.UndirectedGraph()
	>>> example_graph.add_edge('Michigan', 'OSU')
	>>> example_graph.add_edge('USC', 'OSU')
	>>> example_graph.add_edge('USC', 'UCB')
	>>> example_graph.add_edge('UCSD', 'SDSU')
	>>> assign_good_and_evil(example_graph)
	{
		'OSU':'good',
		'Michigan', 'evil',
		'USC': 'evil',
		'UCB': 'good',
		'UCSD': 'good',
		'SDSU': 'evil'
	}

	"""

	# full_bfs implementation

	status = {node: 'undiscovered' for node in graph.nodes}

	if len(graph.nodes) == 0 or len(graph.nodes) == 1 or len(graph.edges) == 0:
		return None

	for node in graph.nodes:
		if status[node] == 'undiscovered':
			valid = bfs(graph, node, status)

			if valid == None:
				return None

	return status
