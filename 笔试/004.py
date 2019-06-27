from collections import deque

import math


def main():
    result = {}
    with open('input4.txt', 'r') as f:
        while 1:
            line = f.readline()
            if line:
                deviceid, mac, _ = line.split(' ')
                if deviceid not in result:
                    result[deviceid] = {}
                    result[deviceid]['count'] = 0
                if mac not in result[deviceid]:
                    result[deviceid][mac] = 1
                else:
                    result[deviceid][mac] += 1
                result[deviceid]['count'] += 1
            else:
                break
    for dev in result:
        count = result[dev]['count']
        res = 0
        for m in result[dev]:
            num = result[dev][m]
            prob = round(num / count, 2)
            res += -prob * math.log2(prob)
        print(dev,':', round(res,2))
main()
