# 23 Merge k sorted lists

__author__ = 'Yang Xuan (jumpthepig@gmail.com)'


import sys
from Queue import PriorityQueue
sys.path.append('.')
from schema import time_it
from schema import Node as ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    @classmethod
    @time_it
    def mergeKLists(self, lists):
        nums = []
        for ll in lists:
            while ll:
                nums.append(ll.val)
                ll = ll.next

        nums.sort()

        dump = ListNode(2524)
        temp = dump
        for item in nums:
            temp.next = ListNode(item)
            temp = temp.next
        return dump.next

    def pq(self, lists):
        '''Using pq'''
        dump = ListNode(2524)
        pointer = dump
        q = PriorityQueue()

        for index, ll in enumerate(lists):
            if ll:
                q.put((ll.val, index, ll))
        while not q.empty():
            val, index, node = q.get()
            pointer.next = ListNode(val)
            pointer = pointer.next

            node = node.next
            if node:
                q.put((node.val, index, node))
        return dump.nextef priority_queue(self, lists):