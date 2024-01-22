"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

"""

class Solution(object):
    def isValid(self, s):

        open_set = {'(', '{', '['}

        paren_dict = { ')' : '(', '}' : '{', ']' : '['}

        stack = []

        if s[0] not in open_set:
           return False

        for c in s:
            if c in open_set:
                stack.append(c)
            else:
                "Pop the stack, if it's correct opening is not what is on top of the stack, return false"
                if len(stack) == 0:
                    return False
                else:
                    close_char = stack.pop()
                    if close_char != paren_dict[c]:
                        return False

        if len(stack) == 0:
            return True
            

            