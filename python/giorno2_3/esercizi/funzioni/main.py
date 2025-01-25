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

