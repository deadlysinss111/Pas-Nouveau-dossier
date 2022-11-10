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




def conway(x):
    plateau=[]
    row=[]
    for i in range(x):
        for j in range(x):
            row.append(f"{i}/{j}")
        plateau.append(row)
    return plateau

print(conway(10))

def callConway(plateau, x, y):
    return [plateau[x,y]]

def callCross(plateau,x,y):
    cross=''
    if y>0:
        cross = cross +callConway(plateau, x, y-1)
    else:
        cross = cross +"min y"
    cross = cross +"\n"
    if x>0:
        cross = cross +callConway(plateau, x-1, y)
    else:
        cross = cross +"min x"
    cross = cross +" // "
    cross = cross +callConway(plateau, x, y)
    cross = cross +" // "
    if x<len(plateau-1):
        cross = cross +callConway(plateau, x+1, y)
    else:
        cross = cross +"max x"
    cross = cross +"\n"
    if y<len(plateau-1):
        cross = cross +callConway(plateau, x, y+1)
    else:
        cross = cross +"max y"

print(callConway(conway(10), 5, 5))