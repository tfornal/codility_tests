"""A non-empty array A consisting of N integers is given. A pair of integers (P, Q), 
such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains 
at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] 
divided by the length of the slice. To be precise, 
the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q - P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of the 
slice with the minimal average. If there is more than one slice with a minimal average, you should 
return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
"""

A = [4, 2, 2, 5, 1, 1, 5, 8]


def min_check(avg_min, avg_tmp, idx_min, idx_tmp):
    if avg_tmp < avg_min:
        return idx_tmp, avg_tmp
    else:
        return idx_min, avg_min


def solution(A):
    idx_max = len(A) + 1
    idx_min, avg_min = 0, sum(A[0:2]) / 2
    if idx_max == 2:
        return idx_min
    for idx in range(3, idx_max):
        idx2, idx3 = idx - 2, idx - 3
        avg_tmp2 = sum(A[idx2:idx]) / 2
        avg_tmp3 = sum(A[idx3:idx]) / 3
        idx_min, avg_min = min_check(avg_min, avg_tmp2, idx_min, idx2)
        idx_min, avg_min = min_check(avg_min, avg_tmp3, idx_min, idx3)
    print(idx_min)
    return idx_min


solution(A)
