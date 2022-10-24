import unittest
import cryptography

class Testcryptography(unittest.TestCase):

      def test_encrypt(self):
         result = cryptography.encrypt()
         self.assertEqual(result, '')

if __name__ == '__main__':
    unittest.main()
