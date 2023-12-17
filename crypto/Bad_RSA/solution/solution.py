from Crypto.Util.number import long_to_bytes
def legendre(a, p):
    return pow(a, (p - 1) // 2, p)

# return the modular square root if exists
def tonelli(n, p):
    assert legendre(n, p) == 1, "not a square (mod p)"
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r

c = 81002699966894317931757015243327616625750249607142918536476915875284203036909952333334403884924748994941305079738497910819256705553219008583548814577164930548439754825882485834069765863255213357781175046858603314586983556689220366153083705140197813081634066189623901121082327329536928093761976301762823791137
e = 32
n = 127862596228081351365127219817765804640164615099827951964966025012558776028853139180299561304186369793393691203630103832497224903203431930274192466285256640227984085122560879705919753931851019261802596332571068344006946114899092891132410293749320803541627919206026357709494975191861978338093071706834822630301


for i in range(32):
    b = list(bin(i)[2:])
    k = c
    for j in range(len(b)):
        if b[j] == "0":
            b[j] = "-1"
        # since not all the numbers are quadraric residus some cases may raise an exception
        try:
            k = (int(b[j])*tonelli(k,n))%n
        except:
            pass
    possible_flag = long_to_bytes(k)
    if b"shellmates" in possible_flag:
        print(possible_flag)
        break
