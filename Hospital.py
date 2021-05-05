#TODO ADD EVERY IMPORT
#Script file for testing our implementation
from medicalData import MedicalData
from security import Security
from system import System
from patientData import PatientData

import sys
#TODO add command line functionality

## Initialize the System
hospital = System()
## User Registration ##

# patient login
patient = hospital.login(1,'password')
if (patient != None):
    print("Patient login successfully!")
else:
    sys.exit("Patient login failed!")

# doctor login
doctor = hospital.login(2, 'qwerty')
if (doctor != None):
    print("Doctor login successfully!")
else:
    sys.exit("Doctor login failed!")

# # Admin login
# admin = hospital.login(3, 'password')
# if (admin != None):
#     print("Admin login successfully!")
# else:
#     sys.exit("Admin login failed!")

#Insurance staff login
insurance = hospital.login(4, 'sebastian')
if (insurance != None):
    print("Insurance login successfully!")
else:
    sys.exit("Insurance login failed!")

## User Story 1: ##

# Data Initialization

# patient id 1 show his personal data
# insurance provider is id 4
patientData = PatientData('123456', 4, Security([1], [0,1])) 

# Doctor Assignment
hospital.assign_doc(2, 1)

# Doctor Check the Medical History
hospital.checkMedicalHistory(2, 1)

# Order a Treatment
hospital.orderTest(2, 1, 'Hospital bed for 1 night')

# patient leave the doctor
hospital.leave_doc(2, 1)

## User Story 2: ##

# Send the bill to insurance provider
hospital.sendBill(1, patientData)

# patient get back his/her doctor from the hospital
patientData.security.readers.remove(0) 

# Insurance provider check the bill and pay unpaid items
hospital.checkBillandPay(4, 1)

#hospital.accountingData.changePrice(patient,'bingkun', 66666)  #this will fail
# hospital.accountingData.changePrice(admin,'bingkun', 66666)

#TODO
# Make security policies private variables
# assign doctor to patient
# test doctor reading patient data
# insurance provider looks up prices
# Doctor request to add treatment, hospital admin approves/rejects