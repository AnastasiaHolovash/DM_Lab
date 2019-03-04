import original_expression as oexp


def difference(A, B):
    A = list(A)
    B = list(B)
    C = []
    for i in A:
        q = 0
        for j in B:
            if i == j:
                q = 1
        if q == 0:
            C.append(i)
    return C


def second_exp(a, b, universalset):
    result = difference(oexp.notX(b, universalset), oexp.notX(a, universalset))
    return result