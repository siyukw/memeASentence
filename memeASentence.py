import random

def meme():
    input = raw_input("What's the sentence you would like to meme? ")
    output = ""
    for char in input:
        temp = ""
        if random.random() < 0.5:
            temp = char.upper()
        else:
            temp = char.lower()
        output = output + temp
    print output
    
meme()