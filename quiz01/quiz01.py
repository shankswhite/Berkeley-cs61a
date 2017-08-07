def diff(x, y, z):
    """Return whether one argument is the difference between the other two.

    x, y, and z are all integers.

    >>> diff(5, 3, 2) # 5 - 3 is 2
    True
    >>> diff(2, 3, 5) # 5 - 3 is 2
    True
    >>> diff(2, 5, 3) # 5 - 3 is 2
    True
    >>> diff(-2, 3, 5) # 3 - 5 is -2
    True
    >>> diff(-5, -3, -2) # -5 - -2 is -3
    True
    >>> diff(-2, 3, -5) # -2 - 3 is -5
    True
    >>> diff(2, 3, -5)
    False
    >>> diff(10, 6, 4)
    True
    >>> diff(10, 6, 3)
    False
    """
    if x - y == z:
        return True
    elif x - z == y:
        return True
    elif y - x == z:
        return True
    elif y - z == x:
        return True
    elif z - x == y:
        return True
    elif z - y == x:
        return True
    else:
        return False


def abundant(n):
    """Print all ways of forming positive integer n by multiplying two positive
    integers together, ordered by the first term. Then, return whether the sum
    of the proper divisors of n is greater than n.

    A proper divisor of n evenly divides n but is less than n.

    >>> abundant(12) # 1 + 2 + 3 + 4 + 6 is 16, which is larger than 12
    1 * 12
    2 * 6
    3 * 4
    True
    >>> abundant(14) # 1 + 2 + 7 is 10, which is not larger than 14
    1 * 14
    2 * 7
    False
    >>> abundant(16)
    1 * 16
    2 * 8
    4 * 4
    False
    >>> abundant(20)
    1 * 20
    2 * 10
    4 * 5
    True
    >>> abundant(22)
    1 * 22
    2 * 11
    False
    >>> r = abundant(24)
    1 * 24
    2 * 12
    3 * 8
    4 * 6
    >>> r
    True
    """
    total, k = 0, 1
    while k < n and n // k <= k :
        if n % k == 0:
            print(k, '*', n // k)
            total = total + k + n // k
        k = k + 1
    return total > n


def amicable(n):
    """Return the smallest amicable number greater than positive integer n.

    Every amicable number x has a buddy y different from x, such that
    the sum of the proper divisors of x equals y, and
    the sum of the proper divisors of y equals x.

    For example, 220 and 284 are both amicable because
    1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 is 284, and
    1 + 2 + 4 + 71 + 142 is 220

    >>>amicable(5)
    220
    >>> amicable(220)
    284
    >>> amicable(284)
    1184
    >>> r = amicable(5000)
    >>> r
    5020
    """
    n = n + 1
    while True:
        m = sum_divisors(n)
        if m != n and sum_divisors(m) == n:
            return n
        n = n + 1

def sum_divisors(n):
    d, total = 1, 0
    while d< n:
        if n % d == 0:
            total = total + d
        d = d + 1
    return total
