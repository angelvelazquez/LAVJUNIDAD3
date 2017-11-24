"""lUIS ANGEL VELAZZQUEZ JIMENEZ"""
"""GRUPO:GITI-9072-e"""
"""NO:1215100974"""

class Borg:
    """Borg class marking class attributes global"""
    _shared_state = {} 

    def __init__(self):
        self.__dict__ = self._shared_state 


class Singleton(Borg): 
    """This class now shares all its attributes among its vaious instances"""
    
    def __init__(self, **kwargs):
        Borg.__init__(self)
        
        self._shared_state.update(kwargs)

    def __str__(self):
        
        return str(self._shared_state)

x = Singleton(HTTP = "Hyper Text Transfer Protocol")

print(x)

y = Singleton(SNMP = "Simple Network Managment Protocol")

print(y)
