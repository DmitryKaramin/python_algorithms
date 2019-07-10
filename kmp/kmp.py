s = 'abcabd'


def pi_funk(a):
    l = len(a)
    Pi = []
    Pi = Pi + [0] * l
    j = 0
    i = 1

    for _ in range(l - 1):
        if a[i] == a[j]:
            Pi[i] = j + 1
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = Pi[j - 1]

    return Pi


s2 = 'abcabeabcabcabf'


def kmp(t):
    a = 'abcabd'
    pi = pi_funk(s)

    k = 0
    l = 0

    while k != len(t):

        if a[l] == t[k]:
            k += 1
            l += 1
            if l == len(a):
                return True
        elif l == 0:
            k += 1
            if k == len(t):
                return False
        else:
            l = pi[l - 1]

    return False

print(kmp(s2))