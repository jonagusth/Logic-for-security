from user import User
import ast
from accountingData import AccountingData
from security import Security

class System:
  def __init__(self):
    self.users = [] #logged in users
    self.data = [{'id':1, 'pw':'password','type':1},{'id':2,'pw':'qwerty','type':2}, {'id':3,'pw':'password','type':3}] #database of users and passwords
    self.docPatient = {}
    file = open('prices', 'r')
    prices = ast.literal_eval(file.read())
    file.close()

    self.accountingData = AccountingData(Security([3],[3,4]), prices)
    #TODO add data to txt file

#TODO  hash password
  def login(self, id, password):
    for i in self.data:
      if id == i['id'] and password == i['pw']:
        # print('Success')
        ret = User(id,i['type'])
        self.users.append(ret)
        return ret

#TODO add assign patient to doctor function
  def assign_doc(self, docter, patient):
    self.docPatient[docter] = patient

  def get_docPatient(self):
    return self.docPatient


