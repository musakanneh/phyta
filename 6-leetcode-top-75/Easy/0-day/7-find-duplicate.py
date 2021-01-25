#!/usr/bin/python3


# Find duplicate number

def find_duplicate(number):
    for n in number:
        """Simple circle detection algorithm

        Floyd's algorithms

        """
        turtle = number[0]
        hare = number[0]
        while True:
            turtle = number[turtle]
            hare = number[number[hare]]
            if turtle == hare:
                break
        ptr_1 = number[0]
        ptr_2 = turtle
        while ptr_1 != ptr_2:
            ptr_1 = number[ptr_1]
            ptr_2 = number[ptr_2]
        return ptr_1


number = [1, 2, 3, 3, 4, 5]
print(find_duplicate(number))
