def largest_pectangle(h):
	"""Returns an integer representing the
	largest rectangle that can be formed within 
	the bounds of consecutive buildings.

	Approach:
		https://www.youtube.com/watch?v=QjdkTD0X5uU

	"""
	# stack = []
	# max_rectangle_sum = 0
	# left = 0
	
	# for left in range(len(h) - 1):
	# 	right = left + 1
	# 	res = h[left] + h[right]
	# 	if res > max_rectangle_sum:
 #    			max_rectangle_sum = res
 #    	left += 1
 #    	right += 1
	# return max_rectangle_sum

	# def largest_pectangle(h):
	stack = []
	area = i = 0
	h.append(0)
	while i < len(h):
		if not stack or h[stack[-1]] < h[i]:
			stack.append(i)
			i += 1
		else:
			top = stack.pop()
			area = max(area, h[top] * (i - stack[-1] - 1 if stack else i))
	return area

h = [1, 2, 3, 4, 5]
print(largest_pectangle(h))
