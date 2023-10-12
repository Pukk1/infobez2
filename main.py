import math


def ferma(N, e, C):
    message = ""

    # выбираем S
    s = int(math.sqrt(N) // 1)

    # ищем целый корень T
    i = 0
    while True:
        i += 1
        t = s + i
        print("t(" + str(i) + ")=" + str(t))
        w = t ** 2 - N
        print("w(" + str(i) + ")=" + str(w))
        w_sqrt = math.sqrt(w)
        print("w_sqrt(" + str(i) + ")=" + str(w_sqrt))
        if math.sqrt(w) % 1 == 0:
            break

    p = t + w_sqrt
    print("p=" + str(p))
    q = t - w_sqrt
    print("q=" + str(q))
    phi_N = int((p - 1) * (q - 1))
    print("phi(N)=" + str(phi_N))
    d = pow(e, -1, phi_N)
    print("d=" + str(d))

    # дешефруем rsa полученной секретной комбинацией
    for w in C.split():
        m = pow(int(w), d, N)
        sub_str = m.to_bytes(4, byteorder='big').decode('cp1251')
        message += sub_str
    print(f"message = {message}")


N = 81177745546021
e = 2711039
C = '''
61553353723258
11339642237403
55951185642146
38561524032018
34517298669793
33641624424571
78428225355946
50176820404544
68017840453091
5507834749606
26675763943141
47457759065088
'''

ferma(N, e, C)
