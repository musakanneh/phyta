def  reverse_list(_list):
	left = 0
	right = len(_list) - 1
	while left < right:
		_list[left], _list[right] = _list[right], _list[left]
		right-= 1
		left += 1
	return _list

num = ["Musa", "Kanneh"]
print(reverse_list(num))


def string_concat(_string):
	pass