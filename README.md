# steganography
Hiding information in things. Commonly used for digital watermarking as to determine the origin of a file.

## Images - least significant bits
There are 127 ASCII-characters, so it takes 7 bits (2^7=128) to specify one ASCII character. If the least significant bit for each color (assuming 24 bit RGB, 8 bits for each color) is used, each pixel can encode 3 bits. Then 3 pixels can encode a single ASCII-character.
