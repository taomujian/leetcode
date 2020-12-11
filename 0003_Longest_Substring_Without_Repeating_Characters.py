#!/usr/bin/env python3

class Solution(object):

    def lengthOfLongestSubstring(self, s):
        '''
        从字符串里找出来一个没有重复字符的最大字符串,并返回这个最大字符串的长度

        :param str s: 目标字符串
        
        :return str head.next: 最大字符串的长度
        '''
    
        charMap = {}         # 建立一个字符映射表
        # 初始化这个字符映射表
        for i in range(256):
            charMap[i] = -1

        ls = len(s)
        i = max_len = 0
        for j in range(ls):
            # 当某个字符在字符映射表的值大于i,说明这个字符之前已经出现过,需要更新i为上一次出现的位置
            if charMap[ord(s[j])] >= i:
                i = charMap[ord(s[j])] + 1

            charMap[ord(s[j])] = j  # 锁定字符出现的位置
            max_len = max(max_len, j - i + 1) # 根据重复字符出现的位置即i的值、当前循环的值即j的值和上一次循环得到的最大值进行比较得出最大值
        return max_len

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring('abcabcbb'))
