from matplotlib.image import imread, imsave
from itertools import zip_longest

def integer_to_binary(integer):
    return f'{integer:07b}'

def binary_to_integer(bit_string):
    return int(bit_string, 2)

def integer_to_ascii(integer):
    return chr(integer)

def ascii_to_bits(text):
    bit_string = ""
    for char in text:
        ascii_integer = ord(char)
        bit_string += integer_to_binary(ascii_integer)
    return bit_string

def bits_to_ascii(bit_string):
    ascii_string = ""
    for i in range(0, len(bit_string), 7):
        ascii_binary = bit_string[i:i+7]
        ascii_integer = binary_to_integer(ascii_binary)
        ascii_string += integer_to_ascii(ascii_integer)
    return ascii_string

def embed_string():
    pass

def extract_string():
    pass


def main():
    filename = "images/sample.jpg"
    img = imread(filename).copy()
    print(img.size)
    bit_string = ascii_to_bits("Hello, World!")
    bit_string_index = 0

    for i, row in enumerate(img):
        for j, pixel in enumerate(row):
            for c, color in enumerate(pixel):

                current_bit = bit_string[bit_string_index]

                binary_color = integer_to_binary(color)
                least_significant_color_bit = binary_color[-1]

                if least_significant_color_bit != current_bit:
                    updated_binary_color = binary_color[:-1] + current_bit
                    updated_integer_color = binary_to_integer(updated_binary_color)
                    img[i][j][c] = updated_integer_color

                bit_string_index += 1

                if bit_string_index == len(bit_string):
                    imsave("test.jpg", img)
                    return


main()