import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertFalse(check_pwd('apply'))

    def test2(self):
        self.assertFalse(check_pwd('antidisestablishmentarianism'))

    def test3(self):
        self.assertFalse(check_pwd('thispwdisbad'))

    def test4(self):
        self.assertFalse(check_pwd('THISPWDALSOBAD'))

    def test5(self):
        self.assertFalse(check_pwd('StillNotGood'))

    def test6(self):
        self.assertFalse(check_pwd('AlmostRight23'))


if __name__ == '__main__':
    unittest.main()