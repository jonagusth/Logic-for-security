from security import Security

class PatientData:
  def __init__(self, cpr, ip, security):
    self.cpr = cpr
    self.ip = ip #Insurance provider
    self.security = security #Owner and readers

