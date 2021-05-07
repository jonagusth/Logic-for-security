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


command = ' '

while command != '':

    command = input('Choose action or write "help" to see all options: ')

    if (command == "help"):
        print('login')
        print('check in (patients only)')
        print('check out (patients only)')
        print('check history (doctors only)')
        print('order test (doctors only)')
        print('send bill (who sends it?)')
        print('pay bill (insurance only)')
        print('logout?')


    # login command
    if (command == "login"):
        ## User Registration ##
        userId = int(input("User Id: "))
        password = input("Password: ")


        # patient login
        patient = hospital.login(userId,password)
        # doctor login
        doctor = hospital.login(userId, password)
        # Admin login
        admin = hospital.login(userId, password)
        #Insurance staff login
        insurance = hospital.login(userId, password)
        if (patient != None):
            print("Patient login successfully!")
        elif (doctor != None):
            print("Doctor login successfully!")
        elif (admin != None):
            print("Admin login successfully!")
        elif (insurance != None):
            print("Insurance login successfully!")
        else:
            sys.exit("Login failed!")
    
    # check in command
    if (command == "check in"):
        # Patient checking in at hospital
        # If he is a patient
        if patient != None:
            # Promt for his cpr number and insurance provider at the fromnt desk
            cpr = input('cpr: ')
            insuranceProvider = int(input('Insurance provider id (hint, its 4): '))
            # insurance provider is id 4
            patientData = PatientData(cpr, insuranceProvider, Security([patient.id], [0,patient.id]))
            # Patient gets assigned a doctor and by that gives him access to his medical data
            hospital.assign_doc(2, patient.id)
        else: 
            print('Only patients can check in') 

    # check out command
    if (command == "check out"):
        # Patient checking out of hospital
        # If he is a patient
        if patient != None:
            # Patient checks out of hospital and by that gives revokes doctors access to his medical data
            hospital.leave_doc(2, patient.id)
        else: 
            print('Only patients can check out')

    # check history command
    if (command == "check history"):
        # Doctor checking patients medical history
        # If he is a doctor
        if doctor != None:
            patientToCheck = int(input('patient id:'))
            # Patient checks out of hospital and by that gives revokes doctors access to his medical data
            # if doctor is patients doctor
            print(hospital.docPatient)
            hospital.checkMedicalHistory(doctor.id, patientToCheck)
        else: 
            print('Only patients can check out')

      


  ## User Story 1: ##

# Doctor Check the Medical History
hospital.checkMedicalHistory(2, 1)

# Order a Treatment
hospital.orderTest(2, 1, 'Hospital bed for 1 night')

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