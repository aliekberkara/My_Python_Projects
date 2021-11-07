"""
Problem 3
1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.
"""
for i in range(1, 11):
    print('*' * 20)
    for j in range(1, 11):
        print(f"{i}*{j}={i*j}")
