if 1: # ideas
    """
    >>> def a(i):
    ...     return ''.join(map(str, range(1, i+1)))
    >>> a(1)
    '1'
    >>> a(4)
    '1234'
    >>> a(10)
    '12345678910'

    >>> def b(i):
    ...     return ''.join(a(j) for j in range(1, i+1))
    >>> b(1)
    '1'
    >>> b(4)
    '1121231234'
    >>> b(10)
    '11212312341234512345612345671234567812345678912345678910'

    >>> def c(i):
    ...     return sum(i//10+1 for i in range(1, i+1))
    >>> c(1)
    1
    >>> c(4)
    4
    >>> c(10)
    11

    >>> def d(i):
    ...     return c(i) == len(a(i))
    >>> d(1)
    True
    >>> d(4)
    True
    >>> d(10)
    True
    """

with open('./input.txt') as file:
    lines = [int(i.reaplce('\n', '')) for i in file.readlines()]
runtime, *lines = lines