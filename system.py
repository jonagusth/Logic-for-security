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
    file = open('docPatients', 'r')
    self.docPatient = ast.literal_eval(file.read())
    file.close()

    self.patients = []

    for i in self.users:
      if i['type'] == 1:
        self.patients.append(i['id'])

    self.doctors = []

    for i in self.users:
      if i['type'] == 2:
        self.doctors.append(i['id'])
    
    self.iProviders = []

    for i in self.users:
      if i['type'] == 4:
        self.iProviders.append(i['id'])

    self.user = None
    #TODO add data to txt file

#TODO  hash password
  def login(self, id, password):
    for i in self.users:
      if id == i['id'] and password == i['pw']:
        ret = User(id,i['type'])
        # self.activeUsers.append(ret)
        self.user = ret
        return ret 
    print('invalid user Id or password')

  def logout(self, id):
    self.user = None

  def addReader(self, data, reader):
    if reader not in data.security.readers:
      data.security.readers.append(reader)
  
  def addOwner(self, data, owner):
    if owner not in data.security.owners:
      data.security.owners.append(owner)

  def popReader(self, data, reader):
    if reader in data.security.readers:
      data.security.readers.remove(reader)
  
  def popOwner(self, data, owner):
    if owner in data.security.owners:
      data.security.owners.remove(owner)
  

#TODO add assign patient to doctor function
  def assign_doc(self, doctor, patient):
    if {doctor:patient} not in self.docPatient:
      self.docPatient.append({doctor:patient})
    with open('docPatients', 'w') as f:
      print(self.docPatient, file=f)
    self.addReader(self.medicals[patient], doctor)
    self.addReader(self.medicals[patient], patient)
    self.addOwner(self.medicals[patient], doctor)
    #print(self.medicals[patient].data)
    # [{'owners':[0], 'readers':[0], 'id':1, 'cpr':123456, 'history':[{'name':'Blood test', 'result':'standard'}]}]
    tmp = [{'owners':self.medicals[patient].security.owners, 'readers':self.medicals[patient].security.readers, 'id':patient, 'cpr':self.medicals[patient].cpr, 'history':self.medicals[patient].history}]
    with open('medicals', 'w') as f:
      print(tmp, file=f)
    print('patient {} assigned to doctor {}'.format(patient, doctor))

  def leave_doc(self, doctor, patient):
    self.docPatient.remove({doctor:patient})
    with open('docPatients', 'w') as f:
      print(self.docPatient, file=f)
    self.popReader(self.medicals[patient], doctor)
    self.popOwner(self.medicals[patient], doctor)
    tmp = [{'owners':self.medicals[patient].security.owners, 'readers':self.medicals[patient].security.readers, 'id':patient, 'cpr':self.medicals[patient].cpr, 'history':self.medicals[patient].history}]
    with open('medicals', 'w') as f:
      print(tmp, file=f)
    print('patient {} leaves doctor {}'.format(patient, doctor))

  def checkMedicalHistory(self, reader, patient):
    if reader in self.medicals[patient].security.readers:
      if reader == patient:
        print('Patient checks his own medical history')
        print(self.medicals[patient].history)
      else:
        print("Doctor check the medical history:")
        print(self.medicals[patient].history)
    else:
      print("User does not have access to this patient's data!")

  def orderTest(self, doctor, patient, treatment):
    if doctor in self.medicals[patient].security.owners:
      self.medicals[patient].history.append({'name':treatment, 'result':'standard'})
      if treatment not in self.prices:
        self.prices[treatment] = 1111 # dummy price for new service
        with open('prices', 'w') as f:
          print(self.prices, file=f)
      self.accounts[patient].record.append({'name':treatment, 'cost':self.prices[treatment], 'status':'unpaid'})
      tmp = [{'owners':self.medicals[patient].security.owners, 'readers':self.medicals[patient].security.readers, 'id':patient, 'cpr':self.medicals[patient].cpr, 'history':self.medicals[patient].history}]
      with open('medicals', 'w') as f:
        print(tmp, file=f)

      tmp1 = [{'owners':self.accounts[patient].security.owners, 'readers':self.accounts[patient].security.readers, 'id':patient, 'record':self.accounts[patient].record}]
      with open('accounts', 'w') as f:
        print(tmp1, file=f)
      print("{} added to patients hospital bill for: {}".format(self.prices[treatment], treatment))
    else:
      print("Doctor not authorized to order a test!")

  def sendBill(self, patient, patientData):
    if 0 in patientData.security.readers:
      self.addReader(self.accounts[patient], patientData.ip)
      print("patient {}'s bill sent to his insurance provider".format(patient))
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
  
  
  

  



