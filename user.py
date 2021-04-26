class User:
  def __init__(self, pw, id, type):
    self.password = pw #Maybe token instead
    self.id = id
    self.type = type #1 for patients, 2 for doctors, 3 for admin staff, 4 for insurance staff

