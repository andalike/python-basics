def factorial(n):
    if n == 0 or n==1:
        return 1
    return n * factorial(n-1)

# a=factorial(6)
# print(a)

# 0,1,1,2,3,5,8,13,21,34

def fibonacchi(n):
    if n<=1:
        return n
    return fibonacchi(n-1) + fibonacchi(n-2)

# a=fibonacchi(30)
# print(a)

# 729 = 7 + 2 + 9

def sum_pf_digits(n):
    if n<10:
        return n
    return n%10 + sum_pf_digits( n // 10)

a=sum_pf_digits(910)
print(a)



