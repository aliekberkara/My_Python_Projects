def gcd(a,b):

    kalan = a % b
    if kalan == 0:
        return b
    else:
        return gcd(b,kalan)

a, b = 66528, 52920
print("Greatest Common Divider: ", gcd(a,b))

