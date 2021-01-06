def substr_count(n, s):
	"""A function that returns an integer representing
	the number of special substrings that can be formed 
	from the given string

	Approach:
	https://www.youtube.com/watch?v=fib2sRjlxuw

	"""
	result = 0
	i = 0
	while i < n:
		char_count = 1
		while (i + 1 < n and s[i] == s[i + 1]):
			i += 1
			char_count += 1
		result += int(char_count * (char_count + 1) / 2)
		i += 1
    
	for i in range(1, n):
		char_count = 1
		while (i + char_count < n and
			i - char_count >= 0 and
			s[i] != s[i - 1] and
			s[i - char_count] == s[i + char_count] and
			s[i - 1] == s[i - char_count]):
			char_count += 1
		result += char_count - 1
		return result
		