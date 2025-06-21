n = int(input())
a = list(map(int, input().split()))
moves = 0

for i in range(n - 1):
    if a[i] < a[i + 1]: # checking if new element is greater than or equal to the previous element
        continue 
    else: # array is smth like [10,4]
        diff = a[i] - a[i + 1] # diff = 10 - 4 so 6
        a[i + 1] += diff # [10,10] we make it match
        moves += diff

print(moves)
