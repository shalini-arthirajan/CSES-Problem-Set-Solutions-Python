n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
 
for i in range(1, n):
    if i != numbers[i - 1]:
        print(i)
        break
else:
    print(n)
