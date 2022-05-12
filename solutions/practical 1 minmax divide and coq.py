import sys

# Divide and conquer solution to find the minimum and maximum number in a list
def findMinAndMax(nums, left, right, min=sys.maxsize, max=-sys.maxsize):

	# if the list contains only one element

	if left == right:   			# common comparison

		if min > nums[right]:  		# comparison 1
			min = nums[right]

		if max < nums[left]:   		# comparison 2
			max = nums[left]

		return min, max

	# if the list contains only two elements

	if right - left == 1:   		# common comparison

		if nums[left] < nums[right]:  	# comparison 1
			if min > nums[left]:   	# comparison 2
				min = nums[left]

			if max < nums[right]:  	# comparison 3
				max = nums[right]

		else:
			if min > nums[right]:  	# comparison 2
				min = nums[right]

			if max < nums[left]:   	# comparison 3
				max = nums[left]

		return min, max

	# find the middle element
	mid = (left + right) // 2

	# recur for the left sublist
	min, max = findMinAndMax(nums, left, mid, min, max)

	# recur for the right sublist
	min, max = findMinAndMax(nums, mid + 1, right, min, max)

	return min, max


if __name__ == '__main__':

	nums = [7, 2, 9, 3, 1, 6, 7, 8, 4]

	# initialize the minimum element by INFINITY and the
	# maximum element by -INFINITY
	(min, max) = findMinAndMax(nums, 0, len(nums) - 1)

	print("The minimum element in the list is", min)
	print("The maximum element in the list is", max)
