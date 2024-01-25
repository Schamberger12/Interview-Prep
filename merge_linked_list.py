
"""
21. Merge Two Sorted Lists
Solved
Easy
Topics
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Create a starting node, will be set to null
        list_node = ListNode()
        # Need to encapsulate that node into a list. 
        new_list = list_node
        listone = list1
        listtwo = list2

        while listone and listtwo:
            if listone.val < listtwo.val:
                new_list.next = listone
                listone = listone.next
            else:
                new_list.next = listtwo
                listtwo = listtwo.next
            new_list = new_list.next

        if listone:
            new_list.next = listone
        elif listtwo:
            new_list.next = listtwo
        #Return the 2nd node we point to. 
        return list_node.next