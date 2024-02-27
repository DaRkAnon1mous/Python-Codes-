def sumsquare(l):

    odd_sum = sum(x ** 2 for x in l if x % 2 != 0)
    even_sum = sum(x ** 2 for x in l if x % 2 == 0)
    return [odd_sum, even_sum]

print(sumsquare([1,3,5]))


print(sumsquare([2,4,6]))


print(sumsquare([-1,-2,3,7]))
