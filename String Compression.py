class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        #O(n)time O(1)space
        count = 1
        length = 0 #next starting place
        chars.append(' ') #make sure different when comparing with last char
        for i in range(len(chars) - 1):
            if chars[i] != chars[i + 1]:
                offsize = 1 + (len(str(count)) if count > 1 else 0)
                chars[length:length+offsize] = chars[i] + (str(count) if count > 1 else '')               
                length += offsize
                count = 1
            else:
                count += 1
        chars.pop()
        return length

# Given an array of characters, compress it in-place.
# The length after compression must always be smaller than or equal to the original array.
# Every element of the array should be a character (not int) of length 1.
# After you are done modifying the input array in-place, return the new length of the array.
# Follow up:
# Could you solve it using only O(1) extra space?

# Input:
# ["a","a","b","b","c","c","c"]
# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

# Input:
# ["a"]
# Output:
# Return 1, and the first 1 characters of the input array should be: ["a"]
# Explanation:
# Nothing is replaced.

# Input:
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output:
# Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation:
# Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
# Notice each digit has it's own entry in the array.

# Note:
# All characters have an ASCII value in [35, 126].
# 1 <= len(chars) <= 1000.