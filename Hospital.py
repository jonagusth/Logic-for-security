#TODO ADD EVERY IMPORT
#Script file for testing our implementation
from medicalData import MedicalData
from security import Security
from System import System
from patientData import PatientData

import sys

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

# Admin login
admin = hospital.login(3, 'password')
if (admin != None):
    print("Admin login successfully!")
else:
    sys.exit("Admin login failed!")

#TODO insurance staff login

## User Story 1: ##

# Data Initialization
pdSecure = Security([patient], [patient])
patientData = PatientData('cpr0123', 'syge', pdSecure)

mdSecure = Security([hospital], [patient])
medicalData = MedicalData([], mdSecure)

hospital.assign_doc(doctor, patient) # assign a doctor
medicalData.security.add_reader(doctor) 


# Changing Accounting data

#hospital.accountingData.changePrice(patient,'bingkun', 66666)  #this will fail
hospital.accountingData.changePrice(admin,'bingkun', 66666)

#TODO create all agents
# assign doctor to patient
# insurance provider looks up prices