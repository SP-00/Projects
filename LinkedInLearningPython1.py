def hexMath(hex):
    hexNumbers = { '0' :0 , '1' :1, '2' :2 , '3' :3, '4' :4 , '5' :5, '6': 6 , '7' :7, '8' :8 , '9' :9,'A' :10 , 'B' :11, 'C' :12 , 'D' :13, 'E' :14 , 'F' :15  
    }
    hexList = []
    hexMathList = []
    value = 0
    for i in hex:
        hexList.append(hexNumbers[i])
    for j in range(0,len(hex)):
        num = 16**j
        hexMathList.insert(0,16**j)
    for t in range(len(hex)):
        value = value + hexList[t]*hexMathList[t]
    print(value)

hexMath('AAAA')
