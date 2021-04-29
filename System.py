from user import User
from accountingData import AccountingData
from security import Security
import ast

class System:
  def __init__(self):
    self.users = [] #logged in users
    self.data = [{'id':1, 'pw':'password','type':1},{'id':2,'pw':'qwerty','type':2},{'id':3,'pw':'password','type':3}] #database of users and passwords
    self.medicalData = [{'blood':'its red', 'cancer':'Positive','covid':'Negative', 'vaccine':'Phizer'}]
    
    file = open('prices', 'r')
    prices = ast.literal_eval(file.read())
    file.close()
    
    self.accountingData = AccountingData(Security([3],[3,4]), prices)

    #TODO add data to txt file

#TODO  hash password
  def login(self, id, password):
    for i in self.data:
      if id == i['id'] and password == i['pw']:
        print('User {} Successfully logged in'.format(id))
        ret =User(id,i['type'])
        self.users.append(ret)
        return ret

#TODO add assign patient to doctor function


