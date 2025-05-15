import unittest
from bifid_cipher import *

class TestBifidCipher(unittest.TestCase):
    def setUp(self):
        self.square = create_polybius_square()
        self.key_square = create_polybius_square("KEYWORD")

    def test_encrypt_decrypt(self):
        plaintext = "CRYPTOGRAPHY"
        ciphertext = bifid_encrypt(plaintext, self.square)
        self.assertEqual(bifid_decrypt(ciphertext, self.square), "CRYPTOGRAPHY")

    def test_keyword_square(self):
        self.assertEqual(self.key_square[0], ['K', 'E', 'Y', 'W', 'O'])

if __name__ == "__main__":
    unittest.main()