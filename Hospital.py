#TODO ADD EVERY IMPORT
#Script file for testing our implementation
from system import System

hospital =  System()
adam = hospital.login(1,'password')
admin = hospital.login(3,'password')

#hospital.accountingData.changePrice(adam,'siggi', 222)
hospital.accountingData.changePrice(admin,'jón', 100000)




#TODO create all agents
# assign doctor to patient
# insurance provider looks up prices