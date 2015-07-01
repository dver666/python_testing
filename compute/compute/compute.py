class Compute(object):
    def add(self, x, y):
        """Takes two integers and adds them together to produce result.
        >>> c=Compute()
        >>> c.add(1,1)
        3
        >>> c=Compute()
        >>> c.add(25,125)
        150
        >>> c=Compute()
        >>> c.add(1.0, 1.0)
        Traceback (most recent call last):
         ...
        TypeError: Invalid type: {<type 'float'>} and {<type 'float'>}
        """
        if type(x) == int and type(y) == int:
            return x+y
        #elif type(x) == str and type(y) == str:
        #    return x+y
        else:
            # also check that format down below
            raise TypeError("Invalid type: {%s} and {%s}" % (type(x),type(y)))
            #raise TypeError("Invalid type: {} and {}".format(type(x),type(y)))

if __name__=='__main__':
    import doctest
    doctest.testmod(extraglobs={'c': Compute()})

    #comp1=Compute()
    #result=comp1.add(2,2)
    #print result

    #comp2=Compute()
    #result=comp2.add("Hello","World")
    #print result
