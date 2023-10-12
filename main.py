import math

N = 74701165267919
e = 3145553
C = '''
32035658541536
35242897170964
6268303368709
6877322610982
16329207109754
35007623593376
26715311593240
36220800128563
25019660581036
61639733671958
21186453949445
72477207535811
'''

# выбираем стартовое значение A
if math.sqrt(N) % 1 != 0:
    a = int(math.sqrt(N) // 1 + 1)
else:
    a = int(math.sqrt(N) // 1)

# итерируемся по возможным значениям в поисках целого корня B
i = 0
while True:
    t = a + i
    print("t" + str(i) + "=" + str(t))
    b = t ** 2 - N
    print("b" + str(i) + "=" + str(b))
    b_sqrt = math.sqrt(b)
    print("b_sqrt" + str(i) + "=" + str(b_sqrt))
    i += 1
    if b_sqrt % 1 == 0:
        break
    if i == 100:
        raise Exception("Не найден целый корень")

# получили p и q на основе A и B
p = t + b_sqrt
q = t - b_sqrt
phi = int((p - 1) * (q - 1))
d = pow(e, -1, phi)

print("p=" + str(p))
print("q=" + str(q))
print("phi(N)=" + str(phi))
print("d=" + str(d))

# дешефруем rsa полученной секретной комбинацией
res = ""
for b in C.split():
    m = pow(int(b), d, N)
    sub_str_bytes = m.to_bytes(4, byteorder='big')
    sub_str = sub_str_bytes.decode('cp1251')
    res += sub_str
print(f"res = {res}")
