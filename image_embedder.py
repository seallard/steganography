from matplotlib.image import imread, imsave
from itertools import zip_longest

import glob
import tqdm

int2bin = {i:f'{i:07b}' for i in range(0,256)}

def integer_to_binary(integer):
    return int2bin[integer]

def binary_to_integer(bit_string):
    return int(bit_string, 2)

def integer_to_ascii(integer):
    return chr(integer)

def ascii_to_integer(ascii):
    return ord(ascii)

def ascii_to_bits(text):
    bit_string = ""
    progress = tqdm.tqdm(total=len(text),
                        desc="a2b")
    for char in text:
        progress.update(1)
        ascii_integer = ascii_to_integer(char)
        if ascii_integer >= 255:
            ascii_integer = 255
        bit_string += integer_to_binary(ascii_integer)
    progress.close()
    return bit_string

def bits_to_ascii(bit_string):
    ascii_string = ""
    progress = tqdm.tqdm(total=len(bit_string)/7,
                         desc="b2a")
    for i in range(0, len(bit_string), 7):
        progress.update(1)
        ascii_binary = bit_string[i:i+7]
        ascii_integer = binary_to_integer(ascii_binary)
        if ascii_integer >= 255:
            ascii_integer = 255
        ascii_string += integer_to_ascii(ascii_integer)
    progress.close()
    return ascii_string

def embed_string():
    pass

def extract_string(filename):
    img = imread(filename)
    bit_string = ''
    idx = 0
    for i, row in enumerate(img):
        for j, pixel in enumerate(row):
            pixel *= 255
            pixel = [int(x) for x in pixel[:3]]  # Ignore alph
            for c, color in enumerate(pixel):
                binary_color = integer_to_binary(color)
                least_significant_color_bit = binary_color[-1]
                bit_string += least_significant_color_bit
                idx += 1
    return bits_to_ascii(bit_string)

def main():
    files = glob.glob("content/*.txt")
    content = ''
    for f in files:
        with open(f, 'r', encoding='utf-8') as fp:
            content += fp.read()

    print(f"Loaded {len(content)*8} bits")  # 1 byte = 8 bit
    filename = "images/sample.jpg"
    img = imread(filename).copy()
    max_bits = 1
    for x in img.shape:
        max_bits *= x
    print(f"Can load {max_bits} in image")
    
    bit_string = ascii_to_bits(content)
    print("ascii2bits done")
    bit_string_index = 0

    progress = tqdm.tqdm(total=img.shape[0])

    for i, row in enumerate(img):
        progress.update(1)
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

                if bit_string_index >= len(bit_string) - 1:
                    imsave("test.png", img)
                    extracted_string = extract_string("test.png")
                    print(extracted_string)
                    return
    progress.close()

main()