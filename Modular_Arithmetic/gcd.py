def gcd(a,b):
    while True:
        kalan = a % b

        if kalan == 0:
            return b
        
        a = b
        b = kalan
    

def egcd(a, b):

    x, x1 = 1, 0
    y, y1 = 0, 1

    while True:
        kalan = a % b

        bolum = a//b
        x, x1 = x1, x - bolum * x1
        y, y1 = y1, y - bolum * y1

        if kalan == 0:
            
            return f"{x} {y}"
        
        a = b
        b = kalan



a, b = 8146798528947, 17
print("GCD: ", gcd(a,b))

print("EGCD: ", egcd(a,b))



    





