def factorial(n):
    """Calculate the factorial of the given number"""
    # FIXME: this code has a bug!
    if n > 1:
<<<<<<< HEAD
        return n * factorial(n-1)
=======
        return n * factorial(n)
>>>>>>> c0cfee5bfedeb9cc42cc5c2ee52848283cc4e912
    else:
        return 1


assert factorial(5) == 120
