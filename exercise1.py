from typing import Tuple

class VernamCipher:
    """
    The Vernam cipher has a structure similar to that of a stream cipher.
    However, the keystream is a random byte sequence which is exactly as long as the plaintext and is only used once.

    If no key is supplied the cipher is initialised for encryption. Otherwise, the cipher is initialised for decryption.

    Attributes:
        key (bytes): The key to use for encryption/decryption
    """
    def __init__(self, key: bytes = None) -> None:
        if key is not None:
            self.key = key

    def encrypt(self,plaintext: bytes) -> Tuple[bytes, bytes]:
        """
        Enciphers a plaintext

        TODO: This method should:
            1. Creates a random key which is exactly as long as the plaintext.
            2. Encrypt the plaintext by XORing with the key
            3. Return the ciphertext and key

        Parameters:
            plaintext (bytes): The plaintext to be encrypted

        Returns:
            Tuple[bytes,bytes]: The ciphertext and key
        """
        # TODO: REPLACE WITH YOUR IMPLEMENTATION
        ciphertext = b""
        key = b""
        return (ciphertext, key)

    def decrypt(self,ciphertext: bytes) -> bytes:
        """
        Deciphers a ciphertext

        TODO: This method should:
            1. Decrypt the ciphertext by XORing with the key
            2. Return the plaintext

        Parameters:
            ciphertext (bytes): The ciphertext to be decrypted

        Returns:
            bytes: The plaintext
        """
        # TODO: REPLACE WITH YOUR IMPLEMENTATION
        plaintext = b""
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