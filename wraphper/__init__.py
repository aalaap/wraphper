
__version__ = '0.0.2'

def count(array):
    """
    Returns the count of items in a in the list, dictionary or tuple.

    This is a wrapper for the PHP count() function that returns the count of items in an array.

    Parameters:
    array (list, dict, tuple): A list or a dictionary or a tuple.

    Returns:
    int: Count of the items.
    """

    if not isinstance(array, (list, dict, tuple)):
        raise TypeError('Parameter must be an array or an object that implements Countable')
    
    return len(array)

def str_replace(search, replace, subject, count=-1):
    """
    Replace all occurrences of the search string with the replacement string.

    This is a wrapper for the PHP str_replace function that returns a string or an array with all occurrences of search in subject replaced with the given replace value.

    Parameters:
    search: The value being searched for, otherwise known as the needle.
    replace: The replacement value that replaces found search values.
    subject: The string or array being searched and replaced on, otherwise known as the haystack.
    count: If passed, this will be set to the number of replacements performed.

    returns:
    str or array: The subject with the values replaced.
    """

    # str, str, str
    if isinstance(search, str) and isinstance(replace, str) and isinstance(subject, str):
        return subject.replace(search, replace, count)

    # list, str, str
    if isinstance(search, list) and isinstance(replace, str) and isinstance(subject, str):
        ret = subject

        for sea in search:
            ret = ret.replace(sea, replace, count)
        
        return ret

    # str, list, str
    if isinstance(search, str) and isinstance(replace, list) and isinstance(subject, str):
        # This would cause PHP to return the word 'Array' instead of the replacement keywords, but we should just thrown an exception
        raise TypeError('Replace argument can\'t be an array if search is a string')

    # list, list, str
    if isinstance(search, list) and isinstance(replace, list) and isinstance(subject, str):      
        ret = subject

        for i, sea in enumerate(search):
            ret = ret.replace(sea, replace[i], count)
        
        return ret

    # *, * list, so recurse
    if isinstance(subject, list):
        ret = []

        for sub in subject:
            ret.append(str_replace(search, replace, sub, count))
        
        return ret
