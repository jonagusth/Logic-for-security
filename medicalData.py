import Security from security
class MedicalData:
  def __init__(self, Security, history):
    self.Security = Security #Owner and readers
    self.history = history #record of every test ordered for patient and the results

