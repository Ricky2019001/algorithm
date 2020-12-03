# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：TEST -> parser
@IDE    ：PyCharm
@Author ：Mr. Wang
@Date   ：2020/3/8 11:57 下午
@Desc   ：
=================================================='''
import struct
import socket

# IP报文解析器

class IPParser:

    IP_HEADER_LENGTH =20

    @classmethod
    def parse_ip_header(cls, ip_header):
        '''
        1. 4位版本 4位首长 8位服务类型 16位总长度
        2. 16位标识 3位标志 13位片偏移
        3. 8位生存时间 8位协议 16位交验和
        4. 32 原地址
        5. 32 目的地址
        :param ip_header:
        :return:
        '''
        line = struct.unpack('>BBH', ip_header[:4])
        # 11110000 =》1111
        ip_version = line[0]>>4
        ip_length = line[0] & 15
        packet_length = line[2]

        line3 = struct.unpack('>BBH', ip_header[8:12])
        TTL = line3[0]
        protocol = line3[1]
        checksum = line3[2]

        line4 = struct.unpack('>4s', ip_header[12:16])
        src_addr =socket.inet_ntoa(line4[0])

        line5 = struct.unpack('>4s', ip_header[16:20])
        des_addr = socket.inet_ntoa(line5[0])

        return {
            'ip_version ': ip_version,
            'ip_length ': ip_length,
            'packet_length ': packet_length,
            'TTL ': TTL,
            'protocol ' : protocol,
            'checksum ' : checksum,
            'src_addr ' : src_addr,
            'des_addr ' : des_addr
        }

    @classmethod
    def parse(cls, packet):
        ip_header = packet[:20]
        return cls.parse_ip_header(ip_header)
