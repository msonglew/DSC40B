def density(bin_points, total_points, bin_width):
	"""
	Returns: bin density

	Parameters: 
		bin_points: int, number of points in a bin
		total_points: int, total number of points in a dataset
		bin_width: int

	# note: denominator will never be 0, total_points and bin_width not 0

	# general case
	>>> density(2, 2, 5)
	0.2

	# numerator 0
	>>> density(0, 2, 5)
	0.0

	# improper fraction
	>>> density(24, 2, 4)
	3.0

	"""

	return bin_points / (total_points * bin_width)

def histogram(points, bins):
	"""
	Returns: list of bin densities

	Parameters:
		points: list, sorted list of n numbers, smallest to largest
		bins: list (nested tuples), list of k-tuples (a,b) where bins are [a,b)

	# given test case
	>>> points = [1,2,3,6,7,9,10,11]
	>>> bins = [(0,4), (4,8), (8,12)]
	>>> histogram(points,bins)
	[0.09375, 0.0625, 0.09375]

	# for bins different sizes, and test bin half-open intervals
	>>> points = [1,2,3,6,7,9,10,11]
	>>> bins = [(0,3), (3,9), (9,12)]
	>>> histogram(points,bins)
	[0.08333333333333333, 0.0625, 0.125]

	# empty list of points
	>>> points = []
	>>> bins = [(0,4), (4,8), (8,12)]
	>>> histogram(points,bins)
	[]

	# empty list of bins
	>>> points = [1,2,3,6,7,9,10,11]
	>>> bins = []
	>>> histogram(points,bins)


	"""
	
	tot_bins = len(bins)
	tot_pts = len(points)
	num_pts = 0

	if tot_bins == 0:
		return
	
	i = 0

	low, high = bins[i][0], bins[i][1]
	width = high - low

	output = []

	for pt in points:
		if (low <= pt) and (pt < high):
			num_pts += 1
			if pt == points[tot_pts-1]:
				output.append(density(num_pts, tot_pts, width))
				return output

		else:
			output.append(density(num_pts, tot_pts, width))

			num_pts = 1
			i += 1
			low, high = bins[i][0], bins[i][1]
			width = high - low

	return output