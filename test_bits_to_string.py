from image_embedder import bits_to_ascii

def test_convert_empty():
    assert bits_to_ascii("") == ""

def test_convert_single_char():
    assert bits_to_ascii("1100001") == "a"

def test_convert_single_numeric():
    assert bits_to_ascii("0110001") == "1"

def test_convert_word():
    assert bits_to_ascii("11010001100101110110011011001101111") == "hello"

def test_convert_numeric():
    assert bits_to_ascii("011000101100000110000") == "100"

def test_convert_alphanumeric():
    assert bits_to_ascii("110100011001011101100110110011011110110001") == "hello1" 
