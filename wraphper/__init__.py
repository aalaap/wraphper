
__version__ = '0.0.1.post2'

def count(array):
    """
    Returns the count of items in a in the list, dictionary or tuple.

    This is a wrapper for the PHP count() function that returns the count of items in an array.

    Parameters:
    array (list, dict, tuple): A list or a dictionary or a tuple

    Returns:
    int: Count of the items 
    """

    if type(array) not in (list, dict, tuple):
        raise TypeError('Parameter must be an array or an object that implements Countable')
    
    return len(array)
