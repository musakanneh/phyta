from collections import Counter

class Solution(object):
    def stock_merchant(self, n, ar):
        """
        A return an integer representing the 
        number of matching pairs of socks that 
        are available.
        """
        unique_pair = 0
        for val in Counter(ar).values():
            unique_pair = unique_pair + val // 2
        return  unique_pair


    def counting_valleys(self, steps, paths):
        """
        Given the sequence of up and down steps 
        during a hike, find and print the number 
        of valleys walked through.
        """
        altitude = 0
        num_valleys = 0
        for step in steps:
            if paths[step] == 'U':
                if altitude == -1:
                    num_valleys += 1
                altitude += 1
            if paths[step] == 'D':
                altitude -= 1
        return num_valleys

    def jumping_on_clouds(self, c):
        """
        """
        pass
