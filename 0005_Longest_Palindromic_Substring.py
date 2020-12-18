#!/usr/bin/env python3

class Solution(object):

    def longestPalindrome(self, s):
        '''
        找出一个字符串的最大长度的回文字符串

        :param str s: 要查找的字符串

        :return str result: 查找到的最大长度回文字符串
        '''
        
        ls = len(s)
        # 如果字符串长度为1或者为0,则结果就是其本身
        if ls <= 1 or len(set(s)) == 1:
            return s
        # 根据马拉车算法扩充字符串,即在字符串右边添加#符号,这并不是完整的马拉车算法,完整的马拉车算法需要在字符的左右两边都要加上#符号
        temp_s = '#'.join('{}'.format(s))

        tls = len(temp_s)
        seed = range(1, tls - 1)

        # 存储最大长度的回文的位置,元素的值是半径,元素的位置是最大长度回文中心点的位置
        len_table = [0] * tls
        # step是检测的半径长度
        for step in range(1, tls // 2 + 1):
            # final是用来存储上一次循环后检测相等的2个元素的中心点,即pos,这样就保证了在step即检测半径增加的时候,中心点pos小于这个半径的左右元素已经是相等的
            final = []
            # pos是中心位置,结合step这个半径来检测中心位置2侧的元素是否相等
            for pos in seed:
                # 如果检测的2个元素数组越界,则跳过
                if pos - step < 0 or pos + step >= tls:
                    continue
                # 如果检测的2个元素不相等,则跳过
                if temp_s[pos - step] != temp_s[pos + step]:
                    continue
                # 如果检测的2个元素相等,则记录其位置
                final.append(pos)
                # 虽然检测的2个元素相等,但是这2个元素是#符号,不记录位置
                if temp_s[pos - step] == '#':
                    continue
                # 检测的2个元素相等,且不是#符号,记录位置
                len_table[pos] = step
            seed = final
            
        max_pos, max_step = 0, 0
        # 找出最大回文的中心点和半径
        for i, s in enumerate(len_table):
            if s >= max_step:
                max_step = s
                max_pos = i
        # 删去#符号
        trans = str.maketrans({key: None for key in '#'})
        return temp_s[max_pos - max_step:max_pos + max_step + 1].translate(trans)

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("abcbe"))