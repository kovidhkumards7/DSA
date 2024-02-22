a = [1,5,6,7,8,9,11,12,16,18,19,25,23,45,485,7,4158,75,415,7,4152,45,4,54,527857,4,5,45,45]
listOfNumbers = list(set(a))
listOfNumbers.sort()



search = int(input("Enter search element: "))

def binarySearch(listOfNumbers, search):
    low = 0
    high = len(listOfNumbers) - 1
    eleFound = False

    while low <= high and not eleFound:
        mid = (low + high) // 2
        if search == listOfNumbers[mid]:
            eleFound = True
            print(mid)
        elif search > listOfNumbers[mid]:
            low = mid + 1
        else:
            high = mid - 1

    if eleFound:
        print("ele found")
    else:
        print("ele not found")

binarySearch(listOfNumbers, search)

