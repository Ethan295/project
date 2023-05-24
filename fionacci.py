
maxNum = 1000

num1 = 0
num2 = 1
ris = 0

while ris <= maxNum:
    print(ris)
    ris = num1 + num2
    num1 = num2
    num2 = ris
