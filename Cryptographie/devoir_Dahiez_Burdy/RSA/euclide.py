def euclide_etendu_iteratif(a, b):
    
    u, uu = 1, 0
    v, vv = 0, 1
    while b != 0:
        q = a//b
        a, b = b, a % b
        uu, u = u - q * uu, uu
        vv, v = v - q * vv, vv
    return u, v, a


def estPremier(p):
    
    for n in range(2, p):
        if p % n == 0:
            return False
    return True


def cle(p, q, e):
   

    if estPremier(p) == False or estPremier(q) == False:
        return None

    N = p * q
    phi_N = (p - 1) * (q - 1)
    pgcd = euclide_etendu_iteratif(e, phi_N)
    u = pgcd[0]
    d = u
    return (e, N), (d, N)


def chiffrer(m, cle):
    

    return pow(m, cle[0], cle[1])


if __name__ == '__main__':
    p = 13
    q = 19
    e = 31

    cle_privee, cle_publique = cle(p, q, e)
    m = 11
    x = chiffrer(m, cle_privee)
    y = chiffrer(x, cle_publique)

    print(cle_publique)
    print("\n resultat : ", m, x, y)
