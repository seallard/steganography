from matplotlib.image import imread
from itertools import zip_longest

def integer_to_binary(integer):
    return f'{integer:07b}'

def binary_to_integer(bit_string):
    print(type(bit_string))
    print(bit_string)
    return int(bit_string, 2)

def integer_to_ascii(integer):
    return chr(integer)

def ascii_to_bits(text):
    bitstring = ""
    for char in text:
        ascii_integer = ord(char)
        bitstring += integer_to_binary(ascii_integer)
    return bitstring

def bits_to_ascii(bit_string):
    ascii_string = ""
    for i in range(0, len(bit_string), 7):
        ascii_binary = bit_string[i:i+7]
        ascii_integer = binary_to_integer(ascii_binary)
        ascii_string += integer_to_ascii(ascii_integer)
    return ascii_string
    
def img_to_bitmap(img):
    pass

def embed_string():
    pass

def extract_string():
    pass

def int_to_binary(integer):
    pass


def main():
    filename = "sample.jpg"

    img = imread(filename)

    bit_string_index = 0

    for i, row in enumerate(img):
        for j, column in enumerate(row):
            break
