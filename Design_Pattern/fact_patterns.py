from abc import ABCMeta, abstractmethod

class IProduct(metaclass=ABCMeta):
    '''Class interface (PRODUCT) '''

    @staticmethod
    @abstractmethod
    def create_object():
        '''An abstract interface method'''


class ConcreteProductA(IProduct):

    def __init__(self):
        self.name = "Product A"

    def create_object(self):
        return self


class ConcreteProductB(IProduct):

    def __init__(self):
        self.name = "Product B"

    def create_object(self):
        return self


class ConcreteProductC(IProduct):

    def __init__(self):
        self.name = "Product C"

    def create_object(self):
        return self

class Creator:
    '''Factory Class'''

    @staticmethod
    def create_object(some_property):

        if some_property == "a":
            return ConcreteProductA()
        if some_property == "b":
            return ConcreteProductB()
        if some_property == "c":
            return ConcreteProductC()
        return  None


if __name__=="__main__":

    #The CLient
    PRODUCT = Creator.create_object("c")
    print(PRODUCT.name)



