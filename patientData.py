import Security from security

class PatientData:
  def __init__(self, cpr, ip,Security):
    self.cpr = cpr
    self.ip = ip #Insurance provider
    self.Security = Security #Owner and readers

