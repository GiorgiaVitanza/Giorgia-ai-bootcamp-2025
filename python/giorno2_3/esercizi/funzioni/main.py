# Scrivere il codice dell'esercizio qui dentro

def mydivmod(num1, num2):
    """ Implementare una funzione chiamata `mydivmod()` che replichi il funzionamento
    della funzione *builtin* `divmod()` (senza riutilizzarla!). 
    Gestite la divisione per zero *dentro* la funzione.

    Per verificare la *signature* della funzione originale, aprire una console Python
    e dare il seguente comando:

    ```
    >>> help(divmod)
    ... """
    try:
        div = num1//num2
        mod = num1%num2
    except ZeroDivisionError:
        print('Zero Division error, change the second input!')
    output = (div, mod)
    return output

def pow_list(li):
    "Implement a function that takes a list "
    "and returns another list with each value raised "
    "to the power of 2"
    new_li = []
    for el in li:
        new_li.append(el**2)
    return new_li

def count_words(string):
    "Implement a trivial function that counts the "
    "number of words in the given string. "
    "Hint: try executing the following command in the "
    "Python console: 'hello world'.split(' ')"
    return len(string.split(' '))

def reverse_string(string): 
    "Implement a function that takes a string "
    "and returns it reversed. For example, 'hello' becomes 'olleh'."
    new_string = ""
    for i in range(len(string)):
        new_string += string[-(i+1)]
    return new_string

def factorial(num):
    "Implement a function that computes the factorial of a given number. "
    "Factorial of n (n!) is the product of all positive integers from 1 to n. "
    "For example, factorial(5) = 5 * 4 * 3 * 2 * 1."
    try:
        if num > 1:
            new_num = num * factorial(num-1)
        else:
            new_num = 1
        return new_num
                
    except Exception:
        print('ValueError')
    

def is_palindrome(string):
    "Implement a function that checks if a given string is a palindrome. "
    "A palindrome reads the same forwards and backwards, e.g., 'racecar'. "
    "Hint: try executing the following command in the "
    "Python console: 'racecar'[::-1]"
    if string == string[::-1]:
        return True
    else:
        return False

def sum_even_numbers(li):
    "Implement a function that takes a list of numbers "
    "and returns the sum of all even numbers in the list."
    new_li = []
    for el in li:
        # even numbers in the list
        if el%2 == 0:
            new_li.append(el)
    return sum(new_li)

def find_max(li):
    "Implement a function that takes a list of numbers "
    "and returns the largest number in the list."
    return max(li)

def count_vowels(string):
    "Implement a function that takes a string "
    "and returns the count of vowels ('a', 'e', 'i', 'o', 'u') in it. "
    "For example, 'hello world' contains 3 vowels."
    vowels = ('a', 'e', 'i', 'o', 'u')
    vowels_count = 0
    for letter in string:
        if letter in vowels:
            vowels_count += 1
    return vowels_count


print(factorial(5))