import unittest

from Cryptodome.Random import get_random_bytes

import exercise3

class TestARC4(unittest.TestCase):
    def test_encrypt(self):
        encoded_key = 'e304c0590b8021157bf83f6194e459083e1fe4f11731df66e00504f2fe6a7642'
        key = bytes.fromhex(encoded_key)
        rc4_cipher = exercise3.ARC4(key)
        ciphertext = rc4_cipher.encrypt(b'The quick brown fox jumps over the lazy dog')
        self.assertEqual(ciphertext.hex(), '730f7a8bfcad1eee2b9d6f7ba87abd6f2ffa474510c30694bb111d9fcc9af22e788df994c906079b9d74ad')

    def test_decrypt(self):
        encoded_key = 'e304c0590b8021157bf83f6194e459083e1fe4f11731df66e00504f2fe6a7642'
        key = bytes.fromhex(encoded_key)
        encoded_ciphertext = '730f7a8bfcad1eee2b9d6f7ba87abd6f2ffa474510c30694bb111d9fcc9af22e788df994c906079b9d74ad'
        ciphertext = bytes.fromhex(encoded_ciphertext)
        rc4_cipher = exercise3.ARC4(key)
        plaintext = rc4_cipher.decrypt(ciphertext)
        self.assertEqual(plaintext, b'The quick brown fox jumps over the lazy dog')

    def test_consistency(self):
        key = get_random_bytes(32)
        rc4_cipher1 = exercise3.ARC4(key)
        message = b'The quick brown fox jumps over the lazy dog'
        ciphertext = rc4_cipher1.encrypt(message)
        rc4_cipher2 = exercise3.ARC4(key)
        plaintext = rc4_cipher2.decrypt(ciphertext)
        self.assertEqual(plaintext, message)

