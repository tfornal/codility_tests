"""
This is a demo task.

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
import time


def solution(A):
    s = set(A)
    m = max(A)
    for N in range(1, m + 2):
        print(N)
        time.sleep(1)
        if N not in s:
            return N
    return 1


A = [1, 2, 4, 3]
# A = [-10, 1, 3, 6, 4, 12, 25, 2, 6, 9, 2]
x = solution(A)
print(x)
