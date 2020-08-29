from image_embedder import ascii_to_bits

def test_converting_alpha():
    assert ascii_to_bits("hello") == "11010001100101110110011011001101111"
