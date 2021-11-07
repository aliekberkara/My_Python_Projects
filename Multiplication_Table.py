"""
Problem 3
Try to print a multiplication table with numbers from 1 to 10.
"""
for i in range(1, 11):
    print('*' * 20)
    for j in range(1, 11):
        print(f"{i}*{j}={i*j}")
