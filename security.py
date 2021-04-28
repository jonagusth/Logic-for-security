from user import User
class Security:
  def __init__(self, owner, readers):
    self.owner = owner
    self.readers = readers

#TODO
#Add functions for 
#   adding readers
  def add_reader(self, reader):
    self.readers.append(reader)
#   remove readers
#   add owners
#   remover owners (only remove themself maybe)
#   declassify
