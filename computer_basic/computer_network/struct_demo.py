# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：TEST -> struct_demo
@IDE    ：PyCharm
@Author ：Mr. Wang
@Date   ：2020/3/8 11:45 下午
@Desc   ：
=================================================='''
import struct

bin_str=b'ABCD1234'
print(bin_str)
result = struct.unpack('>BBBBBBBB', bin_str)
print(result)
result = struct.unpack('>HHHH', bin_str)
print(result)