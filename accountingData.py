from security import Security
class AccountingData:
  def __init__(self, security, record):
    self.security = security #Owner and readers
    self.record = record

#TODO CHANGE TO ROLE BASED ACCESS CONTROL ONLY FOR THIS OBJECT
#TODO Add View price function
#Changing price of something

  # def changePrice(self, user, service, newPrice): 
  #   if user.type in self.security.owner:  ## setting owners based on user id ?? how we gonna check who is changing?
  #     self.prices[service] = newPrice
  #     with open('prices', 'w') as f:
  #       print(self.prices, file=f)
  #     print('Prices updated:')
  #     print(self.prices)
  #   else: 
  #     print('No access to change Accounting Data')
