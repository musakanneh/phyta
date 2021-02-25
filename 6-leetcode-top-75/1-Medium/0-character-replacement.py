class Solution:
    """Longest Repeating Character Replacement
    Given a string s that consists of only uppercase English letters,
    you can perform at most k operations on that string.
    https://leetcode.com/problems/longest-repeating-character-replacement/
    
    """

    def character_replacement(self, s, k):
        """Use an empty string
        traverse the main string of letters
        and store update input string in the temp string.
        then return the length of the temp string
        
        """
        temp_string = ""
        for i in range(len(s))
        