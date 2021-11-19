from calc.calculation import Calculation

#This is how you extend the Addition class with the Calculation
class division(Calculation):
    """The addition class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""
    def getResult(self):
        #you need to use self to reference the data contained in the instance of the object.  This is encapsulation
        return self.value_a / self.value_b