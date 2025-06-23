# correct approach but TLE error occurs on test#13
''' n = int(input())
nums = map(int, input().split())
 
print(len(set(nums)))'''

#here's a solution that did pass all test cases
from collections import Counter;input();print(len(Counter((input().split(' ')))))
