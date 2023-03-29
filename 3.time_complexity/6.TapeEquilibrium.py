"""A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and 
A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
"""


def solution1(A):
    values = []
    for i in range(1, len(A)):
        values.append(abs(sum(A[:i]) - sum(A[i:])))
    return min(values)


def solution2(a):
    l = len(a)
    min_sum = None  # min sum
    left_side = 0  # sum left
    right_side = sum(a)

    for p in range(0, l - 1):
        left_side = left_side + a[p]
        right_side = right_side - a[p]
        absolute = abs(left_side - right_side)
        if min_sum == None:
            min_sum = absolute
        if min_sum > absolute:
            min_sum = absolute
    return min_sum


A = [-1000, 1000]

x1 = solution1(A)
x2 = solution2(A)

print(x1, x2)
