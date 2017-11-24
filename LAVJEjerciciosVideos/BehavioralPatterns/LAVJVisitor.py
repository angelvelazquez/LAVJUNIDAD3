"""lUIS ANGEL VELAZZQUEZ JIMENEZ"""
"""GRUPO:GITI-9072-e"""
"""NO:1215100974"""

class House(object): 
    def accept(self, visitor):
        """Interface to accept a visitor"""
       
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist) 

    def work_on_electricity(self, electrician):
        print(self, "woorked on by", electrician)
        

    def __str__(self):
        """Simpy return the class name when the House object is printed"""
        return self.__class__.__name__


class Visitor(object):
    """Abstract visitor"""
    def __str__(self):
        """Simply return the class name when the visitor object is printed"""
        return self.__class__.__name__

class HvacSpecialist(Visitor): 
    """Concrete visitor: HVAC specialist"""
    def visit(self, house):
        house.work_on_hvac(self) 

class Electrician(Visitor): 
    """Concrete visitor: electrician"""
    def visit(self, house):
        house.work_on_electricity(self)
        

hv = HvacSpecialist()

e = Electrician()

home = House()

home.accept(hv)

home.accept(e)
