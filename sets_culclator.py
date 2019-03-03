def notX(X, U):
    nX = set(U)
    for elem in X:
        if elem in nX:
            nX.remove(elem)
    return nX


def notX_2(X, U):
    R = []
    for j in X:
        b = False
        for i in U:
            if i == j:
                b = True
        if not b:
            R.append(j)
    return set(R)


def intersec(X,Y):
    result = {}
    for elem in X:
        if elem in Y:
            result.update(elem)
    return result


def unionn(X,Y):
    result = {}
    for elem in X:
        if elem in Y:
            result.update(elem)
    return result


def vyraz(A, B, C, U):
    x = set((A & (U - B)) | ((U - A) & B)) & ((U - C) & ((U - C) | B))
    return x


def vyraz_2(F, D, U):
    x = set(notX(F, U) - D)
    return x


#print(notX_2([2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8, 66], [5, 3, 2, 1, 3, 2, 33, 22, 11]))
