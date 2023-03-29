"""This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""


def solution(A):
    A = set(A)
    for i in range(1, len(A) + 2):
        print(i)
        if i not in A:
            return i
    return 1


A = [1, 3, 6, 4, 1, 2]
A = [1, 2, 3]

x = solution(A)
print(x)
