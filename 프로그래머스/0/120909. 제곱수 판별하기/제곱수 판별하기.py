def solution(n):
    SquareRoot = n ** (1/2)
    if SquareRoot % 1 == 0:
        return 1
    else:
        return 2