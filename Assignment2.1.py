'''
program which accepts a sequence of comma-separated numbers from console
and generate a list.
'''

numberSequence = input("Enter comma separated numbers : ")

numberArray = numberSequence.split(',')

numberList = []

try:
    for number in numberArray:
        numberList.append(int(number))
    print(numberList)
except Exception:
    print("Please enter valid numbers each separated by comma")