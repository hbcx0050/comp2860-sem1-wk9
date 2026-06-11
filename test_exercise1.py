import unittest
import exercise1

class TestVernamCipher(unittest.TestCase):
    def test_decrypt(self):
        message = b'The quick brown fox jumps over the lazy dog'
        encoded_key = '3eec515f561be38892314e2d81855ecb7f07a06846da9029361ea825dd704fa47c730fb64afdc3c213fea9'
        key = bytes.fromhex(encoded_key)
        encoded_ciphertext = '6a84347f276e8aebf9112c5feef230eb1968d8482caffd59453ec753b8026fd014162fda2b87bae27791ce'
        ciphertext = bytes.fromhex(encoded_ciphertext)
        vernam_cipher = exercise1.VernamCipher(key)
        plaintext = vernam_cipher.decrypt(ciphertext)
        self.assertEqual(plaintext,message)

    def test_consistency(self):
        message = b'The quick brown fox jumps over the lazy dog'
        vernam_cipher1 = exercise1.VernamCipher()
        key, ciphertext = vernam_cipher1.encrypt(message)
        vernam_cipher2 = exercise1.VernamCipher(key)
        plaintext = vernam_cipher2.decrypt(ciphertext)
        self.assertEqual(plaintext,message)
