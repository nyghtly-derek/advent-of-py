import unittest
from inverse import solve_captcha_a

class TestInverseA(unittest.TestCase):
    """Tests for `inverse_a.py`."""

    def easy_tests(self):
        test_file = open("input/a.txt", 'r')
        self.assertEqual(
            solve_captcha_a( test_file.read() ), 3)
        test_file.close()
        test_file = open("input/b.txt", 'r')
        self.assertEqual(
            solve_captcha_a(test_file.read()), 4)
        test_file.close()
        test_file = open("input/c.txt", 'r')
        self.assertEqual(
            solve_captcha_a(test_file.read()), 0)
        test_file.close()
    
    def test_solution(self):
        captcha_file = open("input/mycaptcha.txt", 'r')
        captcha_str = captcha_file.read()
        if captcha_str[-1] == '\n':
            captcha_str = captcha_str[:-1] 
        self.assertEqual(
            solve_captcha_a(captcha_str), 1253) 
        captcha_file.close()

if __name__ == '__main__':
    unittest.main()
