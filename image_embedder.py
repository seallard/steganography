from matplotlib.image import imread

def integer_to_binary(integer):
    return f'{integer:07b}'

def ascii_to_bits(text):
    binary = bin(int.from_bytes(text.encode(), 'big'))
    return binary

def bits_to_ascii(bitstring):
    pass

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
