'''
GCD of string
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"

Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"

Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"

Output: ""

Example 4:

Input: str1 = "AAAAAB", str2 = "AAA"

Output: ""​​​​​​​

 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
'''
from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If concatenations are different, no common divisor exists
        if str1 + str2 != str2 + str1:
            return ""

        # Find GCD of the lengths
        gcd_len = gcd(len(str1), len(str2))

        # Return the prefix of that length
        return str1[:gcd_len]


s = Solution()
str = s.gcdOfStrings("ABCABC", "ABC")
print('gcd = '+ str)