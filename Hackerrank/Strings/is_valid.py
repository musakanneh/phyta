from collections import Counter

def is_valid(string):
	"""A function that counts elements of s string
	and returns true if it's valid (having at most two frequencies)
	otherwise, returns false

	"""
	dic = Counter(string)
	if len(set(dic.values())) == 1:
		return "YES"
	elif len(set(dic.values())) > 2:
		return "NO"
	else:
		for key in dic:
			dic[key] -= 1
			temp = list(dic.values())
			try:
				temp.remove(0)
			except:
				pass
			if len(set(temp)) == 1:
				return "YES"
			else:
				dic[key] += 1
		return "NO"
s = "abcdefghhgfedecba"
print(is_valid(s))
