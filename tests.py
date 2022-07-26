import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertFalse(check_pwd('apply'))

    def test2(self):
        self.assertFalse(check_pwd('antidisestablishmentarianism'))


if __name__ == '__main__':
    unittest.main()