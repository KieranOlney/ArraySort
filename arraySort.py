import random

def main():
    testArrayOne = generateArray(100)
    testArrayTwo = generateArray(20)
    testArrayThree = []
    testArrayFour = None
    print(testArrayOne)
    print(sortArray(testArrayOne),"\n\n")
    print(testArrayTwo)
    print(sortArray(testArrayTwo),"\n\n")
    print(sortArray(testArrayThree),"\n\n")
    print(sortArray(testArrayFour),"\n\n")

def sortArray(arrayToSort):
    newArray = []
    if arrayToSort == None:
        print("Array Does Not Exist To Sort")
        return newArray
    elif len(arrayToSort) == 0:
        print("Array Is Empty")
        return newArray
    else:
        while arrayToSort != []:
            arrayMinimum = arrayToSort[0]
            for i in arrayToSort:
                if i < arrayMinimum:
                    arrayMinimum = i

            newArray.append(arrayMinimum)
            arrayToSort.remove(arrayMinimum)
        print("Array Sorted")
        return newArray

def generateArray(length):
    newArray = []
    for i in range(length):
        newArray.append(random.randint(0,10000))
    return newArray

main()