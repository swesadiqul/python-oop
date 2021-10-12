# from first_module import Students as s
# from first_module import Human as h

import first_module
from second_module import Animal as a


obj = first_module.Students('Sobhan Ali',900243)
obj.show_name()
obj.show_roll()
print("\n")

ob2 = first_module.Human('Suzana',900217,'pitza')
ob2.show_name()
ob2.show_roll()
ob2.show_food()
print("\n")

ob3 = a('Rabeya',900245,'Rice','Pet animal')
ob3.show_name()
ob3.show_roll()
ob3.show_food()
ob3.show_pet()
