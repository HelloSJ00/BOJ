import sys
input = sys.stdin.readline

inputMath = list(input())
num = []
tmpNum =''
for i in range(len(inputMath)):
    if (inputMath[i] == '-') or (inputMath[i] == '+'):
        num.append(int(tmpNum))
        tmpNum = ''
        num.append(inputMath[i])
    else:
        tmpNum += inputMath[i]

    if i == (len(inputMath)-1):
        num.append(int(tmpNum))
# print(num)
ok =  True
anwser = 0
for i in num:
    if (i == '-'):
        ok = False
    elif (i=='+'):
        continue
    else:
        if ok:
            anwser += i

        else:
            anwser -= i
print(anwser)