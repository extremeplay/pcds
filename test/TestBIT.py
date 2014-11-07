from pcds import BIT
from unittest import TestCase, main


class TestBIT(TestCase):

    def testcase1(self):

        SIZE = 3
        b = BIT(SIZE)

        b.update(1,10)
        b.update(2,9)
        self.assertEqual(b.query(1,2), 19)
        b.update(3,8)
        self.assertEqual(b.query(1,3), 27)
        self.assertEqual(b.query(2,3), 17)

    def testcase2(self):
        SIZE = 1
        b = BIT(SIZE)
        b.update(1,3333)
        self.assertEqual(b.query(1,1),3333)

if __name__ == '__main__':
    main()

