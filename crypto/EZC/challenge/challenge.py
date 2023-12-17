from Crypto.Util.number import bytes_to_long,getRandomInteger

def is_valid_curve_parameters(p, a, b):
    # Check if 4*a^3 + 27*b^2 is not equal to 0 (required for the elliptic curve equation)
    return (4 * pow(a, 3, p) + 27 * pow(b, 2, p)) % p != 0

def lift(x,a,b,p):
    #y**2=x**3+a*x+b

    y_square = (x**3+a*x+b)%p
    y = pow(y_square, (p + 1) // 4, p)
    if (y * y) % p != y_square:
        # If not, use the negation of y
        y = p - y
    if ((y * y) % p == y_square):
        return y
    else:
        raise ValueError


FLAG = b'shellmates{REDACTED}'

#Curve parameters
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
a = bytes_to_long(FLAG[:len(FLAG)//2])
b = bytes_to_long(FLAG[len(FLAG)//2:])

assert is_valid_curve_parameters(p,a,b)


for i in range(2):
    while True:
        try:
            x=getRandomInteger(p.bit_length())
            y=lift(x,a,b,p)
            break
        except:
            continue
    print(f'Point{(x,y)}')




            
    




