from patientData import PatientData
from medicalData import MedicalData
from user import User
import ast
from accountingData import AccountingData
from security import Security

class System:
  def __init__(self):
    # initialize the user data from databse
    file = open('users', 'r')
    self.users = ast.literal_eval(file.read())
    file.close()
    # initialize the medical data from database
    file = open('medicals', 'r')
    meddata = ast.literal_eval(file.read())
    file.close()
    self.medicals = {} # id - medicalData pairs
    for i in meddata:
      self.medicals[i['id']] = MedicalData(i['history'], Security(i['owners'], i['readers']), i['cpr'])
    # initialize the accounting data from database
    file = open('accounts', 'r')
    accdata = ast.literal_eval(file.read())
    file.close()
    self.accounts = {} # id - accountsData pairs
    for i in accdata:
      self.accounts[i['id']] = AccountingData(Security(i['owners'], i['readers']), i['record'])
    # initialize the price of treatment from database
    file = open('prices', 'r')
    self.prices = ast.literal_eval(file.read())
    file.close()

    self.activeUsers = [] #logged in users
    self.docPatient = []
    #TODO add data to txt file

#TODO  hash password
  def login(self, id, password):
    for i in self.users:
      if id == i['id'] and password == i['pw']:
        ret = User(id,i['type'])
        self.activeUsers.append(ret)
        return ret

  def addReader(self, data, reader):
    data.security.readers.append(reader)
  
  def addOwner(self, data, owner):
    data.security.owners.append(owner)

  def popReader(self, data, reader):
    data.security.readers.remove(reader)
  
  def popOwner(self, data, owner):
    data.security.owners.remove(owner)
  

#TODO add assign patient to doctor function
  def assign_doc(self, doctor, patient):
    self.docPatient.append({doctor:patient})
    self.addReader(self.medicals[patient], doctor)
    self.addOwner(self.medicals[patient], doctor)
    print('patient', patient, 'assigned to doctor', doctor)

  def leave_doc(self, doctor, patient):
    self.docPatient.remove({doctor:patient})
    self.popReader(self.medicals[patient], doctor)
    self.popOwner(self.medicals[patient], doctor)
    print('patient', patient, 'leave doctor', doctor)

  def checkMedicalHistory(self, doctor, patient):
    if doctor in self.medicals[patient].security.readers:
      print("Doctor check the medical history!")
    else:
      print("Doctor does not have access to this patient's data!")

  def orderTest(self, doctor, patient, treatment):
    if doctor in self.medicals[patient].security.owners:
      self.medicals[patient].history.append({'name':treatment, 'result':'standard'})
      self.accounts[patient].record.append({'name':treatment, 'cost':self.prices[treatment], 'status':'unpaid'})
      print("Treatment conducted!")
    else:
      print("Doctor not authorized to order a test!")

  def sendBill(self, patient, patientData):
    if 0 in patientData.security.readers:
      self.addReader(self.accounts[patient], patientData.ip)
      print("patient", patient, "'s bill send to insurance")
    else:
      print("Can't find insurance! patient data not provided!")

  def checkBillandPay(self, ip, patient):
    if ip in self.accounts[patient].security.readers:
      print("Patient", patient, "'s bill checked by insurance", ip)
      for item in self.accounts[patient].record:
        if item['status'] == 'unpaid':
          #if insurance provider has paid the bill
          item['status'] = 'paid'
          print("Patient", patient, item['name'], "paid by insurance", ip)
      billClear = True
      for item in self.accounts[patient].record:
        if item['status'] == 'unpaid':
          print("Patient", patient, "still has unpaid items!")
          billClear = False
      if billClear:
        print("Patient", patient, "'s bill all paid")
        self.popReader(self.accounts[patient], ip)
      
    else:
      print("Insurance provider has no access to this patient's account!")
  
  
  

  



