def factorial(n):
    if( n<2):
        return 1
    else:
        return n*(factorial(n-1))
n=5
res = factorial(n)
print('Factorial of '+str(n) +' is ' +str(res))