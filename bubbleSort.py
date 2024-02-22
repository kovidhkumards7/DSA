a = [1,5,6,7,8,9,11,12,16,18,19,25,23,45,485,7,4158,75,415,7,4152,45,4,54,527857,4,5,45,45]
a = list(set(a))

for i in range(0,len(a) - 1):
    for j in range(0,len(a) - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
        
print(a)