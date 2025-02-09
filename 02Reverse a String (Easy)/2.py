x = input()
y = []
for i in range(len(x)-1,-1,-1):
    y.append(x[i])
print("".join(y))