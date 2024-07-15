a = 288260533169915
p = 1007621497415251

def decrypt_flag(ciphertext):
    plaintext = ''

    for n in ciphertext:
        if pow(n, (p-1)//2, p) == 1:
            plaintext += "1"
        else:
            plaintext += "0"

    plaintext1= ""

    for i in range(1, len(plaintext), 8):
        plaintext1 += chr(int(plaintext[i:i+7], 2))

    return plaintext1


file = open("output.txt", "r")
encrypted_flag = eval(file.read())


print(decrypt_flag(encrypted_flag))