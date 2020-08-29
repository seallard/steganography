from image_embedder import ascii_to_bits


def test_convert_single_char():
    assert ascii_to_bits("a") == "1100001"

def test_convert_single_numeric():
    assert ascii_to_bits("1") == "0110001"

def test_convert_word():
    assert ascii_to_bits("hello") == "11010001100101110110011011001101111"

def test_convert_numeric():
    assert ascii_to_bits("100") == "011000101100000110000"

def test_convert_alphanumeric():
    assert ascii_to_bits("hello1") == "110100011001011101100110110011011110110001"

