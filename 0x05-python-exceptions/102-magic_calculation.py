#!/usr/bin/python3
def magic_calculation(a, b):
    resultat = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            resultat += a ** b / i
        except Exception:
            resultat = b + a
            break
    return resultat
