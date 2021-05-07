#TODO ADD EVERY IMPORT
#Script file for testing our implementation
from medicalData import MedicalData
from security import Security
from system import System
from patientData import PatientData
import random

import sys
#TODO add command line functionality

## Initialize the System
hospital = System()
checkedIn = False
currUser = None
patient = None
doctor = None
admin = None
insurance = None


command = ' '

while command != '':

    command = input('Choose action or write "help" to see all options: ')

    if (command == "help"):
        print('login')
        print('check in (patients only)')
        print('check out (patients only)')
        print('check history (doctors only)')
        print('order test (doctors only)')
        print('pay bill (insurance only)')
        print('status (who is logged in?)')
        print('users')
        print('logout')


    # login command
    if (command == "login"):
        if currUser != None:
            print('You are already logged in as user: {}')
        else:
            ## User Registration ##
            tmp = ''
            while tmp.isdigit() == False:
                tmp = input("User Id: ")
                if tmp.isdigit():
                    if int(tmp) > len(hospital.users):
                        print('User does not exist')
                    else: 
                        userId = int(tmp)
                else: 
                    print('Invalid user Id')

            while currUser == None:
                password = input('Password (hint: its "password"): ')
                currUser = hospital.login(userId,password)
            
            if currUser.type == 1:
                # patient login
                patient = currUser
                print("Patient login successfully!")
            elif currUser.type == 2:
                # doctor login
                doctor = currUser
                print("Doctor login successfully!")
            elif currUser.type == 3:
                # Admin login
                admin = currUser
                print("Admin login successfully!")
            elif currUser.type == 3:
                #Insurance staff login
                insurance = currUser
                print("Insurance login successfully!")
            else:
                sys.exit("Login failed!")

    elif (command == "logout"):
        print('user {} logged out successfully'.format(currUser.id))
        patient = None
        doctor = None
        admin = None
        insurance = None
        currUser = None
    
    # check in command
    elif (command == "check in"):
        # Patient checking in at hospital
        # If he is a patient and logged in
        if currUser != None:
            if patient != None:
                # Promt for his cpr number and insurance provider at the fromnt desk
                cpr = input('cpr: ')
                tmp = ''
                insuranceProvider = None
                while tmp.isdigit() == False:
                    tmp = input('Insurance provider id (hint, its 4): ')
                    if tmp.isdigit():
                        if int(tmp) in hospital.iProviders:
                            insuranceProvider = int(tmp)
                        else: 
                            print('insurance provider does not exist ( told you it was 4 :P )')
                    else: 
                        print('Invalid id')
                # insurance provider is id 4
                patientData = PatientData(cpr, insuranceProvider, Security([patient.id], [0,patient.id]))
                # Patient gets assigned a random doctor and by that gives him access to his medical data
                doc = random.choice(hospital.doctors)
                hospital.assign_doc(2, patient.id)
                checkedIn = True
            else: 
                print('Only patients can check in') 
        else:
            print('You have to be logged in')

    # check out command
    elif (command == "check out"):
        # Patient checking out of hospital
        # If he is a patient and logged in and checked in
        if currUser != None:
            if checkedIn:
                if patient != None:
                    # Patient checks out of hospital and by that revokes doctors access to his medical data
                    # His bill is also automatically sent to his insurance provider ( ip added to readers list of bill)
                    k = None
                    for i in hospital.docPatient:
                        key_list = list(i.keys())
                        val_list = list(i.values())
                        if patient.id in val_list:
                            index = val_list.index(patient.id)
                            k = key_list[index]
                    hospital.leave_doc(k, patient.id)
                    hospital.sendBill(patient.id, patientData)
                    # patient removes the hospital from readers of his data
                    patientData.security.readers.remove(0) 
                else: 
                    print('Only patients can check out')
            else:
                print('You have to be checked in to be able to check out')
        else:
            print('You have to be logged in')

    # check history command
    elif (command == "check history"):
        # Doctor checking patients medical history
        # If he is a doctor and logged in
        if currUser != None:
            if doctor != None:
                tmp = ''
                patientToCheck = None
                while tmp.isdigit() == False:
                    tmp = input('patient id:')
                    if tmp.isdigit():
                        if int(tmp) > len(hospital.users):
                            print('User does not exist')
                        else: 
                            patientToCheck = int(tmp)
                    else: 
                        print('Invalid user Id')
                # Doctor checks medical history of patient if he is the patients doctor
                print(hospital.docPatient)
                hospital.checkMedicalHistory(doctor.id, patientToCheck)
            else: 
                print('Only patients can check out')
        print('You have to be logged in')
    
    # order test command
    elif (command == "order test"):
        # Doctor ordering a test for a patient
        # If he is a doctor and logged in
        if currUser != None:
            if doctor != None:
                tmp = ''
                patientToTest = None
                while tmp.isdigit() == False:
                    tmp = input('patient to test:')
                    if tmp.isdigit():
                        if int(tmp) > len(hospital.users):
                            print('User does not exist')
                        else: 
                            patientToTest = int(tmp)
                    else: 
                        print('Invalid user Id')
                test = input('test/treatment to perform:')
                # Doctor orders a test for the patient and if alloweed its added to patients medical file
                hospital.orderTest(doctor.id, patientToTest, test)
            else: 
                print('Only patients can check out')
        print('You have to be logged in')

    # pay bill command
    elif (command == "pay bill"):
        # insurance provider paying the bill for a patient
        # If he is an insurance provider and logged in
        if currUser != None:
            if insurance != None:
                # Doctor orders a test for the patient and if alloweed its added to patients medical file
                tmp = ''
                patientToPayFor = None
                while tmp.isdigit() == False:
                    tmp = input('patient to pay bill for:')
                    if tmp.isdigit():
                        if int(tmp) > len(hospital.users):
                            print('User does not exist')
                        else: 
                            patientToPayFor = int(tmp)
                    else: 
                        print('Invalid user Id')
                hospital.checkBillandPay(insurance.id, patientToPayFor)
            else: 
                print('Only insurance providers can pay bills')
        print('You have to be logged in')

    # status command
    elif (command == "status"):
        if currUser != None:
            if patient != None:
                if checkedIn:
                    print('You are logged in as patient {} and you are checked in'.format(patient.id))
                else:
                    print('You are logged in as patient {} but you are not checked in'.format(patient.id))
            if doctor != None:
                print('You are logged in as doctor {}'.format(doctor.id))
            if insurance != None:
                print('You are logged in as insurance provider {}'.format(insurance.id))
        else:
            print('You are not logged in')

    # users command
    elif (command == "users"):
        if currUser != None:
            print('You are already logged in, this is a function to help you log in with the appropriate user')
        else:
            print('User 1: user id: 1, pw: password, type: patient')
            print('User 2: user id: 2, pw: password, type: doctor')
            print('User 3: user id: 3, pw: password, type: doctor')
            print('User 4: user id: 4, pw: password, type: insurance provider')

    else:
        print('Invalid command, type "help" too see all options')


#TODO
# Make security policies private variables
# assign doctor to patient
# test doctor reading patient data
# insurance provider looks up prices
# Doctor request to add treatment, hospital admin approves/rejects