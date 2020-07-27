x, y = list(input().split())
min = 50
for i in range(len(y) - len(x)+1):
    count = 0
    for j in range(len(x)):
        if x[j] != y[i+j]:
            count += 1
    if count < min:
        min = count
print(min)
