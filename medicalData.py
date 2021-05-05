from security import Security
class MedicalData:
  def __init__(self, history, security, cpr):
    self.security = security #Owner and readers
    self.cpr = cpr
    self.history = history #record of every test ordered for patient and the results

