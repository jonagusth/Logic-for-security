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

# Admin login
admin = hospital.login(3, 'password')
if (admin != None):
    print("Admin login successfully!")
else:
    sys.exit("Admin login failed!")

#Insurance staff login
insurance = hospital.login(4, 'password')
if (admin != None):
    print("Insurance login successfully!")
else:
    sys.exit("Insurance login failed!")

## User Story 1: ##

# Data Initialization
pdSecure = Security(patient, [patient]) # {patient : patient}
patientData = PatientData('cpr0123', 'syge', pdSecure)

mdSecure = Security(hospital, [patient]) # {hospital : patient}
medicalData = MedicalData([], mdSecure, patientData.cpr)

#TODO Initialize accounting data

hospital.assign_doc(doctor, patient) # assign a doctor
medicalData.security.addReader(doctor) 

# Changing Accounting data

#hospital.accountingData.changePrice(patient,'bingkun', 66666)  #this will fail
hospital.accountingData.changePrice(admin,'bingkun', 66666)

#TODO create all agents
# Make security policies private variables
# assign doctor to patient
# test doctor reading patient data
# insurance provider looks up prices
# Doctor request to add treatment, hospital admin approves/rejects