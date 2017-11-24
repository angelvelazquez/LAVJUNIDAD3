"""Luis Angel Velazquez Jimenez"""
"""Grupo:GITI-9072-e"""
"""No:1215100974"""
def count_to(count):
    """Our iterator implementation"""

    
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

 
    iterator = zip(range(count), numbers_in_german)

    
    for position, number in iterator:

       
        yield number 



for num in count_to(3):
    print("{}".format(num))


for num in count_to(4):
    print("{}".format(num))
