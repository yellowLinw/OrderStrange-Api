#!/usr/bin/python3
# -*- coding: utf-8 -*-

def ip2int(ip):
    ip_list = ip.strip().split('.')
    SUM = 0
    for i in range(len(ip_list)):
        SUM += int(ip_list[i]) * 256 ** (3 - i)
    return SUM


def int2ip(num):
    ip_list = []
    for n in range(4):
        num, mod = divmod(num, 256)
        ip_list.insert(0, str(mod))
    return '.'.join(ip_list)
