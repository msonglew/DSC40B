

def learn_theta(data, colors):
	"""
	Returns single number Theta such that all of the blue points and less than equal
	and all of the red points are greater than

	Parameters:
		data:
			list of n unique real numbers
		colors:
			list of n strings, such that colors[i] gives color of data[i]

	>>> d = [0, 5, 1, 4, 2]
	>>> c = ['blue', 'red', 'blue', 'red', 'blue']
	>>> learn_theta(d, c)
	2

	"""

	# find max blue and min red, return max blue or avg

	max_blue = float('-inf')
	# min_red = float('inf')

	for i in range(len(data)):
		if (colors[i] == 'blue') and (data[i] > max_blue):
				max_blue = data[i]

		# elif (colors[i] == 'red') and (data[i] < min_red):
		# 		min_red = data[i]

	return max_blue


def compute_ell(data, colors, theta):
	"""
	Parameters:
		data:
			as above
		colors:
			as above
		theta:
			float

	Return:
		Loss at theta as a float

	>>> d = [1, 4, 2, 7, 3, 6, 8]
	>>> c = ['blue', 'red', 'blue', 'red', 'blue', 'blue', 'red']
	>>> compute_ell(d, c, 5)
	2
	"""

	# count number of blue > Theta
	# count number of red <= Theta
	ell = 0

	for i in range(len(data)):
		if colors[i] == 'blue' and data[i] > theta:
			ell += 1
		elif colors[i] == 'red' and data[i] <= theta:
			ell += 1

	return ell


def minimize_ell(data, colors):
	"""
	Parameters:
		same as above

	Returns float which minimizes loss L for that particular data set

	Time: Theta(n^2)

	Assume smallest point is blue

	>>> d = [1, 4, 2, 7, 3, 6, 8]
	>>> c = ['blue', 'red', 'blue', 'red', 'blue', 'blue', 'red']
	>>> minimize_ell(d, c)
	3.0

	"""

	min_ell = float('inf')
	min_theta = float('-inf')

	for i in range(len(data)):
		ell = compute_ell(data, colors, data[i])

		if ell < min_ell:
			min_ell = ell
			min_theta = data[i]

	return float(min_theta)


def minimize_ell_sorted(data, colors):
	"""
	Parameters:
		same as above

	Returns:
		minimizer Theta

	Time: Theta(n)

	Assume exactly n/2 of data points are 'red', and n/2 are 'blue'
	(means only even input)

	>>> d = [1, 2, 3, 4, 6, 7, 8, 9]
	>>> c = ['blue', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'red']
	>>> minimize_ell_sorted(d, c)
	4.0

	>>> d = [1, 2, 3, 4, 6, 7, 8, 9]
	>>> c = ['blue', 'blue', 'blue', 'red', 'blue', 'red', 'red', 'red']
	>>> minimize_ell_sorted(d, c)
	3.0

	>>> d = [1, 2, 3, 4, 6, 7, 8, 9]
	>>> c = ['blue', 'blue', 'red', 'red', 'blue', 'blue', 'red', 'red']
	>>> minimize_ell_sorted(d, c)
	2.0

	"""

	# # blue on right is greater than # red on left

	# loss = # blue on right + # red on left

	blue_gt_theta = len(data) / 2
	red_lt_theta = 0

	ell = float('inf')
	ell_index = float('-inf')

	for i in range(len(data)):
		if colors[i] == 'blue':
			blue_gt_theta -= 1
		elif colors[i] == 'red':
			red_lt_theta += 1

		test_ell = blue_gt_theta + red_lt_theta

		if test_ell < ell:
			ell = test_ell
			ell_index = i
		elif test_ell >= ell:
			break

	return float(data[ell_index])
