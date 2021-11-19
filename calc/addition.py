



from calc.calculation import Calculation

#This is how you extend the Addition class with the Calculation
class Addition(Calculation):
    """The addition class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""
    def get_Result(self):

        return self.value_a + self.value_b