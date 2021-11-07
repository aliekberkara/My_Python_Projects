"""
Problem 5

Print only the numbers divisible by 3 from the numbers 1 to 100.
Try to do this with "continue".
"""
for i in range(1, 101):
    if i % 3 == 0:
        print(i)
    else:
        continue
