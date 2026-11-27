from typing import Tuple

from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.strxor import strxor

class VernamCipher:
    """One-time pad: XOR with a random key as long as the message, used once.
    No key -> set up for encryption. Key given -> set up for decryption."""

    def __init__(self, key: bytes = None) -> None:
        if key is not None:
            self.key = key

    def encrypt(self, plaintext: bytes) -> Tuple[bytes, bytes]:
        """Make a random key the length of plaintext, XOR them. Returns (ciphertext, key)."""
        key = get_random_bytes(len(plaintext))
        ciphertext = strxor(plaintext, key)
        return (ciphertext, key)

    def decrypt(self, ciphertext: bytes) -> bytes:
        """XOR ciphertext with self.key. Returns plaintext."""
        plaintext = strxor(ciphertext, self.key)
        return plaintext


def main():
    alice_cipher = VernamCipher()
    message = b"Hello World!"
    ciphertext, key_bytes = alice_cipher.encrypt(message)
    print(ciphertext)
    bob_cipher = VernamCipher(key_bytes)
    plaintext = bob_cipher.decrypt(ciphertext)
    print(plaintext)
    assert plaintext == message


if __name__ == "__main__":
    main()
