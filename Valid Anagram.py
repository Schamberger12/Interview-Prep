"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

"""

class Solution(object):
    def isAnagram(self, s, t):      
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 2 approaches to this:
        # 1: Sort both strings, loop through and check
        #    NB: Slower - O(nlogn) as soon as we sort
        # 2: Create 2 hash tables of key->value pair of character->count
        #    Loop through the keys, and check if the counts are the same for each character
        #    NB: Faster - O(n)

        # Going with the faster approach
        if len(s) != len(t):
            return False
        
        # Create 2 hash tables that will hold character: count pairings
        count_s = {}
        count_t = {}

        # Get the character count into each hash table
        for i in range(len(s)):
            if s[i] in count_s:
                count_s[s[i]] += 1
            else:
                count_s[s[i]] = 1

            if t[i] in count_t:
                count_t[t[i]] += 1
            else:
                count_t[t[i]] = 1

        # loop through the keys in dictionary count_s
        # if the key doesn't exist in count_t or the counts are off, return false. 
        for key in count_s:
            if key not in count_t:
                return False
            elif count_s[key] != count_t[key]:
                return False
        return True
            
            