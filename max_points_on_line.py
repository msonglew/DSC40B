def max_points_on_line(X, p):
	"""
	Returns maximum number of points in X that fall on same straight line containing p

	Params:
		X: list of 2-tuple of integers (points)
		p: qurey point, 2-tuple of integers

	Return:
		integer
		if X empty --> return 0

	>>> X = [
	... (1, 1),
	... (3, 1),
	... (5, 2),
	... (3, 6),
	... (1, 7),
	... (7, 4),
	... (9, 3),
	... (9, 9)
	... ]
	>>> p = (5, 5)
	>>> max_points_on_line(X, p)
	4

	>>> X = []
	>>> p = (5, 5)
	>>> max_points_on_line(X, p)
	0

	>>> X = [(5, 5)]
	>>> p = (5, 5)
	>>> max_points_on_line(X, p)
	1

	"""