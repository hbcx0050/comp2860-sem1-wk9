from Cryptodome.Random import get_random_bytes

class ARC4:
    """
    Attributes:
        S (list): The internal state of the ARC4 cipher. It is an array of 256 8-bit unsigned integers.
    """
    def __init__(self, key: bytes) -> None:
        """
        TODO: The constructor should implement the ARC4 key scheduling algorithm (KSA) as specified on the worksheet

        Parameters:
            key (bytes): The key should be 5 to 256 bytes long
        """
        # TODO: REPLACE WITH YOUR IMPLEMENTATION
        pass

    def prga(self, keystream_length:int) -> bytes:
        """
        TODO: This function should implement the ARC4 pseudorandom generation algorithm (PRGA) as specified on the worksheet

        Parameters:
            keystream_length (int): The plaintext length

        Returns:
            bytes: The keystream
        """
        # TODO: REPLACE WITH YOUR IMPLEMENTATION
        keystream = b""
        return keystream

    def encrypt(self, plaintext:bytes) -> bytes:
        """
        Encrypts the plaintext using the ARC4 cipher.

        TODO: Your implementation should:
            1. Generate a keystream as long as the plaintext
            2. XOR the keystream with the plaintext

        Parameters:
            plaintext (bytes): The plaintext to be encrypted
        Returns:
            bytes: The ciphertext
        """
        # TODO: REPLACE WITH YOUR IMPLEMENTATION
        ciphertext = b""
        return ciphertext

    def decrypt(self, ciphertext:bytes) -> bytes:
        """
        Decrypts the ciphertext using the ARC4 cipher.

        TODO: Your implementation should:
            1. Generate a keystream as long as the ciphertext
            2. XOR the keystream with the ciphertext

        Parameters:
            ciphertext (bytes): The ciphertext to be decrypted
        Returns:
            bytes: The plaintext
        """
        # TODO: REPLACE WITH YOUR IMPLEMENTATION
        plaintext = b""
        return plaintext

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