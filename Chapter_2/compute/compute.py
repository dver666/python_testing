class Compute(object):
    def add(self, x, y):
        number_types=(int,long,float,complex)
        if isinstance(x,number_types) and isinstance(y,number_types):
            return x+y
        else:
            raise ValueError

        #if type(x) == int and type(y) == int:
        #    return x+y
        #else:
        #    raise TypeError("Invalid type: {%s} and {%s}" % (type(x),type(y)))
            ##raise TypeError("Invalid type: {} and {}".format(type(x),type(y)))

if __name__=='__main__':
    comp=Compute()
    result=comp.add(2,2)
    #result=comp.add("Hello","World")
    print result
