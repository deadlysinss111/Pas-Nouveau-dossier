def concatWithComma(str1=str, str2=str):
    return (str1+", "+str2)


def fibonacci(init):
    l=[0,init]
    listSTR=''
    for i in range(10):
        l.append(l[i]+l[i+1])
    for i in range(0,10, 2):
        listSTR=(listSTR + concatWithComma(str(i),str(i+1) +', '))
    listSTR=(listSTR + '...')
    return listSTR

print(fibonacci(1))




def conway():
    