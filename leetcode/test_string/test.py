import math


def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
    ns = nums.sort()
    dict = {}
    for i, n in enumerate(ns):
        if n not in dict:
            dict[n] = i
    lst = []
    for n in nums:
        lst.append(dict[n])
    return lst

if __name__ == '__main__':
    pass
