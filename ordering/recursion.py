def sum_array(array):
    
    '''
    Returns the sum of all items in array 
    
    Args:
        array: list or array-like object containing numerical values
        
    Returns:
        int: sum of all items in array

    Examples:
        >>> sum_array([8, 3, 2, 7, 4])
        24
        >>> sum_array([1,2,3,4,5])
        15
    '''
    
    if len(array) <= 0:
        return 0
    return array[0] + sum_array(array[1:]) 



def fibonacci(n):
    
    '''
    Returns nth term in fibonacci sequence
    
     Args:
        n: int
        
    Returns:
        int: nth term in fibonacci sequence

    Examples:
        >>> fibonacci(6)
        8    
        >>> fibonacci(10)
        55
    '''

    if n < 0:
        print('Error. Input must be greater than -1')
    elif n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)



def factorial(n):
    
    '''
    Returns n!
    
     Args:
        n: int
        
    Returns:
        int: n!

    Examples:
        >>> factorial(6)
        720 
        >>> factorial(4)
        24
    '''

    if n < 0:
        print('Error. Input must be greater than 0')
    elif n <= 1:
        return 1
    else:
        return n*factorial(n-1)



def reverse(word):
    
    '''
    Returns an array in reverse order
    
    Args:
        array: list or array-like object containing values
        
    Returns:
        array: in reverse order

    Examples:
        >>> reverse('8, 3, 2, 7, 4')
        '4 ,7 ,2 ,3 ,8'
        >>> reverse('bob, jen, ann, reg and kip')
        'pik dna ger ,nna ,nej ,bob'
    '''

    if len(word) == 0:
        return word
    return reverse(word[1:]) + word[0]
