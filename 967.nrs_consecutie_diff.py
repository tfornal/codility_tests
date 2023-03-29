"""Given two integers n and k, return an array of all the integers of length n where the difference 
between every two consecutive digits is k. You may return the answer in any order.

Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.
Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
"""


def solution(n, k):
    liczby = []
    for i in range(0, 11):
        if i + k < 10:
            if n % 2 == 0:
                liczby.append(str(i))
                liczby.append(str(i + k))
            # print(n * str(i), str(k))
            print(liczby)


n = 2
k = 3
x = solution(n, k)
print(x)
