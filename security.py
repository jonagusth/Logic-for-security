from user import User
class Security:
  def __init__(self, owner, readers):
    self.owner = name
    self.readers = readers

#TODO
#Add functions for 
#   adding readers
<<<<<<< Updated upstream
=======
  def add_reader(self, reader):
    self.readers.append(reader)

>>>>>>> Stashed changes
#   remove readers
  def removeReader(self, reader):
    self.readers.remove(reader)

#   add owners
  def addOwner(self, owner):  
    self.owner.append(owner)
#   remover owners (only remove themself maybe)

def removeOwner(self, owner):
    self.owner.remove(owner)
#   declassify
