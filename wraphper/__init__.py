
class wraphper(object):

    @classmethod
    def count(self, array):
        """
        Returns the count of items in a in the list or dictionary.

        This is a wrapper for the PHP count() function that returns the count of items in an array, a.k.a. lists or dictionaries.

        Parameters:
        array (list, dict): A list or a dictionary

        Returns:
        int: Count of the items 
        """
        if type(array) not in (list, dict):
            raise TypeError('Parameter must be an array or an object that implements Countable')
        
        return len(array)
