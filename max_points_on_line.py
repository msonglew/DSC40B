def max_points_on_line(X, p):
	"""
	Returns maximum number of points in X that fall 
	on same straight line containing p

	Params:
		X: list of 2-tuple of integers (points)
		p: qurey point, 2-tuple of integers

	Return:
		integer
		if X empty --> return 0

	# general case
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

	# empty set of points
	>>> X = []
	>>> p = (5, 5)
	>>> max_points_on_line(X, p)
	0

	# only identity point in set
	>>> X = [(5, 5)]
	>>> p = (5, 5)
	>>> max_points_on_line(X, p)
	1

	# identity point in set of other points
	>>> X = [
	... (1, 1),
	... (3, 1),
	... (5, 2),
	... (3, 6),
	... (1, 7),
	... (7, 4),
	... (9, 3),
	... (9, 9),
	... (5, 5)
	... ]
	>>> p = (5, 5)
	>>> max_points_on_line(X, p)
	5

	# multiple identity points
	>>> X = [
	... (1, 1),
	... (3, 1),
	... (5, 2),
	... (3, 6),
	... (1, 7),
	... (7, 4),
	... (9, 3),
	... (9, 9),
	... (5, 5),
	... (5, 5)
	... ]
	>>> p = (5, 5)
	>>> max_points_on_line(X, p)
	6
	"""

	def slope(a, b):
		"""
		returns slope between two points, a and b, (tuple format)
		returns 0 when first elements of points are the same
		"""

		if a[0] - b[0] == 0:
			return 0
		return (a[1] - b[1]) / (a[0] - b[0])

	if len(X) == 0:
		return 0

	# slopes has length equal to or less than len(X)
	slopes = {}
	identity_point = 0

	# hashing elements in X, counting identity points (points in X == p)
	for x in X:
		if x == p:
			identity_point += 1
			continue

		x_p_slope = slope(x, p)

		# add slope if not in table
		if x_p_slope not in slopes:
			slopes[x_p_slope] = 1
		# increment by 1 if slope in table
		else:
			slopes[x_p_slope] += 1

	# non-empty slopes
	if len(slopes) > 0:
		return max(slopes.values()) + identity_point
	# empty slopes
	return identity_point


