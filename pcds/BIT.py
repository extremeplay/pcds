class BIT:
    """
    Binary Indexed Tree (also called Fenwick Tree)
    """

    def __init__(self, n):

        # size is n + 1 because we need index to start from 1
        self.a = [0] * (n + 1)

    @staticmethod
    def getlsd(n):
        # n & (n - 1) clears least significant bit
        # n ^ (n & (n - 1)) clears all bits except least significant bit
        # Example:
        # 110110002 = n
        # 110101112 = n - 1
        # 110100002 = n & (n - 1)
        # 110110002 = n
        # 000010002 = n ^ (n & (n - 1))

        return n ^ (n & (n - 1))

    def update(self, pos, val):

        if pos <= 0 or pos >= len(self.a):
            return False

        while pos < len(self.a):
            self.a[pos] += val
            pos += self.getlsd(pos)

        return True

    def query(self, le, ri):

        def query2(pos):
            sol = 0
            while pos > 0:
                sol += self.a[pos]
                pos -= self.getlsd(pos)
            return sol

        if le > ri or le <= 0 or ri >= len(self.a):
            return None

        # there is no better way to do this, solution described on TopCoder works only for ri == le
        return query2(ri) - query2(le - 1)
