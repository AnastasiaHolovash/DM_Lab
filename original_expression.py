"""
def notX(X, U):
    nX = set(U)
    for elem in X:
        if elem in nX:
            nX.remove(elem)
    return nX
"""


def notX(X, U):
    x = list(X)
    u = list(U)
    R = []
    #k = 0
    for j in range(len(x)):
        b = False
        for i in range(len(u)):
            if x[j] == u[i]:
                b = True
        if not b:
            R.append(x[j])
            #k +=1
    return set(R)


def intersec(X,Y):
    x = list(X)
    y = list(Y)
    result = {}
    for elemx in range(len(x)):
        for elemy in range(len(y)):
            if x[elemx] == y[elemy]:
                result.update(x[elemx])
    return result


def unionn(X,Y):
    result = {}
    for elem in X:
        if elem in Y:
            result.update(elem)
    return result


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


def difer(x, y):
    return x-y


def vyraz(A, B, C, U):
    x = set((A & (U - B)) | ((U - A) & B)) & ((U - C) & ((U - C) | B))
    return x


def vyraz_2(F, D, U):
    x = set(notX(F, U) - D)
    return x


print(notX_2([2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8, 66], [5, 3, 2, 1, 3, 2, 33, 22, 11]))
