"""

def notX_2(X, U):
    nX = set(U)
    for elem in X:
        if elem in nX:
            nX.remove(elem)
    return nX

"""

def notX(A, U):
    """Другим аргументом передавати уныверсальну множину"""
    U = list(U)
    A = list(A)
    C = []
    for i in U:
        q = 0
        for j in A:
            if i == j:
                q = 1
        if q == 0:
            C.append(i)
    return set(C)


def intersec(X,Y):
    x = list(X)
    y = list(Y)
    result = []
    for elemx in x:
        for elemy in y:
            if elemx == elemy:
                result.append(elemx)
    return set(result)


def unionn(X,Y):
    x = list(X)
    y = list(Y)
    result = y
    for elemx in x:
        q = False
        for elemy in y:
            if elemx == elemy:
                q = True
        if not q:
            result.append(elemx)
    return set(result)


"""
def intersec_2(X,Y):
    result = {}
    for elem in X:
        if elem in Y:
            result.update(elem)
    return result

"""

"""
def unionn(X,Y):
    result = {}
    for elem in X:
        if elem in Y:
            result.update(elem)
    return result

"""


def origin_exp(A, B, C, U):
    result = set((A & (U - B)) | ((U - A) & B)) & ((U - C) & ((U - C) | B))
    print(result)
    action1 = unionn(intersec(A, notX(B, U)), intersec(notX(A, U), B))
    action2 = intersec(notX(C, U), unionn(notX(C, U), B))
    result = set(intersec(action1, action2))
    return result


def difer(x, y):
    return x-y

def vyraz_2(F, D, U):
    x = set(notX(F, U) - D)
    return x

A ={1,3,2,4,5}
B = {1,3,6,7,8,9,10}
C={1,2,3,4,5,6,7,8,11,22}
U=set(range(20))
#print(notX([2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8, 66], [5, 3, 2, 1, 3, 2, 33, 22, 11]))

#print(unionn([2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8, 66], [5, 3, 2, 1, 3, 2, 33, 22, 11]))
print(origin_exp({1,3,2,4,5}, {1,3,6,7,8,9,10},{1,2,3,4,5,6,7,8,11,22},set(range(20))))
