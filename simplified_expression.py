import original_expression as oexp

def sym_dif(a, b):
    a = list(a)
    b = list(b)
    c = []
    for i in range(len(a)):
        if (a[i] not in b):
            c.append(a[i])
    for j in range(len(b)):
        if (b[j] not in a):
            c.append(b[j])
    return (c)

# Обчислює спрощений вираз (1)


def simplified_exp(A, B, C, U):
    """U - універсальна множина"""
    result = set(oexp.intersec(sym_dif(A, B), oexp.notX(C, U)))
    return result