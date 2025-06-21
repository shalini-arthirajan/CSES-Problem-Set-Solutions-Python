n, x = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
 
i = 0
j = n - 1
gondolas = 0
 
while i <= j:
    if p[i] + p[j] <= x:
        i += 1  # paired with lightest
    j -= 1      # heaviest always goes alone
    gondolas += 1  # one gondola used
print(gondolas)
