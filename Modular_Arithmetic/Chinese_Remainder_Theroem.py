n = [5, 11, 17]
a = [2, 3, 5]

def chinese_remainder_theroem(n, a):
    
    n.sort()
    max = n[-1]
    a3 = a[-1]

    for i in range(len(n)-2, -1, -1):
        for j in range(n[i]):
            if (max * j + a3) % n[i] == a[i]:
                a3 = max*j + a3
                max = n[i]*max
                break

    return f"x = {a3} mod {max}"

print(chinese_remainder_theroem(n,a))
