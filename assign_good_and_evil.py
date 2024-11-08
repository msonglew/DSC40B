import dsc40graph


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
	>>> example_graph.add_edge('Michigan', "OSU')
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
	None

	# graph of only unconnected nodes
	>>> example_graph2 = dsc40graph.UndirectedGraph()
	>>> example_graph2.node('UCB')
	>>> example_graph2.node('UCSD')
	>>> assign_good_and_evil(example_graph2)
	None

	# graph of one node
	>>> example_graph3 = dsc40graph.UndirectedGraph()
	>>> example_graph3.node('UCSD')
	>>> assign_good_and_evil(example_graph3)
	None

	# graph with two connected components
	>>> example_graph = dsc40graph.UndirectedGraph()
	>>> example_graph.add_edge('Michigan', "OSU')
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