# quickselect method, expected Theta(n)

import random

def in_place_partition(arr, start, stop, pivot_ix):
	def swap(ix_1, ix_2):
		arr[ix_1], arr[ix_2] = arr[ix_2], arr[ix_1]

	pivot = arr[pivot_ix]

	swap(pivot_ix, stop-1)

	middle_barrier = start

	for end_barrier in range(start, stop - 1):
		if arr[end_barrier] < pivot:
			swap(middle_barrier, end_barrier)
			middle_barrier += 1
		# else:
			# do nothing

	swap(middle_barrier, stop - 1)

	return middle_barrier

def quickselect(arr, k, start, stop):
	""" Finds kth order statistic in numbers [start:stop]"""
	
	pivot_ix = random.randrange(start, stop)
	pivot_ix = in_place_partition(arr, start, stop, pivot_ix)
	pivot_order = pivot_ix + 1

	if pivot_order == k:
		return arr[pivot_ix]
	elif pivot_order < k:
		return quickselect(arr, k, pivot_ix + 1, stop)
	else: # pivot_order > k
		return quickselect(arr, k, start, pivot_ix)

def knn_distance(arr, q, k):
	"""
	In space R, find distance from query point to its kth closest neighbor

	Parameters:
		arr: list of numbers
		q: number, query point
		k: int, order statistic, minimum is k=1

	Return:
		tuple, (distance, point), of kth neighbor from q

	# elem of arr is positive, q positive
	>>> knn_distance([3, 10, 52, 15], 19, 1)
	(4, 15)

	>>> knn_distance([3, 10, 52, 15], 19, 2)
	(9, 10)

	>>> knn_distance([3, 10, 52, 15], 19, 3)
	(16, 3)

	>>> knn_distance([3, 10, 52, 15], 19, 4)
	(33, 52)


	# elem of arr is negative, q positive
	>>> knn_distance([-6, -5, 4, 3], 2, 3)
	(7, -5)

	# elem of arr is negative, q negative
	>>> knn_distance([-6, -5, -4, -3], -7, 1)
	(1, -6)

	# elem of arr is positive, q negative
	>>> knn_distance([1, 2, 3, 4], -1, 2)
	(3, 2)

	# 2 elems same distance
	>>> knn_distance([-1, 2, 3], 1, 2)
	(2, 3)

	"""

	def dist(x):
		"""
		distance between a point, x, and q
  		"""
		return abs(x-q)

	# create (distance, point) pairs array
	distance_point_pairs = [(dist(x), x) for x in arr]
	return quickselect(distance_point_pairs, k, 0, len(arr))
