import os
import math

numbers = [ '1', '2', '3', '4', '5', '6', '7', '8', '9']
numbersText = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbersTextDict = { 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six':'6', 'seven': '7', 'eight': '8', 'nine': '9'}
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

def textWithNumbers(text):
    i = 0
    j = 0
    while True:
        for n in range (6):
            assumedNumber = text[i:j]
            # print(assumedNumber, text)
            if assumedNumber in numbersText:
                text = text.replace(assumedNumber, numbersTextDict[assumedNumber], 1)
                i=0
                j=0 
                continue  
            j += 1
        i += 1
        j = i
        if i > len(text):
            break
    return text

def get_calibration(text):
    textNumbered = textWithNumbers(text)
    textNumbered = textWithNumbers(text)
    textNumbered = textWithNumbers(text)
    digits = list(textNumbered)
    first = -1
    last = 0
    for i in range(len(digits)):
        digit = digits[i]
       
        if digit in numbers:
            if first == -1:
                first = int(digit)
                last = first
            else: 
                last = int(digit)
    if first == -1:
        return 0
    
    print( first,last)
    return first*10 +last

text =  open_file(os.path.join(os.path.dirname(__file__), 'input.txt'))

arrFromText = text.split('\n')

testArr = [
    'two1nine',
'eightwothree',
'abcone2threexyz',
'xtwone3four',
'4nineeightseven2',
'zoneight234',
'7pqrstsixteen'
]
sum =0
for i in range(len(arrFromText)):
    text = arrFromText[i]
    # print(text)
    sum += get_calibration(text)
print(sum)



    