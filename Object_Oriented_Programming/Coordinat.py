class Dot:
    def __init__(self):
        x = 0
        y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def isRight(self, dot1, dot2):
        if dot1.x > dot2.x:
            return True
        return False
    
    def length(self, dot1, dot2):
        x = dot1.x - dot2.x
        y = dot1.y - dot2.y
        length = (x**2 + y**2)**(0.5)

        return length

d1 = Dot(1, 2)
d2 = Dot(5, 5)

print(d1.isRight(d1, d2))
print(d2.isRight(d2, d1))
print(d1.length(d1, d2))
print(d2.length(d2, d1))