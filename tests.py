import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

  def test1(self):
    self.assertFalse(check_pwd('apply'))


if __name__ == '__main__':
    unittest.main()