import random

class RSA:
    @staticmethod
    def encrypt(public_key, n, msg):
        cipher = ""
        m = None
        for char in msg:
            m = ord(char)
            cipher += str(pow(m, public_key, n)) + " "
        return cipher

    @staticmethod
    def decrypt(private_key, n, cipher):
        msg = ""
        parts = cipher.split()
        for part in parts:
            if part:
                char = int(part)
                msg += chr(pow(char, private_key, n))
        return msg

    @staticmethod
    def modinv(a, m):
        g, x, y = RSA.gcd_extended(a, m)
        if g != 1:
            return None
        else:
            return x % m

    @staticmethod
    def gcd_extended(a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = RSA.gcd_extended(b % a, a)
            return g, x - (b // a) * y, y

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def is_prime(n, k=128):
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0:
            return False
        s = 0
        r = n - 1
        while r & 1 == 0:
            s += 1
            r //= 2
        for _ in range(k):
            a = random.randrange(2, n - 1)
            x = pow(a, r, n)
            if x != 1 and x != n - 1:
                j = 1
                while j < s and x != n - 1:
                    x = pow(x, 2, n)
                    if x == 1:
                        return False
                    j += 1
                if x != n - 1:
                    return False
        return True

    @staticmethod
    def __get_number(length):
        p = random.getrandbits(length)
        p |= (1 << length - 1) | 1
        return p

    @staticmethod
    def get_prime(length=1024):
        p = 4
        while not RSA.is_prime(p, 128):
            p = RSA.__get_number(length)
        return p