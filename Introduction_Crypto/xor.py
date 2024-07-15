from Cryptodome.Util.number import *
from pwn import *

def int_to_text():
        
    ords = hex(11515195063862318899931685488813747395775516287289682636499965282714637259206269)
    ordi = list()
    for i in range(2, len(ords), 2):
        ordi.append('0x'+ords[i:i+2])

    for i in range(len(ordi)):
        ordi[i]=int(ordi[i], 16)

    print('Here is your flag:')
    print("".join(chr(c) for c in ordi))

def text_to_xor():
    word ='label'

    word_bytes = []

    key = 13
    
    for i in range(len(word)):
        word_bytes.append(ord(word[i]))

    xored = [b^key for b in word_bytes]
    word_bytes = xored
    

    print('Here is your flag:')
    print("".join(chr(c) for c in word_bytes))

def hex_to_bytes(hex_str):
    hex_bytes = list()
    for i in range(0, len(hex_str), 2):
        hex_bytes.append('0x' + hex_str[i:i+2])

    for i in range(len(hex_bytes)):
        hex_bytes[i]=int(hex_bytes[i], 16)

    return(hex_bytes)

def hex_to_xor():
    result0 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
    result1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
    result2 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
    result3 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

    key1 = hex_to_bytes(result0)

    result1_bytes = hex_to_bytes(result1)

    key2 = [key1[i]^result1_bytes[i] for i in range(len(key1))]
    
    result2_bytes = hex_to_bytes(result2)

    key3 = [key2[i]^result2_bytes[i] for i in range(len(key2))]

    result3_bytes = hex_to_bytes(result3)

    FLAG = [key1[i]^key2[i]^key3[i]^result3_bytes[i] for i in range(len(key3))]

    print('Here is your flag:')
    print("".join(chr(c) for c in FLAG))


def byte_xor():
    xored = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

    xored_bytes = hex_to_bytes(xored)


    for i in range(1,256):
        FLAG = [xored_bytes[j] ^ i for j in range(len(xored_bytes))]
        if 'crypto' in "".join(chr(c) for c in FLAG):
            print('Here is your flag:')
            print("".join(chr(c) for c in FLAG))

def no_key_xor():
    xored = "18161A05130E1A27171D14061953425157481211071B4C0307451104111158585619030006081C0008150C560313075D50185604140649100306131F174119154442511548031D4E520E00194956051B1A52584A501A4104000101001C091F061B545E504C501A0D1545520400060C040D13581659594D01131808520E041C0C560015185748514915"
    xored_bytes = hex_to_bytes(xored)
    
    key = "pwnlab{Urkutmesin"
    key_bytes = list()
    for i in range(len(key)):
        key_bytes.append(ord(key[i]))

    key_bytes = key_bytes*16
    key_bytes.append(104)
    key_bytes.append(97)
    
    

    FLAG = [xored_bytes[i] ^ key_bytes[i] for i in range(len(xored_bytes))]


    print('Here is your key:')
    print("".join(chr(c) for c in FLAG))

no_key_xor()