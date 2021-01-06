my_list = [0, 1, 2, 3, 4, 5]
for item in my_list:
    print("The value of item is: " + str(item))

# print("---------------------------------")
my_list1 = [80, 1, 2, 3, 4, 5]
for i, value in enumerate(my_list1):
    print("The idx is: " + str(i) + ". The val is: " + str(value))

# print("---------------------------------")
my_dict = {'Name': 'Musa', 'Age': '20', 'Height': '65.0'}
for key in my_dict:
    pass
    print(key + ' --> ' + my_dict[key])

# print("---------------------------------")
my_dict = {
    'a': [0, 1, 2, 3],
    'b': [0, 1, 2, 3],
    'c': [0, 1, 2, 3],
    'd': [0, 1, 2, 3]
}
i = 0
res = []
for item in my_dict:
    res.append(my_dict[item][i])
    i += 1
print(res)

# print("---------------------------------")


def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    smallest_pos = None
    for num in in_list:
        if num > 0:
            if smallest_pos == None or num < smallest_pos:
                smallest_pos = num
    return smallest_pos


# Test cases
print(smallest_positive([4, -6, 7, 2, -4, 10]))
print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))


def list_sort(my_list):
  my_list.sort()
  return len(my_list), my_list

print(list_sort([1, 2, 5, 3, -.1, 7, 7, 6]))


def all_even():
  n = 0
  while True:
    yield n
    n += 2

my_gen = all_even()
for i in range(5):
  pass
  # print(next(my_gen))

do_something = 4
do_something += 3
# print("Ans: ", do_something)
  
for i in range(10):
  pass
  # print(next(my_gen))

def prod(a, b):
  return a * b

def fact_gen():
  yield 

my_fact = fact_gen()

for i in range(10):
  print(next(my_fact))
