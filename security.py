from user import User
class Security:
  def __init__(self, owner, readers):
    self.owner = owner
    self.readers = readers

#TODO We have to add that "is it allowed?"
#Add functions for 
#   adding readers
  def addReader(self, reader):
    self.readers.append(reader)

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
