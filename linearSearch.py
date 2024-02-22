a = [1,5,6,7,8,9,11,12,16,18,19,25,23,45,485,7,4158,75,415,7,4152,45,4,54,527857,4,5,45,45]
listOfNumbers = list(set(a))

search = int(input("Enter the search element: "))

for i in range(0, len(listOfNumbers) - 1):
    if search == listOfNumbers[i]:
        print("ele found")
        break
