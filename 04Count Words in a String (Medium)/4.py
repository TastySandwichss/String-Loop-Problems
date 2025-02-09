x = input()
is_space = True
count = 0
for i in range(len(x)):
    if (x[i] == " "):
        is_space = True
    elif (is_space == True):
        count += 1
        is_space = False
       
print(count)