

def chunk(source, length=512):
    for i in range(0, len(source), length):
        yield source[i:i + length]


def shift(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff


def sha(data):
    """
    SHA-1 hash function\n
    Returns the SHA1 as a 40-character hex string\n
    Example: python .\main.py "<data>"
    """
    hashes = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]
    origin = ""
    encoded = ""
    for n in data:
        origin += f"{ord(n):08b}"
    byte = origin + "1"
    padding = (448 - len(byte) % 512 + 512) % 512
    byte += padding * "0"
    byte += f'{len(origin):064b}'
    for cnk in chunk(byte):
        w = [0] * 80
        for i, word in enumerate(chunk(cnk, 32)):
            w[i] = int(word, 2)
        for i in range(16, 80):
            w[i] = shift((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1)
        a, b, c, d, e = hashes
        f, k = -1, -1
        for i in range(0, 80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6
            temp = shift(a, 5) + f + e + k + w[i] & 0xffffffff
            e, d, c, b, a = d, c, shift(b, 30), a, temp
        hashes[0] = (hashes[0] + a) & 0xffffffff
        hashes[1] = (hashes[1] + b) & 0xffffffff
        hashes[2] = (hashes[2] + c) & 0xffffffff
        hashes[3] = (hashes[3] + d) & 0xffffffff
        hashes[4] = (hashes[4] + e) & 0xffffffff
    for hash in hashes:
        encoded += f"{hash:08x}"
    return encoded
