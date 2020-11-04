#!/usr/bin/env python3

class Two_Sum:

    def get_data(self, elem):
        """
        获取元组的最后一个元素
        
        :param tuple elem:  要寻找的元组
        :return int result: 元组的最后一个元素
        """
        
        result = elem[1]
        return result

    def run(self, nums, target):
        """
        寻找数组中二个元素之和为目标的元素的索引
        
        :param list nums: 要寻找的数组
        :param int target: 目标值
        :return list result: 数组中二个元素之和为目标的元素的索引列表
        """

        try:
            nums_index = [(index, value) for index, value in enumerate(nums)]
            nums_index.sort(key = self.get_data)    # 按照元组的最后一个元素排序,默认是按照第一个元素排序
            begin, end = 0, len(nums) - 1
            while begin < end:
                data_sum = nums_index[begin][1] + nums_index[end][1]
                if data_sum == target:
                    result = [nums_index[begin][0], nums_index[end][0]]
                    return result
                elif data_sum < target:
                    begin += 1
                else:
                    end -= 1
        except Exception as e:
            print(e)
        finally:
            pass
        

if __name__ == "__main__":
    two_sum = Two_Sum()
    print(two_sum.run([3, 2, 4], 6))

