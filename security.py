from user import User
class Security:
  def __init__(self, owner, readers):
    self.owner = owner
    self.readers = readers

#TODO
#Add functions for 
#   adding readers
#   remove readers
#   add owners
#   remover owners (only remove themself maybe)
#   declassify
  def addReader(self, reader):
    self.readers.append(reader)

  def addOwner(self, owner):
    self.owner.append(owner)

  def removeReader(self, reader):
    self.readers.remove(reader)

  def removeOwner(self, owner):
    self.owner.remove(owner)
