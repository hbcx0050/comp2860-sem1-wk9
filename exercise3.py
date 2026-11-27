from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.strxor import strxor


class ARC4:
    """RC4 stream cipher. self.S is the 256-byte internal state."""

    def __init__(self, key: bytes) -> None:
        """Key scheduling algorithm (KSA). Key is 5-256 bytes."""
        if not 5 <= len(key) <= 256:
            raise ValueError("Key must be 5-256 bytes")

        # Start with S = 0..255, then shuffle it using the key.
        self.S = list(range(256))
        j = 0
        for i in range(256):
            j = (j + self.S[i] + key[i % len(key)]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]

        # PRGA position, kept so successive calls continue the same stream.
        self.i = 0
        self.j = 0

    def prga(self, keystream_length: int) -> bytes:
        """Pseudorandom generation algorithm (PRGA). Returns keystream_length bytes."""
        S = self.S
        keystream = bytearray()
        for _ in range(keystream_length):
            self.i = (self.i + 1) % 256
            self.j = (self.j + S[self.i]) % 256
            S[self.i], S[self.j] = S[self.j], S[self.i]
            keystream.append(S[(S[self.i] + S[self.j]) % 256])
        return bytes(keystream)

    def encrypt(self, plaintext: bytes) -> bytes:
        """XOR plaintext with a keystream of the same length."""
        return strxor(plaintext, self.prga(len(plaintext)))

    def decrypt(self, ciphertext: bytes) -> bytes:
        """XOR ciphertext with a keystream of the same length."""
        return strxor(ciphertext, self.prga(len(ciphertext)))


def main():
    key = get_random_bytes(32)
    alice_cipher = ARC4(key)
    message = b"Hello World!"
    ciphertext = alice_cipher.encrypt(message)
    print(ciphertext)
    bob_cipher = ARC4(key)
    plaintext = bob_cipher.decrypt(ciphertext)
    print(plaintext)
    assert plaintext == message


if __name__ == "__main__":
    main()
