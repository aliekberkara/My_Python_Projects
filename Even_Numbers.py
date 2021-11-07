"""
Problem 6
List comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmaya çalışın.
"""

liste = [x for x in range(1, 101) if x % 2 == 0]
print(liste)
