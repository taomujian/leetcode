#!/usr/bin/env python3

class ListNode:
    def __init__(self, val):
        '''
        初始化一个单链表结点

        :param str val: 结点的值
        
        :return:
        '''

        self.val = val
        self.next = None

class Solution:

    def addTwoNumbers(self, l1, l2):
        '''
        完成2个链表的相加,并倒序输出

        :param ListNode l1: 链表结点
        :param ListNode l2: 链表结点
        
        :return ListNode head.next: 相加结果的链表
        '''

        carry = 0
        head = curr = ListNode(0) #初始化2个链表结点,存放相加后的结果,head和curr都指向同一个链表
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry = carry // 10
        
        # 如果最后一次相加进位了,则要新开一个结点进1
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next

#if __name__ == "__main__":
    #solution = Solution()
    #solution.addTwoNumbers([2,4,3], [5,6,4])