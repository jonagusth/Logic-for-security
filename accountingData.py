from security import Security
class AccountingData:
  def __init__(self, security, prices):
    self.security = security #Owner and readers
    self.prices = prices #Prices of beds, tests of extra services

#TODO Add functions
#Changing price of something

  def changePrice(self, user, service, newPrice): 
    if user.type in self.security.owner:  ## setting owners based on user id ?? how we gonna check who is changing?
      self.prices[service] = newPrice
      with open('prices', 'w') as f:
        print(self.prices, file=f)
      print('Prices updated:')
      print(self.prices)
    else: 
      print('No access to change Accounting Data')
