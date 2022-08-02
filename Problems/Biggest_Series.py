# Write a program that outputs the largest number of consecutive quotation marks number in a text.

def counterLetters(text):
    data = 0
    enb = 0
    i = 0 
    for t in text:
        if(t == '"'):
            data += 1
        else:
            if data >= enb:
                enb = data
            data = 0
        
        if i == (len(text) - 1):
            if data >= enb:
                enb = data
        i += 1
    
    return enb


text = 'H"e"l"""l""o"""""'
print("--------------------------------------------------\n" + text)
print(f'Number of consecutive quotation marks: {counterLetters(text)}')