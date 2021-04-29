from security import Security
class AccountingData:
  def __init__(self,Security,Prices):
    self.Security = Security #Owner and readers
    self.Prices #Prices of beds, tests of extra services

#TODO Add functions
#Changing price of something

  #Check if user logged in?
  def changePrice(self, user, service, newPrice): 
    if user.type in self.Security.owner:  ## setting owners based on user id ?? how we gonna check who is changing?
      self.Prices[service] = newPrice
      with open('prices', 'w') as f:
        print(self.Prices, file=f)
      print('Prices updated:')
      print(self.Prices)
    else: 
      print('No access to change Accounting Data')
