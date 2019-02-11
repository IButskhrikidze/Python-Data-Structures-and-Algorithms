from math import sqrt, floor


def Num_Divisors(n):
    cnt = 0
    sq = floor(sqrt(n))
    for i in range(1, sq + 1):
        if n % i == 0:
            cnt += 2

    if sq * sq == n:
        cnt -= 1

    return cnt


def Sum_Divisors(n):
    cnt = 0
    sq = floor(sqrt(n))
    for i in range(1, sq + 1):
        if n % i == 0:
            cnt += i + n // i

    if sq * sq == n:
        cnt -= sq

    return cnt


n = int(input())

print("Number of divisors of {} is {}".format(n, Num_Divisors(n)))
print("Sum of divisors of {} is {}".format(n, Sum_Divisors(n)))
