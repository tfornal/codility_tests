"""A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
"""


# def solution(N):
#     n = bin(N)[2:]

#     n_str = str(n)
#     lista = list(n_str)
#     ones_idx = []
#     for index, numer in enumerate(lista):
#         if int(numer) == 1:
#             ones_idx.append(index)
#     max_bin = []
#     for i, j in enumerate(ones_idx):
#         if len(ones_idx) <= 1:
#             return 0
#         if i == 0:
#             continue
#         max_bin.append(ones_idx[i] - ones_idx[i - 1])
#     solution = max(max_bin)
#     if solution > 1:
#         return solution - 1
#     else:
#         return 0


def solution(n):
    b = bin(n)[2:]
    print(b)
    l = b.strip("0").split("1")
    print(l)
    return max([len(x) for x in l])


N = 4
x = solution(N)
print(x)
# xs = bin(N)[2:].strip('0').split('1')
# return max([len(x) for x in xs])
