from saes import SimplifiedAES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.strxor import strxor
from Cryptodome.Util.Padding import pad, unpad


class SAES_CBC:
    """CBC mode around Simplified AES. Key and IV are both 2 bytes (one block)."""

    def __init__(self, key: bytes, iv: bytes = None) -> None:
        self.blocksize = 2
        if len(key) != self.blocksize:
            raise ValueError("Key must be 2 bytes")
        self.key = key

        if iv is None:
            iv = get_random_bytes(self.blocksize)
        elif len(iv) != self.blocksize:
            raise ValueError("IV must be 2 bytes")
        self.iv = iv

        self.block_cipher = SimplifiedAES(self.key)

    def encrypt(self, plaintext: bytes) -> bytes:
        """CBC encrypt with self.block_cipher. Plaintext is already padded."""
        ciphertext = b""
        previousBlock = self.iv
        currentBlockSize = self.blocksize

        for i in range(0, len(plaintext), currentBlockSize): 
            currentBlock = plaintext[i: i+currentBlockSize] 
            xorBlock = strxor(currentBlock, previousBlock)
            temp = self.block_cipher.encrypt(xorBlock)

            ciphertext += temp
            previousBlock = temp

        return ciphertext

    def decrypt(self, ciphertext: bytes) -> bytes:
        """CBC decrypt with self.block_cipher. Returns padded plaintext."""
        plaintext = b""
        previousBlock = self.iv
        currentBlockSize = self.blocksize

        for i in range(0, len(ciphertext), currentBlockSize):
            currentBlock = ciphertext[i: i+currentBlockSize]
            decryptedBlock = self.block_cipher.decrypt(currentBlock)
            temp = strxor(decryptedBlock, previousBlock)

            plaintext += temp
            previousBlock = currentBlock
        return plaintext


if __name__ == "__main__":
    key = get_random_bytes(2)
    iv = get_random_bytes(2)
    print("key:", key.hex(), " iv:", iv.hex())

    saes_cbc = SAES_CBC(key, iv)
    plaintext = b"The quick brown fox jumps over the lazy dog"
    padded_plaintext = pad(plaintext, 2)
    print(padded_plaintext)

    ciphertext = saes_cbc.encrypt(padded_plaintext)
    print(ciphertext.hex())

    decrypted = saes_cbc.decrypt(ciphertext)
    print(decrypted)
    print(unpad(decrypted, 2))
