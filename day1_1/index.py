import os
import math

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

def get_calibration(text):
    digits = list(text)
   
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
    return first*10 +last

text =  open_file(os.path.join(os.path.dirname(__file__), 'input.txt'))

arrFromText = text.split('\n')


sum =0
for i in range(len(arrFromText)):
    text = arrFromText[i]
    # print(text)
    sum += get_calibration(text)
print(sum)



    