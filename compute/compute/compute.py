class Compute(object):
    """
    class Compute(object)
    
    you defined wanted behavior in method add
    
    write a test to cover it
    
    write new test that checks that the TypeError is raised
    when you pass in strings
    
    use assertRaises from unittest
    """
    def add(self, x, y):
        if type(x) == int and type(y) == int:
            return x+y
        #elif type(x) == str and type(y) == str:
        #    return x+y
        else:
            # also check that format down below
            raise TypeError("Invalid type: {%s} and {%s}" % format(type(x),type(y)))

if __name__=='__main__':
    comp1=Compute()
    result=comp1.add(2,2)
    print result

    comp2=Compute()
    result=comp2.add("Hello","World")
    print result
