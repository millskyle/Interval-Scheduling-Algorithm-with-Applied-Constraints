



class UserPreferences():
   def __init__(self):
      self.semester = "201509"
      self.MaximizeDaysOff = True
      self.PreferredDaysOff = []
      self.PreferTimeOfDay = "Evening" 
      # Options "Morning", "Afternoon", "Evening"
      self.optimumTimeOfDay = "0800"
      # Sets preferred time for Gaussian
      self.preferredCampus = 0
      #0 for none, 1 for north, 2 for dt
      self.preferredCRNs = []
      self.preferMinGaps = True
      self.RespectRegistration = True
UserPrefs = UserPreferences()
